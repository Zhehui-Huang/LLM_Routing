import os
import json
import numpy as np
import matplotlib.pyplot as plt


def read_all_json_files(root_directory):
    # List to hold the contents of all text files
    text_files_loc = []

    # Walk through the directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.json'):
                # Construct the full file path
                file_path = os.path.join(dirpath, filename)
                text_files_loc.append(file_path)

    text_files_loc.sort()
    return text_files_loc


def load_json_files():
    root_dir = '/home/zhehui/LLM_Routing/final_results/1_direct_reflect_v3/4-tsp/test'
    text_files_loc = read_all_json_files(root_directory=root_dir)

    json_datas = []
    for file_path in text_files_loc:
        with open(file_path, "r") as file:
            data = json.load(file)
            json_datas.append(data)

    return json_datas


# Function to load and parse JSON files
# def load_json_files(file_paths):
#     json_data = []
#     for path in file_paths:
#         with open(path, 'r') as file:
#             json_data.append(json.load(file))
#     return json_data

# Function to compute the mean, replacing -1 with 0
def compute_mean(values):
    values = [0 if v == -1 else v for v in values]
    return np.mean(values)


# Function to prepare data for plotting
def prepare_plot_data(json_data):
    plot_data = []
    for file in json_data:
        means = []
        for key in file.keys():
            values = list(file[key].values())
            mean = compute_mean(values)
            means.append(mean)
        plot_data.append(means)
    return plot_data


json_data = load_json_files()
plot_data = prepare_plot_data(json_data)

# Plotting
colors = ['blue', 'orange', 'green', 'red']
group_labels = ['File A', 'File B', 'File C']
fig, ax = plt.subplots(figsize=(12, 8))

ind = np.arange(len(group_labels))
bar_width = 0.2

for i in range(len(plot_data[0])):
    means = [plot_data[j][i] for j in range(len(plot_data))]
    ax.bar(ind + i * bar_width, means, bar_width, label=f'Key {i}', color=colors[i])

ax.set_xlabel('Files')
ax.set_ylabel('Mean Values')
ax.set_title('Mean Values by File and Key')
ax.set_xticks(ind + bar_width / 2)
ax.set_xticklabels(group_labels)
ax.legend()

plt.tight_layout()
plt.show()
