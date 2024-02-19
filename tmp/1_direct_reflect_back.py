import sys
import os

from openai import OpenAI

from utils import (extract_execute_code, read_file, gpt_prompt_tips, read_all_files, save_evaluation)

from task_specify_sol_req import sol_req

client = OpenAI()
gpt_model = "gpt-4-0125-preview"
sol_path = 'solution/1_direct_reflect'


def solve_problem(task_descriptions, python_file_path, env_and_task, sol_given_parts):
    ori_python_file_path = python_file_path
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

    find_solution_flag = False
    for reflect_id in range(1):
        print(f'Reflection round: {reflect_id}')

        # 1. Execute the code and get the results
        python_file_path = ori_python_file_path[:-3] + f'_{reflect_id}' + '.py'
        external_solutions, total_time = extract_execute_code(
            problem_solving_content=reply_content, python_file_path=python_file_path)

        exec_res = f"### Here is the solution: {external_solutions.stdout} {external_solutions.stderr} ###"
        print('exec_res: ', exec_res, sep="\n")

        # 2. Check if the solution is correct
        question_for_answer = (
            "### Question: Is the solution meets all the requirements of task descriptions? "
            "If yes, you must only output: <**Yes**> "
            "If not, please provide a correct version with python code. ###")

        q_meet_req = f"{env_and_task} {exec_res} {question_for_answer} {sol_given_parts}"
        print('q_meet_req: ', q_meet_req, sep="\n")

        q_meet_req_messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": q_meet_req},
        ]
        q_meet_req_reply = client.chat.completions.create(
            model=gpt_model,
            messages=q_meet_req_messages,
            stream=False,
        )
        q_meet_req_content = q_meet_req_reply.choices[0].message.content
        print('q_meet_req_content: ', q_meet_req_content, sep="\n")

        if "**Yes**" in q_meet_req_content:
            print(f'Find the correct solution in round: {reflect_id}!')
            find_solution_flag = True
            eva_python_file_path = python_file_path[:-3] + f'_reflect_yes' + '.py'
            save_evaluation(python_file_path=eva_python_file_path, external_solutions=external_solutions,
                            total_time=total_time)
            break
        else:
            print(f'In round: {reflect_id}, the solution is not correct or optimal!')
            # Assign meet_req_content to reply_content, used for next round
            reply_content = q_meet_req_content
            eva_python_file_path = python_file_path[:-3] + f'_reflect_no_{reflect_id}' + '.py'
            save_evaluation(python_file_path=eva_python_file_path, external_solutions=external_solutions,
                            total_time=total_time)

    if find_solution_flag is False:
        print(f'Can not find the solution!')

    print('End!')


def main():
    text_files_loc = read_all_files(root_directory='task')
    print('file number:', len(text_files_loc), sep='\n')
    for file_path in text_files_loc:
        for tid in range(3):
            env_and_task = read_file(file_path=file_path)
            python_file_path = sol_path + file_path[4:-4] + f'_{tid}' + '.py'
            directory = os.path.dirname(python_file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)

            print('python_file_path:', python_file_path, sep='\n')
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
