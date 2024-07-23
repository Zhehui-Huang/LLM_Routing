import os
import re
import subprocess

import time
import pytz
from datetime import datetime
LA_TIMEZONE = pytz.timezone('America/Los_Angeles')

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
    exec_status_str = ''

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

    except subprocess.TimeoutExpired as e:
        exec_success = False
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
                return True
            if 'FAIL' in line:
                return False

    raise ValueError("No 'CORRECT' or 'FAIL' found in the output file.")


def extract_python_code(content):
    pattern = re.compile(r'```python(.*?)```', re.DOTALL)
    match = pattern.search(content)
    if match:
        return match.group(1).strip()
    else:
        tmp_str = 'print("No Python code block found in the solution reply.")'
        print(tmp_str)
        return tmp_str
        # raise ValueError("No Python code block found in the solution reply.")

