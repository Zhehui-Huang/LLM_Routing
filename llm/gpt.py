import sys
import os
import argparse

from openai import OpenAI
from utils import ask_llm, LLM_SYSTEM_PROMPT


def solve_problem(args):
    # Restart OpenAI
    client = OpenAI()

    # 1. Load the task description
    task_to_code_prompt = ''

    # 2. Construct the messages
    messages = [
        {"role": "system", "content": LLM_SYSTEM_PROMPT},
        {"role": "user", "content": task_to_code_prompt}
    ]
    for i in range(args.reflect_num):
        print(f"Reflect count: {i}")
        # 3. Ask LLMs and get code
        code_solution_content = ask_llm(client=client, llm_model=args.llm_model, messages=messages)

        # 4. Save code.

        # 5. Execute the code
        # exec(code_solution_content)

        # 6. Verify executing results by using verifier

        # 7. If succeeded, break the loop; Otherwise, append info into messages and continue to reflect.



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--llm_model', type=str, default='gpt-4-turbo',
                        choices=['gpt-4-turbo-2024-04-09', 'gpt-4o-2024-05-13', 'gpt-4o-mini-2024-07-18'])
    parser.add_argument('--reflect_num', type=int, default=5, help='Default: self reflect 5 times.')
    return parser.parse_args()


def main():
    args = get_args()
    solve_problem(args=args)


if __name__ == '__main__':
    sys.exit(main())
