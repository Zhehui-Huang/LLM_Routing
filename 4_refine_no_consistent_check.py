import os
import sys

import google.generativeai as genai
from openai import OpenAI

from task_specify_sol_req import sol_req
from utils import (read_file, nltd_to_math_requirements, gpt_prompt_tips, read_all_files, save_evaluation, refine,
                   nltd_to_math)

# OpenAI
client = OpenAI()
gpt_model = "gpt-4-0125-preview"

# Gemini
GOOGLE_API_KEY = "AIzaSyBruy7vdcDDCHfIrNxgiYkBhAl7g2ajXGA"
genai.configure(api_key=GOOGLE_API_KEY)

# Solution path
sol_path = 'solution/4_refine_no_consistent_check'

consistent_check_count = 2
refine_count = 3


def solve_problem(task_descriptions, python_file_path, env_and_task, sol_given_parts):
    # Init Gemini
    math_content_modify = nltd_to_math(client=client, gpt_model=gpt_model, task_descriptions=task_descriptions)

    # Refine
    problem_solving_questions = (
        f"Given above mathematical problem, please provide a solution. {sol_given_parts} "
        "!!! Even if the task asked for optimal solution, as long as you think it is too compute intensive, "
        "you can provide a feasible solution with a heuristic solver. !!!"
        f"{sol_given_parts}"
    )

    init_messages = [
        {"role": "system", "content": f"You are a helpful assistant. {gpt_prompt_tips}"},
        {"role": "user", "content": task_descriptions},
        {"role": "assistant", "content": math_content_modify},
        {"role": "user", "content": problem_solving_questions}
    ]

    final_external_solutions, final_total_time = refine(
        refine_count=refine_count, client=client, gpt_model=gpt_model, init_messages=init_messages,
        python_file_path=python_file_path, sol_given_parts=sol_given_parts, math_content_modify=math_content_modify)

    # Save evaluation
    save_evaluation(python_file_path=python_file_path, external_solutions=final_external_solutions,
                    total_time=final_total_time)
    print('End!')


def main():
    text_files_loc = read_all_files(root_directory='task_v2')
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
