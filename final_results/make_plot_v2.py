import os
import json
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

benchmark = {
    'A-TSP': 11.09,
    'B-BTSP': 5.0,
    'C-GTSP': 10.19,
    'D-OTSP': 15.56,
    'E-TPP': 221.98,
    'F-TSPTW': 12.18,
    'G-TSPM': 11,
    'H-TSPMDNC': 14.94,
    'I-TSPMDC': 10.16,
    'J-KTSP': 10.40,
    'K-CTSP': 21.95,
}


def calculate_optimality(value, best_value):
    if value == best_value:
        return 1.0
    else:
        return 1 / (1 + (value - best_value) / best_value)


def read_all_json_files(root_directory):
    text_files_loc = []
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.json'):
                file_path = os.path.join(dirpath, filename)
                text_files_loc.append(file_path)
    text_files_loc.sort()
    return text_files_loc


def load_json_files():
    root_dir = '/home/zhehui/LLM_Routing/final_results/1_direct_reflect_v3/4-tsp/back'
    text_files_loc = read_all_json_files(root_directory=root_dir)
    json_datas = []
    for file_path in text_files_loc:
        with open(file_path, "r") as file:
            data = json.load(file)
            json_datas.append(data)

    extracted_parts = [path.split('/')[-1].split('.json')[0] for path in text_files_loc]


    return json_datas, extracted_parts


def compute_mean(values):
    modified_values = []
    for v in values:
        if v == -1:
            continue
        modified_values.append(v)

    if len(modified_values) == 0:
        return 0

    return np.mean(modified_values)


def prepare_plot_data(json_data, extracted_parts):
    plot_data = []
    raw_datas = []
    for jid, file in enumerate(json_data):
        means = []
        raw_data = []
        for key in file.keys():
            values = list(file[key].values())
            values = np.round(values, 2)
            tmp_bench = benchmark[extracted_parts[jid]]
            for x in values:
                if x != -1 and x < tmp_bench:
                    raise ValueError(f'any(x < tmp_bench for x in values): {values} < {tmp_bench}')

            mean = compute_mean(values)
            means.append(mean)
            raw_data.append(values)
        plot_data.append(means)
        raw_datas.append(raw_data)
    return plot_data, raw_datas


json_data, extracted_parts = load_json_files()
plot_data, raw_datas = prepare_plot_data(json_data, extracted_parts)

# Dynamically set group labels based on the number of files
group_labels = [f'File {i + 1}' for i in range(len(json_data))]

# Plotting adjustments
colors = cycle(['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan'])
fig, ax = plt.subplots(figsize=(12, 8))

# Adjust these parameters to change the appearance of the plot
bar_width = 0.8 / len(plot_data[0])  # Adjust the bar width based on number of keys
ind = np.arange(len(group_labels))  # the x locations for the groups

for i in range(len(raw_datas[0])):
    values = [raw_datas[j][i] for j in range(len(raw_datas))]
    # calculate_optimality(best_value, means)
    ordered_keys = sorted(benchmark.keys())

    modified_means = []
    for file_id in range(len(values)):
        tmp_values = values[file_id]

        optimality_data = []
        for tmp_value in tmp_values:
            if tmp_value == -1:
                tmp_optimality = 0
            else:
                tmp_optimality = calculate_optimality(value=tmp_value, best_value=benchmark[ordered_keys[file_id]])
            optimality_data.append(tmp_optimality)
        mean_optimality_data = np.mean(optimality_data)
        modified_means.append(mean_optimality_data)

    ax.bar(ind + i * bar_width, modified_means, bar_width, label=f'Key {i + 1}', color=next(colors))

ax.set_xlabel('Files')
ax.set_ylabel('Mean Values')
ax.set_title('Mean Values by File and Key')
ax.set_xticks(ind + bar_width * len(plot_data[0]) / 2 - bar_width / 2)
ax.set_xticklabels(group_labels)
ax.legend()

plt.tight_layout()
plt.show()