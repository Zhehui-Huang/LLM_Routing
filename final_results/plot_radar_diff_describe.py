import json
import os
import sys

import matplotlib.pyplot as plt
import numpy as np

from final_results.extract_data_radar import extract_data_radar
from final_results.plot_utils import (read_all_json_files, tsp_1_name_label, tsp_4_name_label)


# Read data from JSON files
def read_data(files):
    data = []
    for file in files:
        with open(file, 'r') as f:
            data.append(json.load(f))
    return data


def make_radar_plot(folder_path, plot_metric, prex, concise_path):
    text_files_loc = read_all_json_files(root_directory=folder_path)
    data = read_data(text_files_loc)

    concise_text_files_loc = read_all_json_files(root_directory=concise_path)
    concise_data = read_data(concise_text_files_loc)

    labels = []
    for file_loc in text_files_loc:
        if file_loc.split('/')[-1][:-5][0] == '0':
            labels.append(file_loc.split('/')[-1][1:-5])
        else:
            labels.append(file_loc.split('/')[-1][:-5])

    keys = []
    for k in data[0].keys():
        if int(k) % 6 == 0 and int(k) > 0:
            keys.append(str(k))

    # labels = np.array(['G', 'H', 'J'])
    num_vars = len(labels)

    # Calculate angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Complete the loop

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    # Adjust the start angle so the first axis is at the left and reverse the direction
    # ax.set_theta_offset(np.pi)
    # ax.set_theta_direction(-1)

    # colors = plt.cm.viridis(np.linspace(0, 1, len(keys)))
    colors = ['#f4e13b', '#ff7f00', '#60bc2c']  # '#7244cd'

    print('plot_metric', plot_metric)
    tt_path = folder_path.split('/')
    print('type: ', f'{tt_path[-2]}_{tt_path[-1]}')
    print('=========================')

    #
    key = '6'
    values = [d[key] for d in concise_data]
    values += values[:1]  # Complete the loop
    ax.plot(angles, values, 'o-', linewidth=2 + 0.5 * 0, label='Concise', color=colors[1])
    ax.fill(angles, values, alpha=0.25 + 0.1 * 0, color=colors[1])

    print('Concise: ', values[:-1])
    print('Avg Concise: ', np.mean(values[:-1]))

    values = [d[key] for d in data]
    values += values[:1]  # Complete the loop
    ax.plot(angles, values, 'o-', linewidth=2 + 0.5 * 1, label='Detailed', color=colors[2])
    ax.fill(angles, values, alpha=0.25 + 0.1 * 2, color=colors[2])
    print('Detailed: ', values[:-1])
    print('Avg Detailed: ', np.mean(values[:-1]))
    print('***********************************************************')

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=7)
    split_folder = folder_path.split('/')
    if plot_metric == 'feasible':
        tmp_title = 'Feasibility'
    elif plot_metric == 'optimal':
        tmp_title = 'Optimality'
    elif plot_metric == 'efficient':
        tmp_title = 'Efficiency'

    title = f"{tmp_title} of {split_folder[3][0]} robot, {split_folder[4]} points"
    # plt.title(title)
    # plt.show()
    file_name = f"plots/diff_describe/{tmp_title}/{split_folder[3][0]}_{split_folder[4]}.pdf"
    directory = os.path.dirname(file_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.savefig(file_name)

def main():
    ori_foler_path_list = [
        'z_v2_fix_bug_1_direct_reflect_v3/1-tsp/5',
        'z_v2_fix_bug_1_direct_reflect_v3/1-tsp/10',
        'z_v2_fix_bug_1_direct_reflect_v3/4-tsp/10',
    ]
    concise_foler_path_list = [
        'z_v2_fix_bug_1_direct_reflect_ambiguities_v3_ambiguities/1-tsp/5',
        'z_v2_fix_bug_1_direct_reflect_ambiguities_v3_ambiguities/1-tsp/10',
        'z_v2_fix_bug_1_direct_reflect_ambiguities_v3_ambiguities/4-tsp/10',
    ]
    for f_id, ori_folder_path in enumerate(ori_foler_path_list):
        # ori_folder_path = 'z_v2_fix_bug_1_direct_reflect_v3/1-tsp/5'
        split_path = ori_folder_path.split('/')
        if split_path[-2] == '1-tsp':
            name_label = tsp_1_name_label
        elif split_path[-2] == '4-tsp':
            name_label = tsp_4_name_label
        else:
            raise ValueError(f'Unknown task: {split_path[-2]}')

        plot_metric_list = ['feasible', 'optimal', 'efficient']
        for plot_metric in plot_metric_list:
            save_folder_path = extract_data_radar(folder_path=ori_folder_path, name_label=name_label,
                                                  plot_metric=plot_metric)
            concise_save_folder_path = extract_data_radar(folder_path=concise_foler_path_list[f_id],
                                                          name_label=name_label, plot_metric=plot_metric)
            # 'plot_data/gpt_z_v2_fix_bug_1_direct_reflect_v3/feasible/1-tsp/5'
            make_radar_plot(folder_path=save_folder_path, plot_metric=plot_metric, prex=split_path[0],
                            concise_path=concise_save_folder_path)


if __name__ == '__main__':
    sys.exit(main())