import sys
import os

from openai import OpenAI
import google.generativeai as genai

from ambiguties_utils import overall_clear_check
from task_specify_sol_req import sol_req
from utils import (read_file, gpt_prompt_tips, read_all_files, reflect_solution, extract_execute_code,
                   save_evaluation, gemini_prompt_tips)

client = OpenAI()
gpt_model = "gpt-4-0125-preview"

GOOGLE_API_KEY = "AIzaSyBruy7vdcDDCHfIrNxgiYkBhAl7g2ajXGA"
genai.configure(api_key=GOOGLE_API_KEY)

sol_path = 'solution/3_user_direct_reflect_ambiguities'

reflect_num = 6


def solve_problem(task_descriptions, python_file_path, env_and_task, sol_given_parts):
    # 1. Translate natural language task descriptions (NLTD) to solutions.
    print('task_descriptions: ', task_descriptions, sep="\n")
    use_gemini = False
    task_descriptions, real_check_id = overall_clear_check(
        check_count=3, client=client, gpt_model=gpt_model, env_and_task=env_and_task,
        gpt_prompt_tips=gpt_prompt_tips, gemini_prompt_tips=gemini_prompt_tips, use_gemini=use_gemini
    )

    request_reply = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": f"You are a helpful assistant. {gpt_prompt_tips}"},
            {"role": "user", "content": f'{task_descriptions} \n{sol_given_parts}'},
        ],
        stream=False,
    )
    reply_content = request_reply.choices[0].message.content
    print('reply_content:', reply_content, sep='\n')

    external_solutions, total_time = extract_execute_code(
        problem_solving_content=reply_content, python_file_path=python_file_path)

    # constraints_content = get_constraints(env_and_task)
    get_constraints_reply = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": f"You are a helpful assistant. {gpt_prompt_tips}"},
            {"role": "user", "content": f'Please extract all constraints from the task descriptions: {env_and_task}. '
                                        f'For example, the constraints can be like: Each city must be visited exactly'
                                        f' once.'},
        ],
        stream=False,
    )
    constraints_content = get_constraints_reply.choices[0].message.content
    print('constraints_content:', constraints_content, sep='\n')

    question_for_answer = (
        "### \nQuestion: \nPlease use Python code to check if the solution satisfies all of following "
        f"constraints one by one: \n{constraints_content}\n"
        "If the solution is correct, you need to output exactly <** YES!!! **>. \n"
        "If the solution is not correct, you need to use Python code to print all violated constraints."
        "You need to combine all the constraints together. You should print the exact violated constraints. "
        "You should not only output the index of the constraints. \n"
        "For example, if the constraint, each city must be visited exactly once by one of the robots, "
        "is violated, and you found that city 1 is not visited. Besides, you found travel cost calculation is wrong. \n"
        "In the python code, you need to combine both of them and print them out. \n###"
    )

    extra_eval_content = 'This is without reflect!'
    save_evaluation(python_file_path=python_file_path, external_solutions=external_solutions,
                    total_time=total_time, extra_eval_content=extra_eval_content,
                    reflect_id=0)

    final_external_solutions, final_total_time, find_solution_flag, extra_eval_content = reflect_solution(
        ori_python_file_path=python_file_path, math_content_modify=None, client=client, gpt_model=gpt_model,
        reflect_num=reflect_num, question_for_answer=question_for_answer, external_solutions=external_solutions,
        total_time=total_time, env_and_task=env_and_task, sol_given_parts=sol_given_parts, reply_content=reply_content
    )

    if find_solution_flag is False:
        print(f'Can not find the solution!')

    print('End!')


def main():
    text_files_loc = read_all_files(root_directory='task_v3_ambiguities/4-tsp/K-CTSP')
    text_files_loc = [text_files_loc[0]]
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
                          env_and_task=env_and_task, sol_given_parts=sol_given_parts)


if __name__ == '__main__':
    sys.exit(main())