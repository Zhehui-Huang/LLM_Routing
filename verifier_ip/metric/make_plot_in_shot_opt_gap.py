import os.path

import matplotlib.pyplot as plt
import numpy as np


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
        if line.strip() and not line.startswith('Overall Opt Gap') and not line.startswith('###'):
            if line.startswith('gpt4/'):
                # This is a new key for the task, reset the current task
                current_task = line.strip().strip(':')
                formatted_dict[current_task] = {}
            elif current_task:
                # This is a value for the current task, split and store it
                key, value = line.split(':')
                key = int(key.strip())
                value_str = value.strip().strip(',')
                if value_str.lower() != 'nan':
                    value = float(value_str)
                    formatted_dict[current_task][key] = value

    # Print the formatted dictionary
    print(formatted_dict)
    return formatted_dict



# context_list = ['zero', 'pseudo-code_v2', 'pseudo-code_v3', 'pdf_paper_v2', 'pdf_paper_v3']
pass_type_list = ['pass_overall', 'pass_debug', 'pass_one']
used_context = 'zero'
# Plotting all datasets on the same plot with overlapping bars
plt.figure(figsize=(12, 6))

bar_width = 0.6
gap = bar_width

tasks = ['TSP', 'BTSP', 'GTSP', 'KTSP', 'mTSP', 'mTSP_MinMax', 'mTSPMD', 'CVRP']
x_pos = np.arange(len(tasks))
# Aggregating data for plotting

for cid, pass_type in enumerate(pass_type_list):
    # if context == 'math':
    #     continue
    base_path = f'/home/ethan/repository/test_verifier/LLM_Routing/verifier_ip/metric/clean_data/gpt4/{used_context}/{pass_type}'
    post_path = 'all_opt_gap.txt'

    data = format_data(os.path.join(base_path, post_path))
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
    # plt.bar(x_pos + (cid - 3) * gap, bars, width=bar_width, label=pass_type, alpha=0.7)
    plt.bar(x_pos, bars, width=bar_width, label=pass_type, alpha=0.7)

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
