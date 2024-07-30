import os.path
import matplotlib.pyplot as plt
import numpy as np

def format_data(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()

    lines = file_content.strip().split('\n')
    formatted_dict = {}
    current_task = None

    for line in lines:
        if line.strip() and not line.startswith('Overall Success') and not line.startswith('###'):
            if line.startswith('gpt4/'):
                current_task = line.strip().strip(':')
                formatted_dict[current_task] = {}
            elif current_task:
                key, value = line.split(':')
                key = int(key.strip())
                value = float(value.strip().strip(','))
                formatted_dict[current_task][key] = value

    return formatted_dict

pass_type_list = ['pass_overall', 'pass_debug', 'pass_one']
used_context = 'zero'
plt.figure(figsize=(12, 6))

bar_width = 0.2
tasks = ['TSP', 'BTSP', 'GTSP', 'KTSP', 'mTSP', 'mTSP_MinMax', 'mTSPMD', 'CVRP']
x_pos = np.arange(len(tasks))

task_data = {task: [0] * len(pass_type_list) for task in tasks}

# Define a color for each pass type
colors = ['blue', 'orange', 'green']

for cid, pass_type in enumerate(pass_type_list):
    base_path = f'/home/ethan/repository/test_verifier/LLM_Routing/verifier_ip/metric/clean_data/gpt4/{used_context}/{pass_type}'
    post_path = 'all_success.txt'

    data = format_data(os.path.join(base_path, post_path))

    for key, values in data.items():
        task_name = key.split('/')[-1]
        if task_name in task_data:
            success_rates = list(values.values())
            avg_success_rate = np.mean(success_rates)
            task_data[task_name][cid] = avg_success_rate

# Plotting data: tasks first, then pass_type_list
for task_id, task in enumerate(tasks):
    if task == 'GTSP':
        pass_type_list_v2 = ['pass_debug', 'pass_overall', 'pass_one']
        bars = task_data[task]
        plt.bar(x_pos[task_id], bars[1], width=bar_width, alpha=0.7, color=colors[1],
                label='pass_debug' if task_id == 0 else "")
        plt.bar(x_pos[task_id], bars[0], width=bar_width, alpha=0.7, color=colors[0], label='pass_overall' if task_id == 0 else "")
        plt.bar(x_pos[task_id], bars[2], width=bar_width, alpha=0.7, color=colors[2],
                label='pass_one' if task_id == 0 else "")
    else:
        for cid, pass_type in enumerate(pass_type_list):
            bars = task_data[task]
            plt.bar(x_pos[task_id], bars[cid], width=bar_width, alpha=0.7, color=colors[cid], label=pass_type if task_id == 0 else "")

plt.xticks(x_pos + bar_width, tasks)
plt.ylabel('Average Success Rate')
plt.legend(loc='upper right')
plt.grid(axis='y')
plt.show()
