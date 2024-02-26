import copy

import google.generativeai as genai
from google.generativeai.types import generation_types

from utils import gemini_prompt_tips, extract_execute_code, save_evaluation

GOOGLE_API_KEY = "AIzaSyBruy7vdcDDCHfIrNxgiYkBhAl7g2ajXGA"
genai.configure(api_key=GOOGLE_API_KEY)


def ask_gemini(questions):
    gemini_model = genai.GenerativeModel('gemini-pro')
    gemini_chat = gemini_model.start_chat(history=[])
    question_reply = gemini_chat.send_message(f"{questions} \n{gemini_prompt_tips}")
    answer = question_reply.text
    return answer


def gemini_nltd_to_math(task_descriptions):
    math_content = ask_gemini(task_descriptions)
    math_content_modify = f"### \nMathematical formulation: {math_content} \n###"
    print('Mathematical formulation:    ', math_content_modify, sep='\n')
    print('====================================================================================================')
    return math_content_modify


def gemini_math_to_solution(math_content_modify, sol_given_parts):
    questions = (f"Given the mathematical formulation: \n{math_content_modify}. \nPlease provide a solution. \n"
                 f"{sol_given_parts}")
    answer = ask_gemini(questions)
    return answer


def gemini_reflect_solution(
        ori_python_file_path, math_content_modify, reflect_num=3, question_for_answer=None,
        external_solutions=None, total_time=None, env_and_task=None, sol_given_parts=None, external_solver=False,
        external_tool_name=""):
    # Solve the problem
    find_solution_flag = False
    extra_eval_content = None
    python_file_path = ori_python_file_path

    final_external_solutions = copy.deepcopy(external_solutions)
    final_total_time = total_time

    for reflect_id in range(reflect_num):
        print(f'Reflection round: {reflect_id}')

        if external_solutions is None:
            exec_res = f"'''\nHere is the solution: ***no solution***\n'''"
        else:
            if external_solutions.stderr == "":
                exec_res = f"'''\nHere is the solution:\n{external_solutions.stdout} \n'''"
            else:
                exec_res = (f"'''\nHere is the solution:{external_solutions.stdout} \n"
                            f"The solution has errors. \n{external_solutions.stderr}'''")

        print('exec_res: ', exec_res, sep="\n")

        # 2. Check if the solution is correct
        if math_content_modify is not None:
            q_meet_req = f"{math_content_modify} \n{exec_res} \n{question_for_answer}"
        else:
            q_meet_req = f"{env_and_task} \n{exec_res} \n{question_for_answer}"

        print('q_meet_req: ', q_meet_req, sep="\n")

        q_meet_req_content = ask_gemini(questions=q_meet_req)
        print('q_meet_req_content: ', q_meet_req_content, sep="\n")

        verify_external_solutions, _ = extract_execute_code(
            problem_solving_content=q_meet_req_content, python_file_path=python_file_path)

        # if verify_external_solutions is not None:
        #     print('verify_external_solutions: ', verify_external_solutions.stdout, sep="\n")

        if verify_external_solutions is not None and "YES!!!" in verify_external_solutions.stdout and verify_external_solutions.stderr == "":
            extra_eval_content = f'Find the correct solution in round: {reflect_id}!'
            print(extra_eval_content)
            find_solution_flag = True

            final_external_solutions = copy.deepcopy(external_solutions)
            final_total_time = total_time

            save_evaluation(python_file_path=ori_python_file_path, external_solutions=final_external_solutions,
                            total_time=final_total_time, extra_eval_content=extra_eval_content,
                            reflect_id=reflect_id + 1)

            break
        else:
            find_no_sol = f'Does Not Find the Solution in round: {reflect_id}'

            if final_external_solutions is None:
                extra_eval_content = f"***no solution*** \nTime Out!\n{find_no_sol} \n{q_meet_req_content} \n"
            else:
                extra_eval_content = (
                    f"{final_external_solutions.stdout} \n {final_external_solutions.stderr} \n {find_no_sol} \n "
                    f"{q_meet_req_content} \n"
                )
            save_evaluation(python_file_path=ori_python_file_path, external_solutions=final_external_solutions,
                            total_time=final_total_time, extra_eval_content=extra_eval_content,
                            reflect_id=reflect_id + 1)

            if reflect_id == reflect_num - 1:
                print(find_no_sol)
                break

            # Since does not find the solution, we need to provide the correct solution
            if math_content_modify is None:
                tmp_pre_content = env_and_task
            else:
                tmp_pre_content = math_content_modify

            if verify_external_solutions is None:
                tmp_verify_external_solutions_out = q_meet_req_content
            else:
                tmp_verify_external_solutions_out = verify_external_solutions.stdout

            if external_solver is False:
                modified_task_descriptions = (
                    f"{tmp_pre_content} \n{exec_res} \nHere are the analysis why the solution is not correct.\n"
                    f"{tmp_verify_external_solutions_out} \nPlease provide a correct solution with Python code. "
                    f"You can use the previous solution as a reference. \n"
                    f"If the solution is ***no solution***, you can use a heuristic solver to solve the problem. \n"
                    f"If the solution has errors, you can either fix the error or solve the problem from scratch, "
                    f"please use your best judgment. "
                    f"\n{sol_given_parts}"
                )
            else:
                modified_task_descriptions = (
                    f"{tmp_pre_content} \n{exec_res} \nHere are the analysis why the solution is not correct.\n"
                    f"{tmp_verify_external_solutions_out} \nPlease provide a correct solution with Python code. "
                    f"You can use the previous solution as a reference. \n"
                    f"If the solution is ***no solution***, you can either stick on the current tool "
                    f"{external_tool_name} or pick another tool (such as Gurobi, OR-Tools, etc.) "
                    f"to solve the problem. \n"
                    f"If the solution has errors, you have three choices, fix these errors, solve the problem "
                    f"with current tool {external_tool_name}, or pick another tool. Please use your best judgment. \n"
                    f"{sol_given_parts}"
                )

            print('modified_task_descriptions: ', modified_task_descriptions, sep="\n")

            try:
                reply_content = ask_gemini(questions=modified_task_descriptions)
                print('reply_content:', reply_content, sep='\n')
            except generation_types.StopCandidateException as e:
                reply_content = None
                print("Encountered a StopCandidateException, adjusting input...")
                break

            external_solutions, total_time = extract_execute_code(
                problem_solving_content=reply_content, python_file_path=python_file_path)

    return final_external_solutions, final_total_time, find_solution_flag, extra_eval_content
