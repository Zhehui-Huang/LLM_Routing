import sys
from openai import OpenAI

from utils import (extract_execute_code, nltd_to_math, math_to_solution, read_file, gpt_prompt_tips,
                   nltd_to_math_requirements)

client = OpenAI()
gpt_model = "gpt-4-0125-preview"
python_file_path = '../2_math_extracted_code.py'


def solve_problem(task_descriptions):
    # 1. Translate natural language task descriptions (NLTD) to mathematical formulations.
    math_content_modify = nltd_to_math(client=client, gpt_model=gpt_model, task_descriptions=task_descriptions)
    # 2. Math to solution
    solution_content = math_to_solution(client=client, gpt_model=gpt_model, task_descriptions=task_descriptions,
                                        math_content_modify=math_content_modify, prompt_tips=gpt_prompt_tips)

    # 3. Solve the problem
    extract_execute_code(problem_solving_content=solution_content, python_file_path=python_file_path)
    print('End!')


def main():
    env_and_task = read_file(file_path="../../task/E-m_tsp_max_score_with_time_budget/3/10_points.txt")

    task_descriptions = f"{env_and_task} {nltd_to_math_requirements} {gpt_prompt_tips}"

    solve_problem(task_descriptions=task_descriptions)


if __name__ == '__main__':
    sys.exit(main())
