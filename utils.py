import subprocess


def nltd_to_math(client, gpt_model, task_descriptions):
    math_reply = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": task_descriptions}
        ],
        stream=False,
    )

    math_content = math_reply.choices[0].message.content
    print('Mathematical problem:    ', math_content, sep='\n')
    print('====================================================================================================')
    math_content_modify = f"### Mathematical problem: {math_content} ###"
    return math_content_modify


def math_to_solution(client, gpt_model, task_descriptions, math_content_modify, prompt_tips):
    pre_problem_solving_questions = (
        "### Solution requirements: Please use Python code to solve the above mathematical problem. "
        "You must consider all constrains regardless of complexity. "
        "If there is a solution, please only output following things without any analysis. "
        "1. Tour (template: Place <text> -> Place <text>) "
        "2. Cost (template: Cost: <text>). "
        "3. Python code to visualize the tour, and mark each movement with an arrow. ###"
    )

    problem_solving_questions = f"{pre_problem_solving_questions} {prompt_tips}"

    solution_reply = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": task_descriptions},
            {"role": "assistant", "content": math_content_modify},
            {"role": "user", "content": problem_solving_questions},
        ],
        stream=False,
    )
    solution_content = solution_reply.choices[0].message.content
    print('Solutions: ', solution_content)
    return solution_content


def consistent_check(client, gpt_model, task_descriptions, environment_info, task, math_content_modify, consistent_check_prex=None):
    if consistent_check_prex is None:
        consistent_check_prex = (
            "### Question: are following natural language task descriptions and mathematical problem convey the "
            "same meaning?"
            "If your answer is yes, please **MUST** only output following: <***yes***>. "
            "If your answer is no, you **MUST** output two things. 1. output: <***no***>. 2. clarifications questions "
            "to users **MUST** only related to natural language task descriptions. You **should not** ask questions "
            "related to mathematical formulations ###")

    task_descriptions_modified = f" '''Following are natural language task descriptions: {environment_info} {task} '''"
    consistent_check_input = f"{consistent_check_prex} {task_descriptions_modified} {math_content_modify}"

    consistent_check_reply = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": task_descriptions},
            {"role": "assistant", "content": math_content_modify},
            {"role": "user", "content": consistent_check_input},
        ],
        stream=False,
    )
    consistent_check_content = consistent_check_reply.choices[0].message.content
    return consistent_check_content, consistent_check_input


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

    return external_solutions
