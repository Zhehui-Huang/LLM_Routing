import copy
import os
import sys

import google.generativeai as genai
from openai import OpenAI

from task_specify_sol_req import sol_req
from utils import (extract_execute_code, read_file, nltd_to_math_requirements, gpt_prompt_tips, read_all_files,
                   save_evaluation, nltd_to_math)

# OpenAI
client = OpenAI()
gpt_model = "gpt-4-0125-preview"

# Gemini
GOOGLE_API_KEY = "AIzaSyBruy7vdcDDCHfIrNxgiYkBhAl7g2ajXGA"
genai.configure(api_key=GOOGLE_API_KEY)

# Solution path
sol_path = 'solution/5_external_tools_no_consistent_check_v2'

consistent_check_count = 2
refine_count = 3


def solve_problem(task_descriptions, python_file_path, sol_given_parts):
    math_content_modify = nltd_to_math(client=client, gpt_model=gpt_model, task_descriptions=task_descriptions)

    # Ask recommended solvers
    tmp_recommend_solver = (
        f"Please provide the best tool (such as Gurobi, OR-Tools, etc.) that you want to use to solve the "
        f"the following mathematical formulations. "
        f"You must only output the tool name. {math_content_modify}. "
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

    # 3. Math to solution
    problem_solving_questions = (
        f"You must use Python code and {recommend_solver_content} to solve the above mathematical "
        f"formulations. You must consider all constrains regardless of complexity. {sol_given_parts}"
    )
    print('problem_solving_questions:', problem_solving_questions, sep='\n')

    init_messages = [
        {"role": "system", "content": f"You are a helpful assistant. {gpt_prompt_tips}"},
        {"role": "user", "content": task_descriptions},
        {"role": "assistant", "content": math_content_modify},
        {"role": "user", "content": problem_solving_questions}
    ]

    pre_external_solutions = None
    final_external_solutions = None
    final_total_time = None
    for count in range(refine_count):
        solution_reply = client.chat.completions.create(
            model=gpt_model,
            messages=init_messages,
            stream=False,
        )
        solution_content = solution_reply.choices[0].message.content
        external_solutions, total_time = extract_execute_code(
            problem_solving_content=solution_content, python_file_path=python_file_path)

        # From assistant
        tmp_assistant_content = (
            f"### Solution: {solution_content} ### "
            f"### Execution results: {external_solutions.stdout} {external_solutions.stderr} ###"
        )
        tmp_assistant_message = {"role": "assistant", "content": tmp_assistant_content}
        init_messages.append(tmp_assistant_message)
        print('Solutions: ', tmp_assistant_content, sep='\n')

        # From user
        tmp_user_content = (
            f"Please provide a better solution with Python code and {recommend_solver_content}. "
            f"If previous solution has errors, "
            f"please fix all errors. You must consider all constrains regardless of complexity. {sol_given_parts}"
        )
        tmp_user_message = {"role": "user", "content": tmp_user_content}
        init_messages.append(tmp_user_message)
        print('User: ', tmp_user_content, sep='\n')

        if count == 0:
            pre_external_solutions = copy.deepcopy(external_solutions)

            # Update final solution
            final_external_solutions = copy.deepcopy(external_solutions)
            final_total_time = total_time
        else:
            tmp_refine_question = (
                f"Question: Based on the mathematical formulations and solution requirements below, "
                f"is the current solution better than the previous one? "
                f"!!! You MUST ONLY EXACTLY OUTPUT <**Yes**> or <**No**> !!! "
                f"### Mathematical formulations: {math_content_modify} ### "
                f"### Solution requirements: {sol_given_parts} ### "
                f"### Previous solution: {pre_external_solutions.stdout} {pre_external_solutions.stderr} ### "
                f"### Current solution: {external_solutions.stdout} {external_solutions.stderr} ### ")
            print('tmp_refine_question:', tmp_refine_question, sep='\n')

            tmp_refine_messages = [
                {"role": "system", "content": f"You are a helpful assistant. {gpt_prompt_tips}"},
                {"role": "user", "content": tmp_refine_question},
            ]
            tmp_refine_ans_reply = client.chat.completions.create(
                model=gpt_model,
                messages=tmp_refine_messages,
                stream=False,
            )
            tmp_refine_ans_content = tmp_refine_ans_reply.choices[0].message.content
            if 'Yes' in tmp_refine_ans_content:
                print(f'Better than the previous one! {tmp_refine_ans_content}')
                pre_external_solutions = copy.deepcopy(external_solutions)

                # Update final solution
                final_external_solutions = copy.deepcopy(external_solutions)
                final_total_time = total_time
                # Save evaluation
                save_evaluation(python_file_path=python_file_path, external_solutions=external_solutions,
                                total_time=total_time)
                continue
            else:
                print(f'NOT better than the previous one! {tmp_refine_ans_content}')
                # Save evaluation
                save_evaluation(python_file_path=python_file_path, external_solutions=external_solutions,
                                total_time=total_time)
                continue

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
                          sol_given_parts=sol_given_parts)


if __name__ == '__main__':
    sys.exit(main())
