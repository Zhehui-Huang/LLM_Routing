import sys
import os

from openai import OpenAI

from utils import extract_execute_code, read_file, gpt_prompt_tips, read_all_files

from task_specify_sol_req import sol_req

client = OpenAI()
gpt_model = "gpt-4-0125-preview"


def solve_problem(task_descriptions, python_file_path, env_and_task, sol_given_parts):
    # 1. Translate natural language task descriptions (NLTD) to solutions.
    problem_solving_reply = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": task_descriptions}
        ],
        stream=False,
    )
    problem_solving_content = problem_solving_reply.choices[0].message.content
    print('Solutions: ', problem_solving_content, sep="\n")

    # 2. Print the solution
    external_solutions = extract_execute_code(problem_solving_content=problem_solving_content,
                                              python_file_path=python_file_path)
    find_solution_flag = False
    for reflect_id in range(5):
        print(f'Reflection round: {reflect_id}')
        if external_solutions.stderr == "":
            tmp_solution = external_solutions.stdout
        else:
            tmp_solution = external_solutions.stderr

        tmp_modified_solution = f"### Here is the solution: {tmp_solution} ###"
        env_and_task_description = f"'''Following are natural language task descriptions: {env_and_task} '''"
        question_for_answer = (
            "### Question: Is the solution meets the requirements? If yes, you must only output: <**Yes**> "
            "If not, please give me a corrected version with Python code. ###")
        reflect_input = f"{env_and_task_description} {tmp_modified_solution} {question_for_answer} {sol_given_parts}"

        reflect_input_reply = client.chat.completions.create(
            model=gpt_model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": reflect_input}
            ],
            stream=False,
        )

        reflect_input_content = reflect_input_reply.choices[0].message.content
        print('reflect_input_content: ', reflect_input_content, sep="\n")
        if "**Yes**" in reflect_input_content:
            print(f'Find the correct solution in round: {reflect_id}!')
            find_solution_flag = True
            break
        else:
            find_solution_flag = False
            print(f'In round: {reflect_id}, the solution is not correct!')
            modified_python_file_path = python_file_path[:-3] + f'_reflect_{reflect_id}' + '.py'
            external_solutions = extract_execute_code(problem_solving_content=reflect_input_content,
                                                      python_file_path=modified_python_file_path)

    if find_solution_flag is False:
        print(f'Can not find the solution!')

    print('End!')


def main():
    text_files_loc = read_all_files(root_directory='task/E-m_tsp_max_score_with_time_budget')
    print('file number:', len(text_files_loc), sep='\n')
    for file_path in text_files_loc:
        for id in range(3):
            env_and_task = read_file(file_path=file_path)
            python_file_path = 'solution/1_direct_no_vis' + file_path[4:-4] + f'_{id}' + '.py'
            directory = os.path.dirname(python_file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)

            print('python_file_path:', python_file_path, sep='\n')
            # if os.path.exists(python_file_path):
            #     print('python_file_path exists:', python_file_path, sep='\n')
            #     continue

            parts = file_path.split('/')
            robot_num = '1'
            if int(parts[2][0]) > 1:
                robot_num = 'M'
            sol_given_parts_key = f"{parts[1][0]}_{robot_num}"
            sol_given_parts = sol_req[sol_given_parts_key]
            task_descriptions = f"{env_and_task} {sol_given_parts} {gpt_prompt_tips}"

            solve_problem(task_descriptions=task_descriptions, python_file_path=python_file_path,
                          env_and_task=env_and_task, sol_given_parts=sol_given_parts)


if __name__ == '__main__':
    sys.exit(main())
