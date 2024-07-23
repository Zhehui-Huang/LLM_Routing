import sys
import os
import argparse
import time
import pytz
from datetime import datetime

from openai import OpenAI
from utils import ask_llm, LLM_SYSTEM_PROMPT, list_files, extract_value, read_txt_file, write_py_file, run_py_file, limit_text, check_correct_in_file, extract_python_code

LA_TIMEZONE = pytz.timezone('America/Los_Angeles')

# SINGLE_TASK_LIST = ['TSP', 'BTSP', 'GTSP', 'KTSP', 'MV-TSP']
SINGLE_TASK_LIST = ['TSP']
# CITY_NUM_LIST = [10, 15, 20, 25, 50]
CITY_NUM_LIST = [10]
MAXIMUM_EXEC_TIME = 600
MAXIMUM_TEXT_LENGTH = 1000

BASE_PATH = '/Users/tencentintern/Documents/LLM_Routing/llm'

OPENAI_API_KEY = "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"


def solve_single(args):
    # TODO: Get execution time of optimal solutions provided by guangyao, the maximum exec time is less than 2x of that time.
    # Setup client
    client = OpenAI(api_key=OPENAI_API_KEY)

    path_prex = 'extra_info'
    base_task_path = f'{BASE_PATH}/task/single'
    base_solution_path = f'{BASE_PATH}/{path_prex}/solution/single'
    base_log_path = f'{BASE_PATH}/{path_prex}/log/single'
    base_verifier_path = f'{BASE_PATH}/{path_prex}/verifier/single'
    base_verifier_log_path = f'{BASE_PATH}/{path_prex}/log_verifier/single'
    base_exec_details_path = f'{BASE_PATH}/{path_prex}/exec_details/single'
    base_messages_path = f'{BASE_PATH}/{path_prex}/messages/single'
    base_constraints_path = f'{BASE_PATH}/{path_prex}/constraints/single'

    track_file_path = f'{BASE_PATH}/{path_prex}/track_single.txt'
    os.makedirs(os.path.dirname(track_file_path), exist_ok=True)
    if os.path.exists(track_file_path):
        raise FileExistsError(f"Track file already exists: {track_file_path}")
    else:
        with open(track_file_path, 'w') as file:
            file.write("Track file for single task execution.\n===\n")

    for city_num in CITY_NUM_LIST:
        for task_name in SINGLE_TASK_LIST:
            task_folder = os.path.join(base_task_path, task_name)
            file_path_list, file_name_list = list_files(directory=task_folder)
            file_path_list.sort()
            file_name_list.sort()
            # Maintain exec_detail_path
            for file_path, file_name in zip(file_path_list, file_name_list):
                # 0. Extract city number from file name
                file_city_num = extract_value(file_name=file_name)
                if int(file_city_num) != city_num:
                    continue

                print(f"Task file path: {file_path}")

                file_base_name = file_name[:-4]
                with open(track_file_path, 'a') as file:
                    file.write(f"City: {city_num}, Task: {task_name}, File: {file_base_name}\n+++\n")
                # 1. Create exec_details and messages_path file

                # 1.1 exec_details
                exec_detail_path = f'{base_exec_details_path}/{task_name}/{city_num}/exec_details_{file_name}'
                os.makedirs(os.path.dirname(exec_detail_path), exist_ok=True)

                start_time = time.time()
                cur_time = datetime.now(LA_TIMEZONE)
                print(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\tStarting ...")
                with open(exec_detail_path, 'w') as file:
                    file.write(f"Start time: [{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\n\n")
                    file.write(f"Task file path: {exec_detail_path}\n===\n")

                # 1.2 messages_path
                messages_path = f'{base_messages_path}/{task_name}/{city_num}/messages_{file_name}'
                os.makedirs(os.path.dirname(messages_path), exist_ok=True)
                with open(messages_path, 'w') as file:
                    file.write(f"Task file path: {messages_path}\n===\n")

                # 2. Load the task description
                task_description = read_txt_file(path=file_path)

                # 3. Construct the messages
                messages = [
                    {"role": "system", "content": LLM_SYSTEM_PROMPT},
                    {"role": "user", "content": task_description}
                ]
                with open(messages_path, 'a') as file:
                    file.write(f"System - LLM_SYSTEM_PROMPT\n")
                    file.write(f"User - Task description: {file_base_name}\n")

                tmp_reflect_num = 0
                tmp_log_file_path = None
                for i in range(args.reflect_num):
                    tmp_reflect_num = i
                    print(f"Reflect count: {i}")
                    with open(exec_detail_path, 'a') as file:
                        file.write(f"\nReflect count: {i}\n===\n")
                    # 3. Ask LLMs and get code
                    code_solution_content, response_time = ask_llm(client=client, llm_model=args.llm_model, messages=messages)
                    code_solution_content = extract_python_code(content=code_solution_content)

                    with open(exec_detail_path, 'a') as file:
                        file.write(f"Ask LLM for code solution, response time: {response_time:.2f} seconds.\n")

                    # 4. Save code.
                    sol_file_path = f'{base_solution_path}/{task_name}/{city_num}/{file_base_name}/solution_r{i}.py'
                    write_py_file(path=sol_file_path, content=code_solution_content)

                    # 5. Execute the code
                    log_file_path = f'{base_log_path}/{task_name}/{city_num}/{file_base_name}/log_r{i}.txt'
                    exec_status_str, execution_time, log_file_path = run_py_file(
                        code_path=sol_file_path, log_path=log_file_path, max_exec_time=MAXIMUM_EXEC_TIME
                    )
                    tmp_log_file_path = log_file_path
                    with open(exec_detail_path, 'a') as file:
                        file.write(f"Code solution execution status: {exec_status_str}, execution time: {execution_time}\n")

                    # 6 Check execution results
                    response_solution = {"role": "assistant", "content": code_solution_content}
                    messages.append(response_solution)
                    with open(messages_path, 'a') as file:
                        file.write(f"Assistant - Solution: {sol_file_path}\n")

                    if exec_status_str == 'success':
                        # 6.1 Use a verifier to verify if the solution is correct.
                        pass_verifier_value = -1
                        overall_verifier_log_file_path = ''

                        extract_constraints_prompt = (
                            'Following is the task description for a variant of the TSP (Traveling Salesman Problem) or VRP (Vehicle Routing Problem):\n'
                            '---\n'
                            f'{task_description}\n'
                            '---\n'
                            'Please extract all constraints from the given task description and list them in the following format:\n'
                            '- [Requirement 1]\n'
                            '- [Requirement 2]\n'
                            '- [Requirement 3]\n'
                            'Ensure the output contains only the list of constraints in the specified format and no additional information.'
                        )

                        extract_constraints_messages = [
                            {"role": "system", "content": LLM_SYSTEM_PROMPT},
                            {"role": "user", "content": extract_constraints_prompt}
                        ]
                        with open(messages_path, 'a') as file:
                            file.write(f"Another LLM - Extract constraints prompt\n")

                        constraints_content, response_time = ask_llm(
                            client=client, llm_model=args.llm_model, messages=extract_constraints_messages
                        )
                        with open(exec_detail_path, 'a') as file:
                            file.write(f"Ask another LLM for constraints, response time: {response_time:.2f} seconds.\n")

                        constraints_path = f'{base_constraints_path}/{task_name}/{city_num}/{file_base_name}/constraints_r{i}.txt'
                        os.makedirs(os.path.dirname(constraints_path), exist_ok=True)
                        with open(constraints_path, 'w') as file:
                            file.write(constraints_content)

                        constraints_content_response = {"role": "assistant", "content": constraints_content}
                        extract_constraints_messages.append(constraints_content_response)
                        with open(messages_path, 'a') as file:
                            file.write(f"Another LLM - Constraints response: {constraints_path}\n")

                        for vi in range(args.verify_retry_num):
                            # 6.1.1 Generate verifier prompt
                            if vi == 0:
                                log_content = read_txt_file(path=log_file_path)
                                clipped_log_content = limit_text(text=log_content, max_length=MAXIMUM_TEXT_LENGTH)
                                verifier_prompt = (
                                    'Here is the execution information:\n'
                                    f'{clipped_log_content}\n'
                                    f'If {clipped_log_content} does not contain solutions, output "FAIL".\n'
                                    'Please generate Python code to verify if the solution is correct by checking the following requirements:\n'
                                    f'{constraints_content}\n'
                                    'You may generate unit tests for each requirement. '
                                    'If the solution is correct, output "CORRECT"; otherwise, output "FAIL".'
                                )
                            else:
                                verify_log_content = read_txt_file(path=overall_verifier_log_file_path)
                                clipped_verify_log_content = limit_text(text=verify_log_content, max_length=MAXIMUM_TEXT_LENGTH)
                                verifier_prompt = (
                                    f'The generated code for verification has bugs. Here is the execution information:\n'
                                    f'{clipped_verify_log_content}\n'
                                    f'Please fix all bugs. If fixing the bugs is too complex, you may generate a new verifier.'
                                )

                            user_prompt = {"role": "user", "content": verifier_prompt}
                            extract_constraints_messages.append(user_prompt)
                            with open(messages_path, 'a') as file:
                                file.write(f"Another LLM - User - Verifier prompt.\n")

                            # 6.1.2 Ask LLMs and get verifier code
                            verifier_code_content, response_time = ask_llm(client=client, llm_model=args.llm_model, messages=extract_constraints_messages)
                            verifier_code_content = extract_python_code(content=verifier_code_content)

                            with open(exec_detail_path, 'a') as file:
                                file.write(f"Ask another LLM for verifier code, response time: {response_time:.2f} seconds.\n")

                            # 6.1.3 Save verifier code
                            verifier_file_path = f'{base_verifier_path}/{task_name}/{city_num}/{file_base_name}/verifier_r{i}_v{vi}.py'
                            write_py_file(path=verifier_file_path, content=verifier_code_content)

                            # 6.1.4 Execute verifier code
                            verifier_log_file_path = f'{base_verifier_log_path}/{task_name}/{city_num}/{file_base_name}/verifier_log_{i}_{vi}.txt'
                            verifier_exec_status_str, execution_time, verifier_log_file_path = run_py_file(
                                code_path=verifier_file_path, log_path=verifier_log_file_path,
                                max_exec_time=MAXIMUM_EXEC_TIME
                            )

                            with open(exec_detail_path, 'a') as file:
                                file.write(f"Another LLM verifier code solution execution status: {verifier_exec_status_str}, execution time: {execution_time}\n")

                            # 6.1.5 Check verifier execution results
                            if verifier_exec_status_str == 'success':
                                overall_verifier_log_file_path = verifier_log_file_path
                                verify_res_bool = check_correct_in_file(file_path=verifier_log_file_path)
                                if verify_res_bool:
                                    pass_verifier_value = 1

                                    with open(exec_detail_path, 'a') as file:
                                        file.write(f"Another LLM - pass verifier\n")
                                    break
                                else:
                                    pass_verifier_value = 0
                                    with open(exec_detail_path, 'a') as file:
                                        file.write(f"Another LLM - fail verifier\n")
                                    break
                            else:
                                overall_verifier_log_file_path = verifier_log_file_path
                                pass_verifier_value = -1
                                response_verifier = {"role": "assistant", "content": verifier_code_content}
                                extract_constraints_messages.append(response_verifier)
                                with open(messages_path, 'a') as file:
                                    file.write(f"Another LLM - Assistant - Verifier: {verifier_file_path}\n")

                        if pass_verifier_value == 1:
                            break
                        elif pass_verifier_value == 0:
                            verify_log_content = read_txt_file(path=overall_verifier_log_file_path)
                            clipped_verify_log_content = limit_text(text=verify_log_content,
                                                                    max_length=MAXIMUM_TEXT_LENGTH)

                            regenerate_prompt = (
                                f'The generated code is incorrect and does not pass the verifier. Here is the veifier execution information:\n'
                                f'{clipped_verify_log_content}\n'
                                f'Please regenerate a solution for the task, using heuristics or approximation techniques if necessary.'
                            )
                            user_prompt = {"role": "user", "content": regenerate_prompt}
                            # Here, should be messages instead of extract_constraints_messages, since I want to regenerate solutions
                            messages.append(user_prompt)
                            with open(messages_path, 'a') as file:
                                file.write(f"User - Regenerate solution generation prompt. Verifier code is okay but does not pass verifier.\n")
                            continue
                        elif pass_verifier_value == -1:
                            # Here, should be messages instead of extract_constraints_messages, since I want to regenerate solutions
                            solve_task_prompt = (
                                f'The generated code for verification has bugs and has exceeded the retry limit.\n'
                                f'We think the generated solution for the task is incorrect.\n'
                                f'Please regenerate a solution for the task, using heuristics or approximation techniques if necessary.'
                            )
                            user_prompt = {"role": "user", "content": solve_task_prompt}
                            messages.append(user_prompt)
                            with open(messages_path, 'a') as file:
                                file.write(f"User - Regenerate Solve Task Prompt: Verifier has bugs. But out of retry times, so regenerate solutions.\n")
                            continue
                        else:
                            raise ValueError(f"Unknown pass verifier value: {pass_verifier_value}")

                    # 6. Verify executing results by using verifier
                    # # 6.2 Execute error
                    # # # 6.2.1 Timeout
                    if exec_status_str == 'timeout':
                        log_content = read_txt_file(path=log_file_path)
                        clipped_log_content = limit_text(text=log_content, max_length=MAXIMUM_TEXT_LENGTH)

                        timeout_prompt = (
                            f'Here is the execution information:\n'
                            f'{clipped_log_content}\n'
                            f'The generated code exceeds the time limit of {MAXIMUM_EXEC_TIME} seconds.\n\n'
                            f'Please generate a more time-efficient method, using heuristics or approximation techniques if necessary.'
                        )
                        user_prompt = {"role": "user", "content": timeout_prompt}
                        messages.append(user_prompt)
                        with open(messages_path, 'a') as file:
                            file.write(f"User - execution timeout. Regenerate solutions.\n")
                    elif exec_status_str == 'error':
                        log_content = read_txt_file(path=log_file_path)
                        clipped_log_content = limit_text(text=log_content, max_length=MAXIMUM_TEXT_LENGTH)

                        fix_bug_prompt = (
                            f'The generated code has bugs. Here is the execution information:\n'
                            f'{clipped_log_content}\n'
                            f'Please fix all bugs. If fixing the bugs is too complex, you may generate a new solution. '
                            f'Feel free to use heuristics or approximation techniques if necessary.'
                        )
                        user_prompt = {"role": "user", "content": fix_bug_prompt}
                        messages.append(user_prompt)
                        with open(messages_path, 'a') as file:
                            file.write(f"User - ask LLM to regenerate code by fixing bugs.\n")
                    else:
                        raise ValueError(f"Unknown execution status: {exec_status_str}")

                with open(track_file_path, 'a') as file:
                    file.write(f"Reflect num: {tmp_reflect_num}\n")
                    file.write(f"Log of solution file path: {tmp_log_file_path}\n+++\n\n\n")

                end_time = time.time()
                response_time = end_time - start_time
                cur_time = datetime.now(LA_TIMEZONE)
                print(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\tFinished.\tOverall time: {response_time:.2f} seconds.")

                with open(exec_detail_path, 'a') as file:
                    file.write(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\tFinished.\n\n")
                    file.write(f"Overall time: {response_time:.2f} seconds.\n")


def solve_problem(args):
    if args.robot_num == 'single':
        solve_single(args=args)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--llm_model', type=str, default='gpt-4-turbo',
                        choices=['gpt-4-turbo-2024-04-09', 'gpt-4o-2024-05-13', 'gpt-4o-mini-2024-07-18'])
    parser.add_argument('--reflect_num', type=int, default=3, help='Default: self reflect 5 times.')
    parser.add_argument('--verify_retry_num', type=int, default=2, help='Default: self reflect 5 times.')
    parser.add_argument('--robot_num', type=str, default='single', choices=['single', 'multiple'],
                        help='Default: self reflect 5 times.')
    return parser.parse_args()


def main():
    args = get_args()
    solve_problem(args=args)


if __name__ == '__main__':
    sys.exit(main())
