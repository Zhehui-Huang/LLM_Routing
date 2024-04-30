import sys
import os
import argparse

from openai import OpenAI

from gpt_utils import ask_gpt, nl_to_math_to_sol
from task_specify_sol_req import sol_req_dict
from utils import read_file, read_all_files, reflect_solution, extract_execute_code, save_evaluation, save_math_form


def solve_problem(python_file_path, env_and_task, sol_req, args):
    # Restart OpenAI
    client = OpenAI()
    # Translate natural language task descriptions (NLTD) to solutions.
    if args.prompt_paradigm in ['nl_to_sol', 'nl_to_sol_tool']: #TODO: Support nl_to_sol_tool
        task_descriptions = f"{env_and_task} {sol_req}"
        sol_content = ask_gpt(questions=task_descriptions, client=client, args=args)
    elif args.prompt_paradigm in ['nl_to_math_to_sol', 'nl_to_math_to_sol_tool']: #TODO: Support nl_to_math_to_sol_tool
        sol_content, math_content = nl_to_math_to_sol(env_and_task=env_and_task, client=client, args=args, sol_req=sol_req)
        save_math_form(python_file_path, math_content)
    else:
        raise NotImplementedError(f'args.prompt_paradigm: {args.prompt_paradigm} is not implemented!')

    external_solutions, total_time = extract_execute_code(
        problem_solving_content=sol_content, python_file_path=python_file_path, reflect_id=0)
    extra_eval_content = 'This is without reflect!'
    save_evaluation(python_file_path=python_file_path, external_solutions=external_solutions,
                    total_time=total_time, extra_eval_content=extra_eval_content, reflect_id=0)

    # Get constraints from the task descriptions.
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

    final_external_solutions, final_total_time, find_solution_flag, extra_eval_content = reflect_solution(
        ori_python_file_path=python_file_path, math_content_modify=None, client=client, gpt_model=args.gpt_model,
        reflect_num=args.reflect_num, question_for_answer=question_for_answer, external_solutions=external_solutions,
        total_time=total_time, env_and_task=env_and_task, sol_given_parts=sol_given_parts, external_solver=False,
        external_tool_name="", reply_content=sol_content
    )

    if find_solution_flag is False:
        print(f'Can not find the solution!')

    print('End!')


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', type=str, default='task_detail',
                        choices=['task_detail', 'task_concise'])
    parser.add_argument('--gpt_model', type=str, default='gpt-4-0125-preview')
    parser.add_argument('--prompt_paradigm', type=str, default='nl_to_sol',
                        choices=['nl_to_sol', 'nl_to_math_to_sol', 'nl_to_sol_tool', 'nl_to_math_to_sol_tool'],
                        help='nl_to_sol: natural language to solution through code; '
                             'nl_to_math_to_sol: natural language to math first, then to solution through code; '
                             'nl_to_sol_tool: natural language to solution through code with external solvers; '
                             'nl_to_math_to_sol_tool: natural language to math first, then to solution through '
                             'code with external solvers '
                        )
    parser.add_argument('--evaluate_num', type=int, default=10,
                        help='Default: Evaluate the solution for the same task 10 times.')
    parser.add_argument('--reflect_num', type=int, default=6,
                        help='Default: self reflect 6 times.')

    return parser.parse_args()


def main():
    args = get_args()
    text_files_loc = read_all_files(root_directory=args.task)
    sol_path = f'solution/{args.gpt_model}/{args.prompt_paradigm}'
    for file_path in text_files_loc:
        for tid in range(args.evaluate_num):
            python_file_path = os.path.join(sol_path, file_path[:-4] + f'_{tid}' + '.py')
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
            # Get solution requirements
            sol_req_key = f"{parts[2][0]}_{robot_num}"
            sol_req = sol_req_dict[sol_req_key]

            solve_problem(python_file_path=python_file_path, env_and_task=env_and_task, sol_req=sol_req, args=args)


if __name__ == '__main__':
    sys.exit(main())
