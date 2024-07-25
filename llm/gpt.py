import argparse
import os
import sys

import pytz
from openai import OpenAI

from task2exec import task2exec_res
from utils import (ask_llm, LLM_SYSTEM_PROMPT, list_files, extract_value, read_txt_file, check_log_file_empty,
                   write_start_info,
                   write_end_info, CITY_NUM_LIST, SINGLE_TASK_LIST, MULTI_TASK_LIST, INSTANCE_TRY_TIMES)
from verifier import get_executable_unit_test_code

LA_TIMEZONE = pytz.timezone('America/Los_Angeles')


BASE_PATH = '/home/ethan/repository/backup/LLM_Routing/llm'
OPENAI_API_KEY = "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"


def get_results_one_try(
        args, client, file_path, file_base_name, task_name, city_num,
        base_exec_details_path, base_messages_path, base_solution_path, base_log_path, base_constraints_path,
        base_verifier_path, base_verifier_log_path, instance_tid, outer_tid, total_request_llm_num_dict,
        token_file_path):
    # 1. Write start info;
    # a) Track info: Reflect times and results path
    # b) Execution info: The process of each instance execution
    # c) Message info: How the message construct
    exec_detail_path, start_time, messages_path = write_start_info(
        file_base_name=file_base_name, base_exec_details_path=base_exec_details_path, task_name=task_name,
        city_num=city_num, base_messages_path=base_messages_path, instance_tid=instance_tid, outer_tid=outer_tid
    )

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

    # 4. Task -> Solution & Execution -> Results -> exec_status_str
    exec_status_str, llm_exec_reflect_num, tmp_log_file_path, total_request_llm_num_dict = task2exec_res(
        args=args, client=client, file_base_name=file_base_name, task_name=task_name, city_num=city_num,
        messages=messages, base_solution_path=base_solution_path, base_log_path=base_log_path,
        exec_detail_path=exec_detail_path, messages_path=messages_path, instance_tid=instance_tid, outer_tid=outer_tid,
        total_request_llm_num_dict=total_request_llm_num_dict, token_file_path=token_file_path
    )

    # 5. Check exec_status_str, exec_status_str = fail
    # Check the content in tmp_log_file_path, if it is empty, then return 'fail', 'None', 'None'
    file_empty_str = check_log_file_empty(file_path=tmp_log_file_path)
    if exec_status_str == 'fail' or file_empty_str == 'EMPTY':
        write_end_info(start_time=start_time, exec_detail_path=exec_detail_path)
        # exec_status_str, unit_test_status, unit_test_res
        return 'fail', 'None', 'None', total_request_llm_num_dict

    # 7 exec_status_str = success -> verifier
    # 7.1 Get constraints from task description
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

    # 7.2 Ask LLM for constraints -> Write down constraints
    constraints_content, response_time = ask_llm(
        client=client, llm_model=args.llm_model, messages=extract_constraints_messages,
        token_file_path=token_file_path, notes='extract_constraints'
    )
    total_request_llm_num_dict['constraints'] += 1

    constraints_path = f'{base_constraints_path}/{task_name}/{city_num}/{file_base_name}/{instance_tid}/{outer_tid}/constraints_r{llm_exec_reflect_num}.txt'
    os.makedirs(os.path.dirname(constraints_path), exist_ok=True)
    with open(constraints_path, 'w') as file:
        file.write(constraints_content)

    # 7.3 Construct constraints response
    constraints_content_response = {"role": "assistant", "content": constraints_content}
    extract_constraints_messages.append(constraints_content_response)

    # 7.4 Maintain messages_path, exec_detail_path
    with open(exec_detail_path, 'a') as file:
        file.write(f"Another LLM - Get constraints from LLM, response time: {response_time:.2f} seconds.\n")
    with open(messages_path, 'a') as file:
        file.write(f"Another LLM - User - Ask for prompts\n")
        file.write(f"Another LLM - Assistant - Constraints response: {constraints_path}\n")

    unit_test_status, unit_test_res, total_request_llm_num_dict = get_executable_unit_test_code(
        args=args, client=client, extract_constraints_messages=extract_constraints_messages,
        task_name=task_name, city_num=city_num, file_base_name=file_base_name,
        llm_exec_reflect_num=llm_exec_reflect_num, base_verifier_log_path=base_verifier_log_path,
        base_verifier_path=base_verifier_path, exec_detail_path=exec_detail_path,
        log_file_path=tmp_log_file_path, constraints_content=constraints_content,
        messages_path=messages_path, instance_tid=instance_tid, outer_tid=outer_tid,
        total_request_llm_num_dict=total_request_llm_num_dict, token_file_path=token_file_path
    )

    if unit_test_status == 'success':
        if unit_test_res == 'CORRECT':
            # return exec_status_str, unit_test_status, unit_test_res
            return 'success', 'success', 'CORRECT', total_request_llm_num_dict
        elif unit_test_res == 'FAIL':
            # return exec_status_str, unit_test_status, unit_test_res
            return 'success', 'success', 'FAIL', total_request_llm_num_dict
        elif unit_test_res == 'None':
            # return exec_status_str, unit_test_status, unit_test_res
            return 'success', 'success', 'None', total_request_llm_num_dict
    elif unit_test_status == 'fail':
        # return exec_status_str, unit_test_status, unit_test_res
        return 'success', 'fail', 'not_executed', total_request_llm_num_dict
    else:
        raise ValueError(f"Unknown unit test status: {unit_test_status}")


