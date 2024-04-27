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


def make_radar_plot(folder_path, plot_metric, prex, math_path, external_path, math_external_path):
    text_files_loc = read_all_json_files(root_directory=folder_path)
    data = read_data(text_files_loc)

    math_text_files_loc = read_all_json_files(root_directory=math_path)
    math_data = read_data(math_text_files_loc)

    external_text_files_loc = read_all_json_files(root_directory=external_path)
    external_data = read_data(external_text_files_loc)

    math_external_text_files_loc = read_all_json_files(root_directory=math_external_path)
    math_external_data = read_data(math_external_text_files_loc)

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
    colors = ['#7244cd', '#377eb8', '#ff7f00', '#60bc2c']  #

    #
    key = '0'
    values = [d[key] for d in math_external_data]
    values += values[:1]  # Complete the loop
    ax.plot(angles, values, 'o-', linewidth=2 + 0.5 * 0, label='Math + External', color=colors[0])
    ax.fill(angles, values, alpha=0.25 + 0.1 * 0, color=colors[0])

    values = [d[key] for d in math_data]
    values += values[:1]  # Complete the loop
    ax.plot(angles, values, 'o-', linewidth=2 + 0.5 * 1, label='Math', color=colors[1])
    ax.fill(angles, values, alpha=0.25 + 0.1 * 1, color=colors[1])

    values = [d[key] for d in external_data]
    values += values[:1]  # Complete the loop
    ax.plot(angles, values, 'o-', linewidth=2 + 0.5 * 2, label='NL + External', color=colors[2])
    ax.fill(angles, values, alpha=0.25 + 0.1 * 2, color=colors[2])


    values = [d[key] for d in data]
    values += values[:1]  # Complete the loop
    ax.plot(angles, values, 'o-', linewidth=2 + 0.5 * 3, label='NL', color=colors[3])
    ax.fill(angles, values, alpha=0.25 + 0.1 * 3, color=colors[3])

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
    else:
        raise ValueError(f'Unknown plot_metric: {plot_metric}')

    # title = f"{tmp_title} of {split_folder[3][0]} robot, {split_folder[4]} points"
    # plt.title(title)
    # plt.show()
    file_name = f"plots/compare/{tmp_title}/{split_folder[3][0]}_{split_folder[4]}.pdf"
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
    math_ori_foler_path_list = [
        'z_v2_fix_bug_2_math_reflect_v3/1-tsp/5',
        'z_v2_fix_bug_2_math_reflect_v3/1-tsp/10',
        'z_v2_fix_bug_2_math_reflect_v3/4-tsp/10',
    ]
    external_ori_foler_path_list = [
        'z_v2_fix_bug_5_external_tools_direct_v3/1-tsp/5',
        'z_v2_fix_bug_5_external_tools_direct_v3/1-tsp/10',
        'z_v2_fix_bug_5_external_tools_direct_v3/4-tsp/10',
    ]
    math_external_ori_foler_path_list = [
        'z_v2_fix_bug_5_external_tools_math_v3/1-tsp/5',
        'z_v2_fix_bug_5_external_tools_math_v3/1-tsp/10',
        'z_v2_fix_bug_5_external_tools_math_v3/4-tsp/10',
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
            math_save_folder_path = extract_data_radar(folder_path=math_ori_foler_path_list[f_id],
                                                       name_label=name_label, plot_metric=plot_metric)

            external_save_folder_path = extract_data_radar(folder_path=external_ori_foler_path_list[f_id],
                                                           name_label=name_label, plot_metric=plot_metric)

            math_external_save_folder_path = extract_data_radar(folder_path=math_external_ori_foler_path_list[f_id],
                                                                name_label=name_label, plot_metric=plot_metric)

            make_radar_plot(folder_path=save_folder_path, plot_metric=plot_metric, prex=split_path[0],
                            math_path=math_save_folder_path, external_path=external_save_folder_path,
                            math_external_path=math_external_save_folder_path)


if __name__ == '__main__':
    sys.exit(main())
