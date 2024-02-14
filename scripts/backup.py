import sys
from openai import OpenAI

client = OpenAI()

task_descriptions = (
    "### Task descriptions: I have two robots, and I want both robot visit all cities exactly once and "
    "returns to the origin city. ### "
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
    "8. Cost: The cost of one action is measured by the distance between two nodes. ### "
    "Please translate task descriptions to mathematical problems given the information above. The mathematical "
    "problem should be as concise as possible. Do not print any analysis or unnecessary things. "
    "Take a deep breath. Think step by step. "
    "I will tip $500 if you give me perfect solutions. It is really important to my career and life."
)

# ****************************************
# 1. Translate natural language task descriptions (NLTD) to mathematical formulations.
math_formulation = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": task_descriptions}
    ],
    stream=False,
)

# for chunk in response:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")

print('Math formulation:    ', math_formulation.choices[0].message.content)
print('====================================================================================================')

problem_solving = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": task_descriptions},
        {"role": "assistant", "content": math_formulation.choices[0].message.content},
        {"role": "user",
         "content": "Given the above mathematical formulation, please solve the problem. If there is no solution, "
                    "print no solution. If there is a solution, you need to provide two things, 1. Path 2. Python code to "
                    "visualize the path and mark the movement with arrows."
        }
    ],
    stream=False,
)

print('Solutions: ', problem_solving.choices[0].message.content)

def main():
    task_descriptions = (
        "### Task descriptions: I have two robots, and I want both robot visit all cities exactly once and "
        "returns to the origin city. ### "
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
        "8. Cost: The cost of one action is measured by the distance between two nodes. ### "
        "Please translate task descriptions to mathematical problems given the information above. The mathematical "
        "problem should be as concise as possible. Do not print any analysis or unnecessary things. "
        "Take a deep breath. Think step by step. "
        "I will tip $500 if you give me perfect solutions. It is really important to my career and life."
    )
    solve_problem(task_descriptions)


if __name__ == '__main__':
    sys.exit(main())