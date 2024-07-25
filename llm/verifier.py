from utils import (ask_llm, read_txt_file, write_py_file, run_py_file, limit_text, check_correct_in_file,
                   extract_python_code, MAXIMUM_EXEC_TIME, MAXIMUM_TEXT_LENGTH, get_output_details)


def get_executable_unit_test_code(args, client, extract_constraints_messages, task_name, city_num, file_base_name,
                                  llm_exec_reflect_num, base_verifier_log_path, base_verifier_path, exec_detail_path,
                                  log_file_path, constraints_content, messages_path, instance_tid, outer_tid,
                                  total_request_llm_num_dict, token_file_path):
    overall_verifier_prompt = ''
    unit_test_status = ''
    unit_test_res = ''
    for ui in range(args.reflect_num):
        # 1. Construct user prompt
        if ui == 0:
            log_content = read_txt_file(path=log_file_path)
            extract_output_details = log_content.split('OUTPUT:')[1].split('ERROR:')[0].strip()
            clipped_log_content = limit_text(text=extract_output_details, max_length=MAXIMUM_TEXT_LENGTH)
            verifier_prompt = (
                'Here is the solution:\n'
                f'{clipped_log_content}\n'
                # f'If {clipped_log_content} does not contain solutions, output "FAIL".\n'
                'Please generate unit tests by using Python code to verify if the solution is correct by checking the following requirements:\n'
                f'{constraints_content}\n'
                'If the solution is correct, output "CORRECT"; otherwise, output "FAIL".'
            )
        else:
            verifier_prompt = overall_verifier_prompt

        user_prompt = {"role": "user", "content": verifier_prompt}
        extract_constraints_messages.append(user_prompt)

        # 2. Verifier LLM: generate unit tests code
        verifier_code_content, response_time = ask_llm(
            client=client, llm_model=args.llm_model, messages=extract_constraints_messages,
            token_file_path=token_file_path, notes='verifier')

        total_request_llm_num_dict['verifier'] += 1
        verifier_code_content = extract_python_code(content=verifier_code_content)

        # 3. Write verifier code to file & execute verifier code
        verifier_file_path = f'{base_verifier_path}/{task_name}/{city_num}/{file_base_name}/{instance_tid}/{outer_tid}/verifier_r{llm_exec_reflect_num}_v{ui}.py'
        write_py_file(path=verifier_file_path, content=verifier_code_content)
        verifier_log_file_path = f'{base_verifier_log_path}/{task_name}/{city_num}/{file_base_name}/{instance_tid}/{outer_tid}/verifier_log_r{llm_exec_reflect_num}_v{ui}.txt'
        verifier_exec_status_str, execution_time, verifier_log_file_path = run_py_file(
            code_path=verifier_file_path, log_path=verifier_log_file_path,
            max_exec_time=MAXIMUM_EXEC_TIME
        )

        # 4. Check verifier execution status
        if verifier_exec_status_str == 'success':
            verify_res_str = check_correct_in_file(file_path=verifier_log_file_path)
            if verify_res_str == 'CORRECT':
                with open(exec_detail_path, 'a') as file:
                    file.write(f"Ask another LLM for verifier code, response time: {response_time:.2f} seconds.\n")
                    file.write(f"Another LLM - pass verifier\n")
                return 'success', 'CORRECT', total_request_llm_num_dict
            elif verify_res_str == 'FAIL':
                with open(exec_detail_path, 'a') as file:
                    file.write(f"Ask another LLM for verifier code, response time: {response_time:.2f} seconds.\n")
                    file.write(f"Another LLM - fail verifier\n")
                return 'success', 'FAIL', total_request_llm_num_dict
            elif verify_res_str == 'None':
                unit_test_status = 'success'
                unit_test_res = 'None'

                verify_log_content = read_txt_file(path=verifier_log_file_path)
                clipped_verify_log_content = limit_text(text=verify_log_content, max_length=MAXIMUM_TEXT_LENGTH)
                overall_verifier_prompt = (
                    f'The generated unit tests for verification does not output "CORRECT" or "FAIL". Here is the executed information:\n'
                    f'{clipped_verify_log_content}\n'
                    'Please regenerate unit tests by using Python code.\n'
                    'If the solution is correct, output "CORRECT"; otherwise, output "FAIL".'
                )

                with open(exec_detail_path, 'a') as file:
                    file.write(f"Ask another LLM for verifier code, response time: {response_time:.2f} seconds.\n")
                    file.write(f"Another LLM - verifier does not output CORRECT OR FAIL.\n"
                               f"More info: {clipped_verify_log_content}\n\n\n")
        else:
            unit_test_status = 'fail'
            unit_test_res = 'not_executed'

            # Verifier: user prompt
            verify_log_content = read_txt_file(path=verifier_log_file_path)
            # Format the verifier log content
            verify_log_content = get_output_details(content=verify_log_content)
            clipped_verify_log_content = limit_text(text=verify_log_content, max_length=MAXIMUM_TEXT_LENGTH)
            overall_verifier_prompt = (
                f'The generated unit tests for verification have bugs. Here is the executed information:\n'
                f'{clipped_verify_log_content}\n'
                f'Please fix all bugs. If fixing bugs is too complex, you may generate new unit tests by using Python code.'
            )

            with open(exec_detail_path, 'a') as file:
                file.write(f"Ask another LLM for verifier code, response time: {response_time:.2f} seconds.\n")
                file.write(f"Another LLM - The verifier has bugs.\n")

        # verify_res_str == 'None' or verifier_exec_status_str == 'error' / 'timeout'
        response_verifier = {"role": "assistant", "content": verifier_code_content}
        extract_constraints_messages.append(response_verifier)

        with open(messages_path, 'a') as file:
            file.write(f"Another LLM - User - Verifier prompt.\n")
            file.write(f"Another LLM - Assistant - Verifier: {verifier_file_path}\n")

    return unit_test_status, unit_test_res, total_request_llm_num_dict
