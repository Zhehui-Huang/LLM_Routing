import sys
from openai import OpenAI
import google.generativeai as genai

from utils import extract_execute_code, nltd_to_math, consistent_check, math_to_solution, read_file, \
    nltd_to_math_requirements, gpt_prompt_tips, gemini_prompt_tips

# OpenAI
client = OpenAI()
gpt_model = "gpt-4-0125-preview"
python_file_path = 'tmp/3_no_ambiguities_extracted_code.py'

# Gemini
GOOGLE_API_KEY = "AIzaSyBruy7vdcDDCHfIrNxgiYkBhAl7g2ajXGA"
genai.configure(api_key=GOOGLE_API_KEY)

consistent_check_count = 2


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
    solution_content = math_to_solution(client=client, gpt_model=gpt_model, task_descriptions=task_descriptions,
                                        math_content_modify=math_content_modify, prompt_tips=gpt_prompt_tips)
    # 4. Solve the problem
    extract_execute_code(problem_solving_content=solution_content, python_file_path=python_file_path)
    print('End!')


def main():
    env_and_task = read_file(file_path="task/simple/5.txt")

    task_descriptions = f"{env_and_task} {nltd_to_math_requirements} {gpt_prompt_tips}"

    solve_problem(task_descriptions=task_descriptions, env_and_task=env_and_task)


if __name__ == '__main__':
    sys.exit(main())
