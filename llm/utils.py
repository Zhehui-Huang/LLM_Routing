import os
import re
import subprocess

import time
import pytz
from datetime import datetime
LA_TIMEZONE = pytz.timezone('America/Los_Angeles')

SINGLE_TASK_LIST = ['TSP', 'BTSP', 'GTSP', 'KTSP', 'MV-TSP']
MULTI_TASK_LIST = ['mTSP', 'mTSP_MinMax', 'mTSPMD', 'CVRP']
# CITY_NUM_LIST = [10, 15, 20, 25, 50]
CITY_NUM_LIST = [10]
MAXIMUM_EXEC_TIME = 600
MAXIMUM_TEXT_LENGTH = 2000

INSTANCE_TRY_TIMES = 5

LLM_SYSTEM_PROMPT = '''
You are an expert in solving various variants of the Traveling Salesman Problem (TSP) and Vehicle Routing Problems (VRP) by using Python code.

Follow these guidelines:
1. Take a deep breath.
2. Think step by step.
3. Ensure the solution is perfect; it is crucial for my career and life.
4. Provide concise and clear answers.
5. Focus on providing the best possible code solution; avoid unnecessary explanations or analysis.

Note: If you fail, there will be severe consequences. If you succeed, there will be a significant reward.

Now, let's proceed with the task at hand.
'''


def ask_llm(client, llm_model, messages):
    start_time = time.time()
    cur_time = datetime.now(LA_TIMEZONE)
    print(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\tAsking LLM ...")

    completion = client.chat.completions.create(
        model=llm_model,
        messages=messages
    )

    end_time = time.time()
    response_time = end_time - start_time
    cur_time = datetime.now(LA_TIMEZONE)
    print(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\tFinished.\tResponse time: {response_time:.2f} seconds.")
    return completion.choices[0].message.content, response_time


def list_files(directory):
    file_list = []
    file_name_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
            file_name_list.append(file)
    return file_list, file_name_list


def extract_value(file_name):
    match = re.search(r'city_(.*?)_instance', file_name)
    if match:
        value = match.group(1)
    else:
        raise ValueError(f"Cannot extract city number from file name: {file_name}")

    return value


def read_txt_file(path):
    with open(path, 'r') as file:
        content = file.read()

    return content


def write_py_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file:
        file.write(content)


def run_py_file(code_path, log_path, max_exec_time):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    # Execute the Python file
    timeout_seconds = max_exec_time

    start_time = time.time()
    cur_time = datetime.now(LA_TIMEZONE)
    print(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\tExecution {code_path}, Log: {log_path}, Max Time: {max_exec_time}...")

    try:
        result = subprocess.run(['python', code_path], capture_output=True, text=True, timeout=timeout_seconds)
        exec_success = (result.returncode == 0)
        if exec_success:
            log_path = log_path.replace('.txt', '_success.txt')
            exec_status_str = 'success'
        else:
            log_path = log_path.replace('.txt', '_error.txt')
            exec_status_str = 'error'

        # Prepare log information
        log_info = {
            'output': result.stdout,
            'error': result.stderr
        }

    except subprocess.TimeoutExpired as _:
        log_path = log_path.replace('.txt', '_timeout.txt')
        exec_status_str = 'timeout'
        log_info = {
            'output': '',
            'error': f'TimeoutExpired: The process exceeded the time limit of {timeout_seconds} seconds.'
        }

    # Calculate execution time
    end_time = time.time()
    execution_time = end_time - start_time
    cur_time = datetime.now(LA_TIMEZONE)
    print(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\tFinished.\tExecution time: {execution_time:.2f} seconds.")

    # Save log information to a file
    with open(log_path, 'w') as log_file:
        for key, value in log_info.items():
            log_file.write(f"{key.upper()}:\n{value}\n\n")

    return exec_status_str, execution_time, log_path


def limit_text(text, max_length):
    middle_length = int(max_length // 2)
    if len(text) > max_length:
        return text[:middle_length] + text[-middle_length:]
    return text


def check_correct_in_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if 'CORRECT' in line:
                return 'CORRECT'
            if 'FAIL' in line:
                return 'FAIL'

    return 'None'


def extract_python_code(content):
    pattern = re.compile(r'```python(.*?)```', re.DOTALL)
    match = pattern.search(content)
    if match:
        return match.group(1).strip()
    else:
        tmp_str = 'print("No Python code block found in the solution reply.")'
        print(tmp_str)
        return tmp_str


def check_log_file_empty(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        output_section = content.split('OUTPUT:')[1].split('ERROR:')[0].strip()
        error_section = content.split('ERROR:')[1].strip()

        # Check if the sections are empty
        output_empty = (output_section == "")
        error_empty = (error_section == "")

    # Determine the result based on the conditions
    if output_empty and error_empty:
        return 'EMPTY'
    else:
        return 'NOT EMPTY'


def write_start_info(file_base_name, base_exec_details_path, task_name, city_num, base_messages_path,
                     instance_tid, outer_tid):
    # 2 Execution results
    exec_detail_path = f'{base_exec_details_path}/{task_name}/{city_num}/{instance_tid}/{outer_tid}/exec_details_{file_base_name}.txt'
    os.makedirs(os.path.dirname(exec_detail_path), exist_ok=True)

    start_time = time.time()
    cur_time = datetime.now(LA_TIMEZONE)
    print(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\tStarting ...")
    with open(exec_detail_path, 'w') as file:
        file.write(f"Start time: [{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\n\n")
        file.write(f"Task file path: {exec_detail_path}\n===\n")

    # 3 Message info
    messages_path = f'{base_messages_path}/{task_name}/{city_num}/{instance_tid}/{outer_tid}/messages_{file_base_name}.txt'
    os.makedirs(os.path.dirname(messages_path), exist_ok=True)
    with open(messages_path, 'w') as file:
        file.write(f"Task file path: {messages_path}\n===\n")

    return exec_detail_path, start_time, messages_path


def write_end_info(start_time, exec_detail_path):
    # 1. Exec details
    end_time = time.time()
    response_time = end_time - start_time
    cur_time = datetime.now(LA_TIMEZONE)
    print(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\tFinished.\tOverall time: {response_time:.2f} seconds.")
    with open(exec_detail_path, 'a') as file:
        file.write(f"[{cur_time.strftime('%Y-%m-%d %H:%M:%S')}]\tFinished.\n\n")
        file.write(f"Overall time: {response_time:.2f} seconds.\n")


def get_output_details(content):
    formatted_str = ''
    output_details = content.split('OUTPUT:')[1].split('ERROR:')[0].strip()
    if output_details != "":
        formatted_str += f'OUTPUT:\n{output_details}\n\n'

    error_details = content.split('ERROR:')[1].strip()
    if error_details != "":
        formatted_str += f'ERROR:\n{error_details}\n\n'

    return formatted_str
