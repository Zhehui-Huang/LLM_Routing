import os
import json
import sys

import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

benchmark_tsp_1_point_5 = {
    'A-TSP': 16.64,
    'B-BTSP': 6.40,
    'C-GTSP': 5.24,
    'D-OTSP': 16.64,
    'E-TPP': 241.21,
    'F-TSPTW': 17.51,
    'G-TSPM': 10,
    'H-TSPMDNC': 11.64,
    'I-TSPMDC': 20.79,
    'J-KTSP': 9.12,
}

benchmark_tsp_1_point_10 = {
    'A-TSP': 25.04,
    'B-BTSP': 5.0,
    'C-GTSP': 16.58,
    'D-OTSP': 28.12,
    'E-TPP': 580.29,
    'F-TSPTW': 26.45,
    'G-TSPM': 22,
    'H-TSPMDNC': 23.29,
    'I-TSPMDC': 27.64,
    'J-KTSP': 17.22,
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


def load_json_files(root_dir):
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


def prepare_plot_data(json_data, extracted_parts, benchmark):
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
                    print(f'extracted_parts[jid]: {extracted_parts[jid]}')
                    raise ValueError(f'any(x < tmp_bench for x in values): {values} < {tmp_bench}')

            mean = compute_mean(values)
            means.append(mean)
            raw_data.append(values)
        plot_data.append(means)
        raw_datas.append(raw_data)
    return plot_data, raw_datas


def main():
    points_list = [5, 10]
    for point_num in points_list:
        if point_num == 5:
            benchmark = benchmark_tsp_1_point_5
            root_dir = '/home/zhehui/LLM_Routing/final_results/back_1_tsp/1-tsp/5'
        elif point_num == 10:
            benchmark = benchmark_tsp_1_point_10
            root_dir = '/home/zhehui/LLM_Routing/final_results/back_1_tsp/1-tsp/10'
        else:
            raise ValueError(f'Invalid point number {point_num}')

        json_data, extracted_parts = load_json_files(root_dir=root_dir)
        plot_data, raw_datas = prepare_plot_data(json_data, extracted_parts, benchmark)

        group_labels = ['A-TSP', 'B-BTSP', 'C-GTSP', 'D-OTSP', 'E-TPP', 'F-TSPTW', 'G-TSPM', 'H-TSPMDNC', 'I-TSPMDC',
                        'J-KTSP', 'K-CTSP']
        # Dynamically set group labels based on the number of files
        group_labels = [group_labels[i] for i in range(len(json_data))]

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
                        tmp_optimality = calculate_optimality(value=tmp_value,
                                                              best_value=benchmark[ordered_keys[file_id]])

                        if tmp_optimality < 1:
                            tmp_optimality = 0

                    optimality_data.append(tmp_optimality)
                mean_optimality_data = np.mean(optimality_data)
                modified_means.append(mean_optimality_data)

            if i == 0:
                tmp_label = 'No Reflect'
            else:
                tmp_label = f'Reflect {i}'
            ax.bar(ind + i * bar_width, modified_means, bar_width, label=tmp_label, color=next(colors))

        ax.set_xlabel('Tasks')
        ax.set_ylabel('Optimality')
        ax.set_title(f'TSP for One Robot: {point_num} Points (Optimal Solutions)')
        ax.set_xticks(ind + bar_width * len(plot_data[0]) / 2 - bar_width / 2)
        ax.set_xticklabels(group_labels)
        ax.legend()

        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    sys.exit(main())
