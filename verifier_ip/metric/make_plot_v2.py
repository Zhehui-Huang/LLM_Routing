# Import necessary libraries
import os.path

import matplotlib.pyplot as plt
import numpy as np


# Data extracted from the provided files
# data = {
#     'gpt4/zero/pass_overall/single/TSP': {10: 1.0, 15: 0.9199999999999999, 20: 0.8400000000000001},
#     'gpt4/zero/pass_overall/single/BTSP': {10: 0.9199999999999999, 15: 0.68, 20: 0.68},
#     'gpt4/zero/pass_overall/single/GTSP': {10: 0.96, 15: 0.96, 20: 1.0},
#     'gpt4/zero/pass_overall/single/KTSP': {10: 1.0, 15: 0.6799999999999999, 20: 0.56},
#     'gpt4/zero/pass_overall/multiple/mTSP': {22: 0.6, 16: 0.6, 19: 0.8, 21: 0.8, 23: 0.8},
#     'gpt4/zero/pass_overall/multiple/mTSP_MinMax': {22: 0.4, 16: 0.6, 19: 1.0, 21: 0.4, 23: 0.8},
#     'gpt4/zero/pass_overall/multiple/mTSPMD': {22: 1.0, 16: 0.0, 19: 0.0, 21: 0.6, 23: 0.0},
#     'gpt4/zero/pass_overall/multiple/CVRP': {22: 0.6, 16: 1.0, 19: 0.6, 21: 0.8, 23: 0.2},
# }
#
# new_data = {
#     'gpt4/zero/pass_one/single/TSP': {10: 0.4, 15: 0.24000000000000005, 20: 0.24},
#     'gpt4/zero/pass_one/single/BTSP': {10: 0.32, 15: 0.16, 20: 0.08},
#     'gpt4/zero/pass_one/single/GTSP': {10: 0.64, 15: 0.68, 20: 0.56},
#     'gpt4/zero/pass_one/single/KTSP': {10: 0.4800000000000001, 15: 0.44000000000000006, 20: 0.31999999999999995},
#     'gpt4/zero/pass_one/multiple/mTSP': {22: 0.0, 16: 0.4, 19: 0.2, 21: 0.2, 23: 0.4},
#     'gpt4/zero/pass_one/multiple/mTSP_MinMax': {22: 0.2, 16: 0.4, 19: 0.6, 21: 0.4, 23: 0.4},
#     'gpt4/zero/pass_one/multiple/mTSPMD': {22: 0.0, 16: 0.0, 19: 0.0, 21: 0.0, 23: 0.0},
#     'gpt4/zero/pass_one/multiple/CVRP': {22: 0.0, 16: 0.2, 19: 0.2, 21: 0.0, 23: 0.0},
# }
#
# debug_data = {
#     'gpt4/zero/pass_debug/single/TSP': {10: 0.8800000000000001, 15: 0.44000000000000006, 20: 0.6799999999999999},
#     'gpt4/zero/pass_debug/single/BTSP': {10: 0.64, 15: 0.27999999999999997, 20: 0.32},
#     'gpt4/zero/pass_debug/single/GTSP': {10: 1.0, 15: 1.0, 20: 1.0},
#     'gpt4/zero/pass_debug/single/KTSP': {10: 0.8800000000000001, 15: 0.6, 20: 0.56},
#     'gpt4/zero/pass_debug/multiple/mTSP': {22: 0.2, 16: 0.8, 19: 0.4, 21: 0.6, 23: 0.4},
#     'gpt4/zero/pass_debug/multiple/mTSP_MinMax': {22: 0.4, 16: 0.6, 19: 1.0, 21: 0.6, 23: 0.8},
#     'gpt4/zero/pass_debug/multiple/mTSPMD': {22: 0.4, 16: 0.0, 19: 0.2, 21: 0.4, 23: 0.0},
#     'gpt4/zero/pass_debug/multiple/CVRP': {22: 0.0, 16: 0.8, 19: 0.4, 21: 0.4, 23: 0.0},
# }

def format_data(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Splitting the content into lines
    lines = file_content.strip().split('\n')

    # Initializing the dictionary to store formatted data
    formatted_dict = {}
    # Keeping track of the current task key
    current_task = None

    for line in lines:
        if line.strip() and not line.startswith('Overall Success') and not line.startswith('###'):
            if line.startswith('gpt4/'):
                # This is a new key for the task, reset the current task
                current_task = line.strip().strip(':')
                formatted_dict[current_task] = {}
            elif current_task:
                # This is a value for the current task, split and store it
                key, value = line.split(':')
                key = int(key.strip())
                value = float(value.strip().strip(','))
                formatted_dict[current_task][key] = value

    # Print the formatted dictionary
    print(formatted_dict)
    return formatted_dict


context_list = ['zero', 'pseudo-code_v2', 'pseudo-code_v3', 'pdf_paper_v2', 'pdf_paper_v3']
# Plotting all datasets on the same plot with overlapping bars
plt.figure(figsize=(12, 6))

bar_width = 0.12
gap = bar_width

tasks = ['TSP', 'BTSP', 'GTSP', 'KTSP', 'mTSP', 'mTSP_MinMax', 'mTSPMD', 'CVRP']
x_pos = np.arange(len(tasks))
# Aggregating data for plotting

for cid, context in enumerate(context_list):
    # if context == 'math':
    #     continue
    base_path = f'/home/ethan/repository/test_verifier/LLM_Routing/verifier_ip/metric/clean_data/gpt4/{context}'
    post_path = 'all_success.txt'

    data = format_data(os.path.join(base_path, 'pass_overall', post_path))
    task_data = {task: [] for task in tasks}

    for key, values in data.items():
        task_name = key.split('/')[-1]
        success_rates = list(values.values())
        avg_success_rate = np.mean(success_rates)
        task_data[task_name].append(avg_success_rate)

    # Preparing data for bar plot
    bars = []
    new_bars = []
    debug_bars = []

    for task in tasks:
        bars.append(np.mean(task_data[task]))

    # Original data (Overall)
    plt.bar(x_pos + (cid - 3) * gap, bars, width=bar_width, label=context, alpha=0.7)

    # # Debug data
    # plt.bar(x_pos, debug_bars, width=bar_width, label='Debug', alpha=0.8, color='#1f77b4')
    #
    #
    # # New data (Pass@1)
    # plt.bar(x_pos + gap, new_bars, width=bar_width, label='Pass@1', alpha=0.7, color='#2ca02c')

plt.xticks(x_pos, tasks)
plt.ylabel('Average Success Rate')
# plt.title('Average Success Rate')
plt.legend(loc='upper right')
plt.grid(axis='y')

# Display plot
plt.show()
