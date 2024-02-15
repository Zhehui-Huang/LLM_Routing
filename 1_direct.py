import sys

from openai import OpenAI

from utils import extract_execute_code, read_file, direct_solution_requirements, gpt_prompt_tips

client = OpenAI()
gpt_model = "gpt-4-0125-preview"
python_file_path = 'tmp/1_direct_extracted_code.py'


def solve_problem(task_descriptions):
    # 1. Translate natural language task descriptions (NLTD) to solutions.
    problem_solving_reply = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": task_descriptions}
        ],
        stream=False,
    )
    problem_solving_content = problem_solving_reply.choices[0].message.content
    print('Solutions: ', problem_solving_content, sep="\n")

    # 2. Print the solution
    extract_execute_code(problem_solving_content=problem_solving_content, python_file_path=python_file_path)
    print('End!')


def main():
    env_and_task = read_file(file_path="task/simple/1.txt")

    task_descriptions = f"{env_and_task} {direct_solution_requirements} {gpt_prompt_tips}"

    solve_problem(task_descriptions=task_descriptions)


if __name__ == '__main__':
    sys.exit(main())
