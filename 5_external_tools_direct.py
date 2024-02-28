import copy
import os
import sys

import google.generativeai as genai
from openai import OpenAI

from task_specify_sol_req import sol_req
from utils import (extract_execute_code, read_file, nltd_to_math_requirements, gpt_prompt_tips, read_all_files,
                   save_evaluation, nltd_to_math, get_constraints, reflect_solution)

# OpenAI
client = OpenAI()
gpt_model = "gpt-4-0125-preview"

# Gemini
GOOGLE_API_KEY = "AIzaSyBruy7vdcDDCHfIrNxgiYkBhAl7g2ajXGA"
genai.configure(api_key=GOOGLE_API_KEY)

# Solution path
sol_path = 'solution/5_external_tools_direct_fix_bug'

reflect_num = 6


def solve_problem(task_descriptions, python_file_path, sol_given_parts, env_and_task):
    # Ask recommended solvers
    tmp_recommend_solver = (
        f"Please pick the best tool (such as Gurobi, OR-Tools, etc.) that you want to use to solve the "
        f"task: \n{env_and_task} \nYou must only output the tool name. \n"
    )
    ask_recommend_solver_messages = [
        {"role": "system", "content": f"You are a helpful assistant. {gpt_prompt_tips}"},
        {"role": "user", "content": tmp_recommend_solver},
    ]
    recommend_solver_reply = client.chat.completions.create(
        model=gpt_model,
        messages=ask_recommend_solver_messages,
        stream=False,
    )
    recommend_solver_content = recommend_solver_reply.choices[0].message.content
    print('recommend_solver_content:', recommend_solver_content, sep='\n')

    # 3. NLTD to solution
    problem_solving_questions = (
        f"You must use Python code and {recommend_solver_content} to solve the task: \n{env_and_task}. \n"
        f"You must consider all constrains regardless of complexity. \n"
        f"{sol_given_parts}"
    )
    print('problem_solving_questions:', problem_solving_questions, sep='\n')

    solution_reply = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": f"You are a helpful assistant. {gpt_prompt_tips}"},
            {"role": "user", "content": problem_solving_questions}
        ],
        stream=False,
    )
    solution_content = solution_reply.choices[0].message.content
    external_solutions, total_time = extract_execute_code(
        problem_solving_content=solution_content, python_file_path=python_file_path)

    constraints_content = get_constraints(env_and_task)

    question_for_answer = (
        "### \nQuestion: \nPlease use Python code to check if the solution satisfies all of following "
        f"constraints one by one: \n{constraints_content}\n"
        "If the solution is correct, you need to output exactly <** YES!!! **>. \n"
        "If the solution is not correct, you need to use Python code to print all violated constraints."
        "You need to combine all the constraints together. You should print the exact violated constraints. "
        "You should not only output the index of the constraints. \n"
        "For example, if the constraint, each city must be visited exactly once by one of the robots, "
        "is violated, and you found that city 1 is not visited. Besides, you found travel cost calculation is wrong. \n"
        "In the python code, you need to combine both of them and print them out. \n"
        "###"
    )

    extra_eval_content = 'This is without reflect!'
    save_evaluation(python_file_path=python_file_path, external_solutions=external_solutions,
                    total_time=total_time, extra_eval_content=extra_eval_content, reflect_id=0)

    final_external_solutions, final_total_time, find_solution_flag, extra_eval_content = reflect_solution(
        ori_python_file_path=python_file_path, math_content_modify=None, client=client,
        gpt_model=gpt_model, reflect_num=reflect_num, question_for_answer=question_for_answer,
        external_solutions=external_solutions, total_time=total_time, env_and_task=env_and_task,
        sol_given_parts=sol_given_parts, external_solver=True, external_tool_name=recommend_solver_content,
        reply_content=solution_content
    )

    if find_solution_flag is False:
        print(f'Can not find the solution!')

    print('End!')


def main():
    text_files_loc = read_all_files(root_directory='task_v3')
    print('file number:', len(text_files_loc), sep='\n')
    for file_path in text_files_loc:
        for tid in range(10):
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
            task_descriptions = f"{env_and_task} {sol_given_parts}"

            solve_problem(task_descriptions=task_descriptions, python_file_path=python_file_path,
                          sol_given_parts=sol_given_parts, env_and_task=env_and_task)


if __name__ == '__main__':
    sys.exit(main())
