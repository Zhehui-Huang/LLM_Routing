import subprocess
import time
import os
import sys


def read_all_files(root_directory):
    # List to hold the contents of all text files
    text_files_loc = []

    # Walk through the directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.py'):
                # Construct the full file path
                file_path = os.path.join(dirpath, filename)
                text_files_loc.append(file_path)

    text_files_loc.sort()
    return text_files_loc

def extract_execute_code(python_file_path, evaluate_file_path):
    start_time = time.time()
    # Execute the Python script
    external_solutions = subprocess.run(['python', python_file_path], capture_output=True, text=True)
    # Print or process the output
    print("external_solutions.stdout:   ", external_solutions.stdout, sep="\n")
    # In case of errors
    print("external_solutions.stderr:   ", external_solutions.stderr, sep="\n")

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total running time: {total_time} seconds")

    solution = ''
    if external_solutions.stderr != "":
        solution += "**no solution**"
    else:
        solution += external_solutions.stdout

    solution += f"\nTotal running time: {total_time} seconds"

    with open(evaluate_file_path, 'w') as python_file:
        python_file.write(solution)


def main():
    text_files_content = read_all_files(root_directory='solution/1_direct_no_vis')
    print(text_files_content)
    for file_path in text_files_content:
        print('file_path:', file_path, sep='\n')

        evaluate_file_path = 'evaluate' + file_path[8:-3] + '.txt'
        if os.path.exists(evaluate_file_path):
            print('python_file_path exists:', evaluate_file_path, sep='\n')
            continue

        directory = os.path.dirname(evaluate_file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        extract_execute_code(python_file_path=file_path, evaluate_file_path=evaluate_file_path)


if __name__ == '__main__':
    sys.exit(main())
