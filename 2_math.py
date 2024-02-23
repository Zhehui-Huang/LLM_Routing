import sys
import os

from openai import OpenAI
from utils import (extract_execute_code, nltd_to_math, math_to_solution, read_file, gpt_prompt_tips,
                   nltd_to_math_requirements, read_all_files, save_evaluation)

from task_specify_sol_req import sol_req

client = OpenAI()
gpt_model = "gpt-4-0125-preview"
sol_path = 'solution/2_direct_math'


def solve_problem(task_descriptions, python_file_path, sol_given_parts):
    # 1. Translate natural language task descriptions (NLTD) to mathematical formulations.
    math_content_modify = nltd_to_math(client=client, gpt_model=gpt_model, task_descriptions=task_descriptions)
    # 2. Math to solution
    solution_content = math_to_solution(client=client, gpt_model=gpt_model, task_descriptions=task_descriptions,
                                        math_content_modify=math_content_modify, prompt_tips=gpt_prompt_tips,
                                        sol_given_parts=sol_given_parts)

    # 3. Solve the problem
    external_solutions, total_time = extract_execute_code(problem_solving_content=solution_content,
                                                          python_file_path=python_file_path)
    # 4. Save the evaluation
    save_evaluation(python_file_path=python_file_path, external_solutions=external_solutions, total_time=total_time)
    print('End!')


def main():
    text_files_loc = read_all_files(root_directory='task_v3')
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
            if int(parts[1][0]) > 1:
                robot_num = 'M'
            sol_given_parts_key = f"{parts[2][0]}_{robot_num}"
            sol_given_parts = sol_req[sol_given_parts_key]
            task_descriptions = f"{env_and_task} {nltd_to_math_requirements}"

            solve_problem(task_descriptions=task_descriptions, python_file_path=python_file_path,
                          sol_given_parts=sol_given_parts)


if __name__ == '__main__':
    sys.exit(main())
