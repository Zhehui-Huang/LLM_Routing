import sys
from openai import OpenAI
import google.generativeai as genai
import re
from utils import extract_execute_code, nltd_to_math, consistent_check, read_file, nltd_to_math_requirements, \
    gpt_prompt_tips, gemini_prompt_tips

# OpenAI
client = OpenAI()
gpt_model = "gpt-4-0125-preview"
python_file_path = 'tmp/4_refine_extracted_code.py'
vis_file_path = 'tmp/vis_5_external_tools_extracted_code.py'

# Gemini
GOOGLE_API_KEY = "AIzaSyBruy7vdcDDCHfIrNxgiYkBhAl7g2ajXGA"
genai.configure(api_key=GOOGLE_API_KEY)

consistent_check_count = 2
refine_count = 5


def solve_problem(task_descriptions, env_and_task):
    # Init Gemini
    gemini_model = genai.GenerativeModel('gemini-pro')
    gemini_chat = gemini_model.start_chat(history=[])

    consistent_check_bool = False

    for check_id in range(consistent_check_count):
        print(f"Check count: {check_id + 1}")
        # 1. Translate natural language task descriptions (NLTD) to mathematical formulations.
        math_content_modify = nltd_to_math(client=client, gpt_model=gpt_model, task_descriptions=task_descriptions)

        # 2. Combine (NLTD + Mathematical formulation) to check consistent
        # # GPT 4
        consistent_check_content, consistent_check_input = consistent_check(
            client=client, gpt_model=gpt_model, task_descriptions=task_descriptions, env_and_task=env_and_task,
            math_content_modify=math_content_modify)

        # # Gemini
        gemini_consistent_check_reply = gemini_chat.send_message(f"{consistent_check_input} {gemini_prompt_tips}")
        gemini_consistent_check_content = gemini_consistent_check_reply.text

        print('GPT4 consistent check:    ', consistent_check_content, sep='\n')
        print('====================================================================================================')
        print('Gemini consistent check:    ', gemini_consistent_check_content, sep='\n')
        print('====================================================================================================')

        gpt_consistent_bool = "***yes***" in consistent_check_content
        gemini_consistent_bool = "***yes***" in gemini_consistent_check_content
        all_consistent_bool = gpt_consistent_bool and gemini_consistent_bool

        if all_consistent_bool is False:
            print('Please clarify the task descriptions.')
            clarifications_from_user = input("")
            clarifications_from_user_prex = "### Following are clarifications of tasks from user."

            clarification_questions = ""
            if gpt_consistent_bool is False:
                clarification_questions += f"### Clarification questions from GPT 4: {consistent_check_content} ###"
            if gemini_consistent_bool is False:
                clarification_questions += f"### Clarification questions from Gemini: {gemini_consistent_check_content} ###"

            consistent_check_content_modified = f"{clarifications_from_user_prex} {clarifications_from_user} ###"
            task_descriptions = (f"{env_and_task} {clarification_questions} {consistent_check_content_modified} "
                                 f"{nltd_to_math_requirements} {gpt_prompt_tips}")
            print('Modified Task descriptions: ', task_descriptions, sep='\n')
            continue
        else:
            consistent_check_bool = True
            break

    if consistent_check_bool is False:
        print('Fail in consistent check.')
        return

    # 3. Math to solution
    pre_problem_solving_questions = (
        "### Solution requirements: Please use Python code to solve the above mathematical problem. "
        "Even if the task requires optimal solution, as long as you think it is too compute intensive, "
        "you can provide a feasible solution with a heuristic solver. "
        "If there is no solution, only print ***no solution***. "
        "If there is a solution, please only output Python code without any analysis. In the Python code, you must "
        "1. Print tour of each robot (template: Place <text> -> Place <text>) "
        "2. Print cost (template: Cost: <text>). ###"
    )

    problem_solving_questions = f"{pre_problem_solving_questions} {gpt_prompt_tips}"

    init_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": task_descriptions},
        {"role": "assistant", "content": math_content_modify},
        {"role": "user", "content": problem_solving_questions}
    ]

    cost_value_list = []
    final_solution_content = None
    for count in range(refine_count):
        solution_reply = client.chat.completions.create(
            model=gpt_model,
            messages=init_messages,
            stream=False,
        )
        solution_content = solution_reply.choices[0].message.content
        print('Solutions: ', solution_content, sep='\n')
        print('====================================================================================================')

        # Attempt to solve
        external_solutions = extract_execute_code(problem_solving_content=solution_content,
                                                  python_file_path=python_file_path)

        # Regular expression to find a floating point number after "cost"
        cost_match = re.search(r'cost.*?([\d.]+)', external_solutions.stdout, re.IGNORECASE)
        cost_value = float(cost_match.group(1)) if cost_match else None
        if cost_value is None:
            print("No cost value found in the solution.")
            break

        cost_value_list.append(cost_value)

        final_solution_content = solution_content

        more_than_two = any(cost_value_list.count(x) >= 2 for x in set(cost_value_list))
        if more_than_two:
            print(f"The final best cost is: {cost_value}")
            break

        # From assistant
        tmp_assistent_message = {"role": "assistant", "content": f"{solution_content} {external_solutions.stdout}"}
        init_messages.append(tmp_assistent_message)
        # From refine
        tmp_refine_message = {
            "role": "user",
            "content": f"Please provide a better solution with Python code."}
        init_messages.append(tmp_refine_message)

    # 4. Solve the problem
    print('Final solution!')
    external_solutions = extract_execute_code(problem_solving_content=final_solution_content,
                                              python_file_path=python_file_path)

    # Visualize solution
    tmp_refine_input = ("### Task: please visualize the solution with Python code. You should mark each movement with "
                        "an arrow. You should put cost in the top-right corner of the plot. You MUST ONLY output the "
                        "Python code. ###")
    visualize_refine_input = f"### Here is the solution {external_solutions.stdout} ### {tmp_refine_input}"
    print("visualize_refine_input: ", visualize_refine_input, sep="\n")

    vis_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"{env_and_task} {visualize_refine_input} {gpt_prompt_tips}"},
    ]

    visualize_solution_reply = client.chat.completions.create(
        model=gpt_model,
        messages=vis_messages,
        stream=False,
    )

    visualize_content = visualize_solution_reply.choices[0].message.content
    print('visualize_content: ', visualize_content)
    print('====================================================================================================')

    # 4. Vis the problem
    vis_external_solutions = extract_execute_code(problem_solving_content=visualize_content,
                                                  python_file_path=vis_file_path)

    print('End!')


def main():
    env_and_task = read_file(file_path="task/middle/1.txt")

    task_descriptions = f"{env_and_task} {nltd_to_math_requirements} {gpt_prompt_tips}"

    solve_problem(task_descriptions=task_descriptions, env_and_task=env_and_task)


if __name__ == '__main__':
    sys.exit(main())
