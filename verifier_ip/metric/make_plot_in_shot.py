# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data extracted from the provided files
data = {
    'gpt4/zero/pass_overall/single/TSP': {10: 1.0, 15: 0.9199999999999999, 20: 0.8400000000000001},
    'gpt4/zero/pass_overall/single/BTSP': {10: 0.9199999999999999, 15: 0.68, 20: 0.68},
    'gpt4/zero/pass_overall/single/GTSP': {10: 0.96, 15: 0.96, 20: 1.0},
    'gpt4/zero/pass_overall/single/KTSP': {10: 1.0, 15: 0.6799999999999999, 20: 0.56},
    'gpt4/zero/pass_overall/multiple/mTSP': {22: 0.6, 16: 0.6, 19: 0.8, 21: 0.8, 23: 0.8},
    'gpt4/zero/pass_overall/multiple/mTSP_MinMax': {22: 0.4, 16: 0.6, 19: 1.0, 21: 0.4, 23: 0.8},
    'gpt4/zero/pass_overall/multiple/mTSPMD': {22: 1.0, 16: 0.0, 19: 0.0, 21: 0.6, 23: 0.0},
    'gpt4/zero/pass_overall/multiple/CVRP': {22: 0.6, 16: 1.0, 19: 0.6, 21: 0.8, 23: 0.2},
}

new_data = {
    'gpt4/zero/pass_one/single/TSP': {10: 0.4, 15: 0.24000000000000005, 20: 0.24},
    'gpt4/zero/pass_one/single/BTSP': {10: 0.32, 15: 0.16, 20: 0.08},
    'gpt4/zero/pass_one/single/GTSP': {10: 0.64, 15: 0.68, 20: 0.56},
    'gpt4/zero/pass_one/single/KTSP': {10: 0.4800000000000001, 15: 0.44000000000000006, 20: 0.31999999999999995},
    'gpt4/zero/pass_one/multiple/mTSP': {22: 0.0, 16: 0.4, 19: 0.2, 21: 0.2, 23: 0.4},
    'gpt4/zero/pass_one/multiple/mTSP_MinMax': {22: 0.2, 16: 0.4, 19: 0.6, 21: 0.4, 23: 0.4},
    'gpt4/zero/pass_one/multiple/mTSPMD': {22: 0.0, 16: 0.0, 19: 0.0, 21: 0.0, 23: 0.0},
    'gpt4/zero/pass_one/multiple/CVRP': {22: 0.0, 16: 0.2, 19: 0.2, 21: 0.0, 23: 0.0},
}

debug_data = {
    'gpt4/zero/pass_debug/single/TSP': {10: 0.8800000000000001, 15: 0.44000000000000006, 20: 0.6799999999999999},
    'gpt4/zero/pass_debug/single/BTSP': {10: 0.64, 15: 0.27999999999999997, 20: 0.32},
    'gpt4/zero/pass_debug/single/GTSP': {10: 1.0, 15: 1.0, 20: 1.0},
    'gpt4/zero/pass_debug/single/KTSP': {10: 0.8800000000000001, 15: 0.6, 20: 0.56},
    'gpt4/zero/pass_debug/multiple/mTSP': {22: 0.2, 16: 0.8, 19: 0.4, 21: 0.6, 23: 0.4},
    'gpt4/zero/pass_debug/multiple/mTSP_MinMax': {22: 0.4, 16: 0.6, 19: 1.0, 21: 0.6, 23: 0.8},
    'gpt4/zero/pass_debug/multiple/mTSPMD': {22: 0.4, 16: 0.0, 19: 0.2, 21: 0.4, 23: 0.0},
    'gpt4/zero/pass_debug/multiple/CVRP': {22: 0.0, 16: 0.8, 19: 0.4, 21: 0.4, 23: 0.0},
}

# Tasks and their respective x-values in the data
tasks = ['TSP', 'BTSP', 'GTSP', 'KTSP', 'mTSP', 'mTSP_MinMax', 'mTSPMD', 'CVRP']
x_pos = np.arange(len(tasks))

# Aggregating data for plotting
task_data = {task: [] for task in tasks}
new_task_data = {task: [] for task in tasks}
debug_task_data = {task: [] for task in tasks}

for key, values in data.items():
    task_name = key.split('/')[-1]
    success_rates = list(values.values())
    avg_success_rate = np.mean(success_rates)
    task_data[task_name].append(avg_success_rate)

for key, values in new_data.items():
    task_name = key.split('/')[-1]
    success_rates = list(values.values())
    avg_success_rate = np.mean(success_rates)
    new_task_data[task_name].append(avg_success_rate)

for key, values in debug_data.items():
    task_name = key.split('/')[-1]
    success_rates = list(values.values())
    avg_success_rate = np.mean(success_rates)
    debug_task_data[task_name].append(avg_success_rate)

# Preparing data for bar plot
bars = []
new_bars = []
debug_bars = []

for task in tasks:
    bars.append(np.mean(task_data[task]))
    new_bars.append(np.mean(new_task_data[task]))
    debug_bars.append(np.mean(debug_task_data[task]))

# Plotting all datasets on the same plot with overlapping bars
plt.figure(figsize=(12, 6))

bar_width = 0.8

# Original data (Overall)
plt.bar(x_pos, bars, width=bar_width, label='Overall', alpha=0.7, color='#ff7f0e')


# Debug data
plt.bar(x_pos, debug_bars, width=bar_width, label='Debug', alpha=0.8, color='#1f77b4')


# New data (Pass@1)
plt.bar(x_pos, new_bars, width=bar_width, label='Pass@1', alpha=0.7, color='#2ca02c')


plt.xticks(x_pos, tasks)
plt.ylabel('Average Success Rate')
# plt.title('Average Success Rate')
plt.legend(loc='upper right')
plt.grid(axis='y')

# Display plot
plt.show()
