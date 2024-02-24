import sys
import os

from openai import OpenAI

from task_specify_sol_req import sol_req
from utils import (read_file, gpt_prompt_tips, read_all_files, reflect_solution, extract_execute_code,
                   save_evaluation, get_constraints)

client = OpenAI()
gpt_model = "gpt-4-0125-preview"
sol_path = 'solution/1_direct_reflect'

reflect_num = 3


def solve_problem(task_descriptions, python_file_path, env_and_task, sol_given_parts):
    # 1. Translate natural language task descriptions (NLTD) to solutions.
    print('task_descriptions: ', task_descriptions, sep="\n")

    request_reply = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": f"You are a helpful assistant. {gpt_prompt_tips}"},
            {"role": "user", "content": task_descriptions},
        ],
        stream=False,
    )
    reply_content = request_reply.choices[0].message.content
    print('reply_content:', reply_content, sep='\n')

    external_solutions, total_time = extract_execute_code(
        problem_solving_content=reply_content, python_file_path=python_file_path)

    constraints_content = get_constraints(env_and_task)

    question_for_answer = (
        "### \nQuestion: \nPlease use Python code to check if the above solution is correct and satisfies the "
        f"constraints: \n{constraints_content}\n"
        "If the solution is correct, you need to output exactly <** YES!!! **>. \n"
        "If the solution is not correct, you need to output why the solution is wrong, at least give some hints. ###"
    )

    extra_eval_content = 'This is without reflect!'
    save_evaluation(python_file_path=python_file_path, external_solutions=external_solutions,
                    total_time=total_time, extra_eval_content=extra_eval_content,
                    reflect_id=0)

    final_external_solutions, final_total_time, find_solution_flag, extra_eval_content = reflect_solution(
        ori_python_file_path=python_file_path, math_content_modify=None, client=client, gpt_model=gpt_model,
        reflect_num=reflect_num, question_for_answer=question_for_answer, external_solutions=external_solutions,
        total_time=total_time, env_and_task=env_and_task, sol_given_parts=sol_given_parts
    )

    if find_solution_flag is False:
        print(f'Can not find the solution!')

    print('End!')


def main():
    text_files_loc = read_all_files(root_directory='task_v3/4-tsp')
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
            if int(parts[1][0]) > 1:
                robot_num = 'M'
            sol_given_parts_key = f"{parts[2][0]}_{robot_num}"
            sol_given_parts = sol_req[sol_given_parts_key]
            task_descriptions = f"{env_and_task} {sol_given_parts}"

            solve_problem(task_descriptions=task_descriptions, python_file_path=python_file_path,
                          env_and_task=env_and_task, sol_given_parts=sol_given_parts)


if __name__ == '__main__':
    sys.exit(main())
