import sys
import os
import argparse

from openai import OpenAI

from gpt_utils import ask_gpt
from task_specify_sol_req import sol_req
from utils import read_file, read_all_files, reflect_solution, extract_execute_code, save_evaluation


def solve_problem(task_descriptions, python_file_path, env_and_task, sol_given_parts, args):
    # Restart OpenAI
    client = OpenAI()
    # 1. Translate natural language task descriptions (NLTD) to solutions.
    sol_content = ask_gpt(questions=task_descriptions, client=client, args=args)

    external_solutions, total_time = extract_execute_code(
        problem_solving_content=sol_content, python_file_path=python_file_path, reflect_id=0)

    # 2. Get constraints from the task descriptions.
    # constraints_content_test = get_constraints(env_and_task)
    get_constraints_prompt = (f'Please extract all constraints from the task descriptions: {env_and_task}. '
                              f'The example of constraints: Each city must be visited exactly one.')

    constraints_content = ask_gpt(questions=get_constraints_prompt, client=client, args=args)

    question_for_answer = (
        "### \nQuestion: \nPlease use Python code to check if the solution satisfies all following "
        f"constraints one by one: \n{constraints_content}\n"
        "If the solution is correct, you should exactly output <** YES!!! **> \n"
        "If the solution is not correct, you should use Python code to print all violated constraints.\n###"
    )

    extra_eval_content = 'This is without reflect!'
    save_evaluation(python_file_path=python_file_path, external_solutions=external_solutions,
                    total_time=total_time, extra_eval_content=extra_eval_content, reflect_id=0)

    final_external_solutions, final_total_time, find_solution_flag, extra_eval_content = reflect_solution(
        ori_python_file_path=python_file_path, math_content_modify=None, client=client, gpt_model=args.gpt_model,
        reflect_num=args.reflect_num, question_for_answer=question_for_answer, external_solutions=external_solutions,
        total_time=total_time, env_and_task=env_and_task, sol_given_parts=sol_given_parts, external_solver=False,
        external_tool_name="", reply_content=sol_content
    )

    if find_solution_flag is False:
        print(f'Can not find the solution!')

    print('End!')


def get_hyperparameters():
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', type=str, default='task_detail')
    parser.add_argument('--gpt_model', type=str, default='gpt-4-0125-preview')
    parser.add_argument('--sol_path', type=str, default='solution/gpt4_direct')
    parser.add_argument('--evaluate_num', type=int, default=10,
                        help='Default: Evaluate the solution for the same task 10 times.')
    parser.add_argument('--reflect_num', type=int, default=6,
                        help='Default: self reflect 6 times.')

    return parser.parse_args()


def main():
    args = get_hyperparameters()
    text_files_loc = read_all_files(root_directory=args.task)
    for file_path in text_files_loc:
        for tid in range(args.evaluate_num):
            python_file_path = os.path.join(args.sol_path, file_path[:-4] + f'_{tid}' + '.py')
            directory = os.path.dirname(python_file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)

            if os.path.exists(python_file_path):
                print('python_file_path exists:', python_file_path, sep='\n')
                continue

            parts = file_path.split('/')
            if int(parts[1][0]) == 1:
                robot_num = '1'
            else:
                robot_num = 'M'

            # Get info
            env_and_task = read_file(file_path=file_path)

            sol_given_parts_key = f"{parts[2][0]}_{robot_num}"
            sol_given_parts = sol_req[sol_given_parts_key]
            task_descriptions = f"{env_and_task} {sol_given_parts}"

            solve_problem(task_descriptions=task_descriptions, python_file_path=python_file_path,
                          env_and_task=env_and_task, sol_given_parts=sol_given_parts, args=args)


if __name__ == '__main__':
    sys.exit(main())
