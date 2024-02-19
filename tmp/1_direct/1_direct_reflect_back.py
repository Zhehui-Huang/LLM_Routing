import copy
import sys
import os
import re

from openai import OpenAI

from utils import (extract_execute_code, read_file, gpt_prompt_tips, read_all_files, extract_analysis_before_python,
                   save_evaluation)

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
    find_solution_flag = False
    analysis_content = ""
    init_reflect_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": task_descriptions},
    ]

    for reflect_id in range(5):
        print(f'Reflection round: {reflect_id}')
        external_solutions, total_time = extract_execute_code(
            problem_solving_content=problem_solving_content, python_file_path=python_file_path)
        if external_solutions.stderr == "":
            tmp_solution = external_solutions.stdout
        else:
            tmp_solution = (f"Since this solution has errors, you do not need to fix these error, just give a new "
                            f"solution. Some information related to the solution: "
                            f"{external_solutions.stdout} {external_solutions.stderr}")

        if reflect_id == 0:
            tmp_solution = f"### Here is the solution: {tmp_solution} ###"
        else:
            tmp_solution = (f"### Here is analysis of the previous solution: {analysis_content} ### "
                            f"### Here is the corrected solution: {tmp_solution} ###")

        tmp_solution_message = {"role": "assistant", "content": tmp_solution}
        init_reflect_messages.append(tmp_solution_message)

        tmp_modified_solution = f"### Here is the solution: {tmp_solution} ###"
        env_and_task_description = f"'''Following are natural language task descriptions: {env_and_task} '''"
        question_for_answer = (
            "### Question: Is the solution meets the task descriptions requirements? "
            "If yes, you must only output: <**Yes**> "
            "If not, please give me a corrected version with python code. You need to provide two things. "
            "1. Analysis why the solution does not meet the requirement. "
            "2. Corrected solution with Python code. ###")
        reflect_input = f"{env_and_task_description} {tmp_modified_solution} {question_for_answer}"

        reflect_input_message = {"role": "user", "content": reflect_input}
        init_reflect_messages.append(reflect_input_message)

        reflect_input_reply = client.chat.completions.create(
            model=gpt_model,
            messages=init_reflect_messages,
            stream=False,
        )

        reflect_input_content = reflect_input_reply.choices[0].message.content

        # Feasible question
        feasible_question_for_answer = (
            "Is the solution meets all the task descriptions requirements except optimal solution if the task "
            "descriptions asked for optimal solution?"
            "Specifically, the solution meets all the task descriptions requirements, and it just not optimal. "
            "If the answer is yes, you must only output <**Feasible Yes**>. Otherwise, you must only output "
            "<**Feasible No**>")
        copy_reflect_input = f"{env_and_task_description} {tmp_modified_solution} {feasible_question_for_answer}"

        feasible_solution_reply = client.chat.completions.create(
            model=gpt_model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": copy_reflect_input}
            ],
            stream=False,
        )
        feasible_solution_content = feasible_solution_reply.choices[0].message.content

        if "**Yes**" in reflect_input_content:
            print(f'Find the correct solution in round: {reflect_id}!')
            find_solution_flag = True

            print('reflect_input_content: ', reflect_input_content, sep="\n")
            python_file_path = python_file_path[:-3] + f'_reflect_yes_feasible' + '.py'
            save_evaluation(python_file_path=python_file_path, external_solutions=external_solutions,
                            total_time=total_time)
            break
        else:
            print('feasible_solution_content: ', feasible_solution_content, sep="\n")
            if "Feasible Yes" in feasible_solution_content:
                find_solution_flag = True
                save_feasible_prex = 'yes_feasible'
            elif "Feasible No" in feasible_solution_content:
                find_solution_flag = False
                save_feasible_prex = 'no_feasible'
            else:
                raise ValueError(f'Something wrong in reflect_input_content!')

            print(f'In round: {reflect_id}, the solution is not correct or optimal!')

            # Extract the analysis from reflect_input_content
            # analysis_content = extract_analysis_before_python(reflect_input_content=reflect_input_content)
            analysis_content = reflect_input_content
            problem_solving_content = reflect_input_content
            print('reflect_input_content: ', reflect_input_content, sep="\n")
            python_file_path = python_file_path[:-3] + f'_reflect_{save_feasible_prex}' + '.py'

            save_evaluation(python_file_path=python_file_path, external_solutions=external_solutions,
                            total_time=total_time)

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
