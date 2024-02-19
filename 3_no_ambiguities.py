import sys
import os

import google.generativeai as genai
from openai import OpenAI

from task_specify_sol_req import sol_req
from utils import extract_execute_code, math_to_solution, read_file, \
    nltd_to_math_requirements, gpt_prompt_tips, read_all_files, total_consistent_check, \
    save_evaluation

# OpenAI
client = OpenAI()
gpt_model = "gpt-4-0125-preview"

# Gemini
GOOGLE_API_KEY = "AIzaSyBruy7vdcDDCHfIrNxgiYkBhAl7g2ajXGA"
genai.configure(api_key=GOOGLE_API_KEY)

# Solution path
sol_path = 'solution/3_no_ambiguities'

consistent_check_count = 2


def solve_problem(task_descriptions, python_file_path, env_and_task, sol_given_parts):
    # Init Gemini
    gemini_model = genai.GenerativeModel('gemini-pro')
    gemini_chat = gemini_model.start_chat(history=[])

    consistent_check_bool, math_content_modify = total_consistent_check(
        consistent_check_count=consistent_check_count, client=client, gpt_model=gpt_model,
        task_descriptions=task_descriptions, env_and_task=env_and_task, gemini_chat=gemini_chat)

    if consistent_check_bool is False:
        print('Fail in consistent check.')
        return

    # 3. Math to solution
    solution_content = math_to_solution(client=client, gpt_model=gpt_model, task_descriptions=task_descriptions,
                                        math_content_modify=math_content_modify, prompt_tips=gpt_prompt_tips,
                                        sol_given_parts=sol_given_parts)
    # 4. Solve the problem
    external_solutions, total_time = extract_execute_code(problem_solving_content=solution_content,
                                                          python_file_path=python_file_path)
    # 5. Save the evaluation
    save_evaluation(python_file_path=python_file_path, external_solutions=external_solutions, total_time=total_time)
    print('End!')


def main():
    text_files_loc = read_all_files(root_directory='task')
    print('file number:', len(text_files_loc), sep='\n')
    for file_path in text_files_loc:
        for tid in range(3):
            env_and_task = read_file(file_path=file_path)
            python_file_path = sol_path + file_path[4:-4] + f'_{tid}' + '.py'
            directory = os.path.dirname(python_file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)

            if os.path.exists(python_file_path):
                print('python_file_path exists:', python_file_path, sep='\n')
                continue

            print('python_file_path:', python_file_path, sep='\n')
            parts = file_path.split('/')
            robot_num = '1'
            if int(parts[2][0]) > 1:
                robot_num = 'M'
            sol_given_parts_key = f"{parts[1][0]}_{robot_num}"
            sol_given_parts = sol_req[sol_given_parts_key]
            task_descriptions = f"{env_and_task} {nltd_to_math_requirements}"

            solve_problem(task_descriptions=task_descriptions, python_file_path=python_file_path,
                          env_and_task=env_and_task, sol_given_parts=sol_given_parts)


if __name__ == '__main__':
    sys.exit(main())
