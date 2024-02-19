import sys
from openai import OpenAI

client = OpenAI()
gpt_model = "gpt-4-0125-preview"


# TODO: Need to add API for Gemini

def solve_problem(task_descriptions):
    while True:
        # 1. Translate natural language task descriptions (NLTD) to mathematical formulations.
        math_formulation_reply = client.chat.completions.create(
            model=gpt_model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": task_descriptions}
            ],
            stream=False,
        )

        math_formulation_content = math_formulation_reply.choices[0].message.content
        print('Math formulation:    ', math_formulation_content)
        print('====================================================================================================')

        # 2. Combine (NLTD + Mathematical formulation) to check consistent
        math_prex = "### Following is mathematical formulation. ###"
        math_formulation_content_modified = math_prex + math_formulation_content
        consistent_check_prex = (
            "### Question: are following natural language task descriptions and the mathematical formulation convey the same meaning? "
            "If your answer is yes, please only output ***yes***. If your answer is no, please only answer two things. "
            "1. please output ***No*** . 2. clarifications questions to users. ###")
        consistent_check = f"{consistent_check_prex} {task_descriptions} {math_formulation_content_modified}"

        consistent_check_reply = client.chat.completions.create(
            model=gpt_model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": task_descriptions},
                {"role": "assistant", "content": math_formulation_content},
                {"role": "user", "content": consistent_check},
            ],
            stream=False,
        )
        consistent_check_content = consistent_check_reply.choices[0].message.content
        print('Consistent check:    ', consistent_check_content)
        print('====================================================================================================')

        if "***no***" in consistent_check_content:
            print('Please clarify the task descriptions.')
            clarifications_from_user = input("")
            clarifications_from_user_prex = "### Following are clarifications of tasks from user.###"
            consistent_check_content_modified = f"{clarifications_from_user_prex} {clarifications_from_user}"
            task_descriptions = f"{task_descriptions} {consistent_check_content_modified}"
        elif "***yes***" in consistent_check_content:
            break
        else:
            raise ValueError("The consistent check response is not as expected.")

    # 3. Solve the problem
    problem_solving_reply = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": task_descriptions},
            {"role": "assistant", "content": math_formulation_content},
            {"role": "user",
             "content": "Given the above mathematical formulation, please solve the problem. If there is no solution, "
                        "print no solution. If there is a solution, you need to provide two things, 1. Path 2. Python "
                        "code to visualize the path and mark the movement with arrows."
             }
        ],
        stream=False,
    )
    problem_solving_content = problem_solving_reply.choices[0].message.content
    print('Solutions: ', problem_solving_content)


def main():
    prex = "### Following are natural langauge task descriptions. ###"
    environment_info = (
        "### These two robots both start at (0, 0).) Environment information: "
        "1. Robot: R = {1, ..., n} be the set of robots, where n is the total number of robots. If the "
        "robot number is not defined in the task description, ask the user to clarify. "
        "2. Map area: The area is a 2D grid, the size of which is 6x6. "
        "3. Time Discretization: Divide the time into discrete time steps. Let T = {1, 2, ..., Tmax} be "
        "the set of time steps. If the max time is not provided in the task description, we assume the "
        "max time is infinite. "
        "4. Robot positions: The position of robot at time t is represented by (x(t), y(t)). "
        "5. Path: Let P be the path followed by robot during the whole episode. The paths P are subject to constraints "
        "and should finish the task. "
        "6. Objective Function: Define an objective function that captures the overall efficiency or effectiveness of the "
        "patrol. This could involve minimizing the total patrol time, maximizing coverage, or considering other factors. "
        "7. Available Actions: Robot can go from one node to any nodes. (Complete graph) "
        "8. Cost: The cost of one action is measured by the distance between two nodes. ###"
    )

    task = (
        "### Task: I have two robots, and I want both robot visit all cities exactly once and "
        "returns to the origin city. ###"
    )

    solution_requirements = (
        "### Solution requirements: Please translate task descriptions to mathematical problems given the information above. "
        "The mathematical problem should be as concise as possible. Do not print any analysis or unnecessary things. ###"
    )

    prompt_tips = (
        "### Prompt requirements: Do not print any analysis or unnecessary things. Take a deep breath. Think step by step. "
        "I will tip $500 if you give me perfect solutions. It is really important to my career and life. "
        "I have no hands. ###"
    )

    task_descriptions = f"{prex} {environment_info} {task} {solution_requirements} {prompt_tips}"

    solve_problem(task_descriptions=task_descriptions)


if __name__ == '__main__':
    sys.exit(main())
