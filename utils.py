import subprocess


def extract_execute_code(problem_solving_content, python_file_path):
    # Extra python code from problem_solving_content
    start_marker = "```python"  # Starting marker of Python code
    end_marker = "```"  # Ending marker of Python code

    start_index = problem_solving_content.find(start_marker) + len(start_marker)
    end_index = problem_solving_content.find(end_marker, start_index)
    extracted_code = problem_solving_content[start_index:end_index].strip()

    with open(python_file_path, 'w') as python_file:
        python_file.write(extracted_code)  # Write the extracted code to the file

    # Execute the Python script
    external_solutions = subprocess.run(['python', python_file_path], capture_output=True, text=True)
    # Print or process the output
    print("external_solutions.stdout:   ", external_solutions.stdout)
    # In case of errors
    print("external_solutions.stderr:   ", external_solutions.stderr)