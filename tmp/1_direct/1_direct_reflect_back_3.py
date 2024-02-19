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


def ask_llm(question_for_answer, init_messages):
    user_message = {"role": "user", "content": question_for_answer}
    init_messages.append(user_message)

    llm_reply = client.chat.completions.create(
        model=gpt_model,
        messages=init_messages,
        stream=False,
    )
    llm_content = llm_reply.choices[0].message.content
    print('llm_content: ', llm_content, sep="\n")
    return init_messages, llm_content

def solve_problem(task_descriptions, python_file_path, env_and_task, sol_given_parts):
    # 1. Translate natural language task descriptions (NLTD) to solutions.
    init_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": task_descriptions},
    ]
    print('task_descriptions: ', task_descriptions, sep="\n")

    request_reply = client.chat.completions.create(
        model=gpt_model,
        messages=init_messages,
        stream=False,
    )
    reply_content = request_reply.choices[0].message.content
    print('Solutions: ', reply_content, sep="\n")

    find_solution_flag = False
    for reflect_id in range(5):
        print(f'Reflection round: {reflect_id}')

        # 1. Execute the code and get the results & Put into init_messages
        external_solutions, total_time = extract_execute_code(
            problem_solving_content=reply_content, python_file_path=python_file_path)

        exec_res = f"### Python code running results: {external_solutions.stdout} {external_solutions.stderr} ###"
        assistant_message = {"role": "assistant", "content": f"{reply_content} {exec_res}"}
        init_messages.append(assistant_message)
        print('exec_res: ', exec_res, sep="\n")

        # 2. Check if the solution is correct
        question_for_answer = (
            "### Question: Is the solution meets all the requirements of task descriptions? "
            "If yes, you must only output: <**Yes**> "
            "If not, please give me a corrected version with python code. You need to provide two things. "
            "1. Analysis why the solution does not meet the requirement. "
            "2. Corrected solution with Python code. ###")
        print('question_for_answer: ', question_for_answer, sep="\n")

        init_messages, meet_req_content = ask_llm(question_for_answer=question_for_answer, init_messages=init_messages)

        if "**Yes**" in meet_req_content:
            print(f'Find the correct solution in round: {reflect_id}!')
            find_solution_flag = True
            eva_python_file_path = python_file_path[:-3] + f'_reflect_yes' + '.py'
            save_evaluation(python_file_path=eva_python_file_path, external_solutions=external_solutions,
                            total_time=total_time)
            break
        else:
            print(f'In round: {reflect_id}, the solution is not correct or optimal!')
            # assistant_message = {"role": "assistant", "content": meet_req_content}
            # init_messages.append(assistant_message)

            # Assign meet_req_content to reply_content, used for next round
            reply_content = meet_req_content

            # 3. Reflect the solution and get the feasible solution
            # q_feasible_sol = (
            #     "Is the solution a feasible solution and meets all the requirements of task descriptions except "
            #     "optimal? "
            #     "If the answer is yes, you must only output <**Feasible Yes**>. "
            #     "Otherwise, you must only output <**Feasible No**>."
            # )
            # print('q_feasible_sol: ', q_feasible_sol, sep="\n")
            #
            # init_messages, q_feasible_sol_content = ask_llm(question_for_answer=q_feasible_sol,
            #                                                 init_messages=init_messages)

            # if "Feasible Yes" in q_feasible_sol_content:
            #     find_solution_flag = True
            #     save_feasible_prex = 'yes_feasible'
            # elif "Feasible No" in q_feasible_sol_content:
            #     find_solution_flag = False
            #     save_feasible_prex = 'no_feasible'
            # else:
            #     raise ValueError(f'Something wrong in reflect_input_content!')

            eva_python_file_path = python_file_path[:-3] + f'_reflect_no' + '.py'
            save_evaluation(python_file_path=eva_python_file_path, external_solutions=external_solutions,
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