def solve_batch(args):
    # TODO: Get execution time of optimal solutions provided by guangyao, the maximum exec time is less than 2x of that time.
    # Setup client
    client = OpenAI(api_key=OPENAI_API_KEY)

    path_prex = 'extra_info'
    base_task_path = f'{BASE_PATH}/task/zero/{args.robot_num}/'

    # LLM executor
    base_solution_path = f'{BASE_PATH}/{path_prex}/solution/{args.robot_num}'
    base_log_path = f'{BASE_PATH}/{path_prex}/log/{args.robot_num}'
    base_exec_details_path = f'{BASE_PATH}/{path_prex}/exec_details/{args.robot_num}'
    base_messages_path = f'{BASE_PATH}/{path_prex}/messages/{args.robot_num}'

    # LLM verifier
    base_constraints_path = f'{BASE_PATH}/{path_prex}/constraints/{args.robot_num}'
    base_verifier_path = f'{BASE_PATH}/{path_prex}/verifier/{args.robot_num}'
    base_verifier_log_path = f'{BASE_PATH}/{path_prex}/log_verifier/{args.robot_num}'

    base_track_file_path = f'{BASE_PATH}/{path_prex}/track/{args.robot_num}'
    base_token_file_path = f'{BASE_PATH}/{path_prex}/token/{args.robot_num}'

    for city_num in CITY_NUM_LIST:

        if args.robot_num == 'single':
            cur_task_list = SINGLE_TASK_LIST
        elif args.robot_num == 'multiple':
            cur_task_list = MULTI_TASK_LIST
        else:
            raise ValueError(f"Unknown robot_num: {args.robot_num}")

        for task_name in cur_task_list:
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

                # 1. Instance try 5 times
                for instance_tid in range(INSTANCE_TRY_TIMES):
                    final_success_bool = False
                    track_file_path = f'{base_track_file_path}/{task_name}/{city_num}/{file_base_name}/{instance_tid}/track.txt'
                    if os.path.exists(track_file_path):
                        print(f'File exists {track_file_path}\n')
                        continue

                    os.makedirs(os.path.dirname(track_file_path), exist_ok=True)
                    # Create track file
                    with open(track_file_path, 'w') as file:
                        file.write(f"Task: {task_name}, City: {city_num}, File name: {file_base_name}, Run time: {instance_tid}\n\n")

                    total_request_llm_num_dict = {
                        'exec': 0,
                        'verifier': 0,
                        'constraints': 0,
                    }
                    for outer_tid in range(args.reflect_num):
                        token_file_path = f'{base_token_file_path}/{task_name}/{city_num}/{file_base_name}/{instance_tid}/{outer_tid}/token_details.txt'
                        os.makedirs(os.path.dirname(token_file_path), exist_ok=True)
                        with open(token_file_path, 'w') as file:
                            file.write(f"Task: {task_name}, City: {city_num}, File name: {file_base_name}, Run time: {instance_tid}, Try id: {outer_tid}\n\n")

                        exec_status_str, unit_test_status, unit_test_res, total_request_llm_num_dict = get_results_one_try(
                            args=args, client=client, file_path=file_path, file_base_name=file_base_name,
                            task_name=task_name, city_num=city_num,
                            base_exec_details_path=base_exec_details_path, base_messages_path=base_messages_path,
                            base_solution_path=base_solution_path, base_log_path=base_log_path,
                            base_constraints_path=base_constraints_path, base_verifier_path=base_verifier_path,
                            base_verifier_log_path=base_verifier_log_path, instance_tid=instance_tid,
                            outer_tid=outer_tid, total_request_llm_num_dict=total_request_llm_num_dict,
                            token_file_path=token_file_path
                        )
                        if exec_status_str == 'success' and unit_test_status == 'success' and unit_test_res == 'CORRECT':
                            final_success_bool = True
                            break

                    total_llm_rnum = sum(total_request_llm_num_dict.values())
                    total_llm_rnum_str = ', '.join(f"'{key}': {value}" for key, value in total_request_llm_num_dict.items())

                    if final_success_bool:
                        with open(track_file_path, 'a') as file:
                            file.write(f"Success: Request LLM number: {total_llm_rnum}\n")
                            file.write(f"Details: {total_llm_rnum_str}\n\n\n")
                    else:
                        with open(track_file_path, 'a') as file:
                            file.write(f"Fail: Request LLM number: {total_llm_rnum}\n")
                            file.write(f"Details: {total_llm_rnum_str}\n\n\n")


def solve_problem(args):
    solve_batch(args=args)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--llm_model', type=str, default='gpt-4-turbo',
                        choices=['gpt-4-turbo-2024-04-09', 'gpt-4o-2024-05-13', 'gpt-4o-mini-2024-07-18'])
    parser.add_argument('--reflect_num', type=int, default=3, help='Default: total 3, self reflect 2 times.')
    parser.add_argument('--robot_num', type=str, default='single', choices=['single', 'multiple'],
                        help='Default: single')
    return parser.parse_args()


def main():
    args = get_args()
    solve_problem(args=args)


if __name__ == '__main__':
    sys.exit(main())
