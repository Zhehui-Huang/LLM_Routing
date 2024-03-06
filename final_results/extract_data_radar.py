import json
import os
import sys

import numpy as np

from final_results.plot_utils import (read_all_json_files, benchmark_tsp_1_point_5, benchmark_tsp_1_point_10,
                                      benchmark_tsp_4_point_10)


def calculate_results(obj, best_value, plot_metric):
    if isinstance(obj, dict):
        for k, v in obj.items():
            obj[k] = calculate_results(v, best_value, plot_metric)
    elif isinstance(obj, list):
        obj = [calculate_results(item, best_value, plot_metric) for item in obj]
    elif isinstance(obj, (int, float)):
        if obj < 0:
            return 0.0
        else:
            if plot_metric == 'feasible':
                return round(best_value / obj, 2)
            elif plot_metric == 'optimal':
                if np.round(best_value / obj, 2) == 1.0:
                    return 1.0
                else:
                    return 0.0
            elif plot_metric == 'efficient':
                if np.round(best_value / obj, 2) > 0.0:
                    return 1.0
                else:
                    raise ValueError(f'np.round(best_value / obj, 2) > 0.0: {np.round(best_value / obj, 2)}')
                    # return 0.0

    return obj


def get_llm_name(type_folder):
    if 'gemini' in type_folder:
        llm_name = 'gemini'
    else:
        llm_name = 'gpt'
    return llm_name


def get_benchmark(tsp_type, point_num):
    if tsp_type == '1-tsp' and point_num == '5':
        benchmark = benchmark_tsp_1_point_5
    elif tsp_type == '1-tsp' and point_num == '10':
        benchmark = benchmark_tsp_1_point_10
    elif tsp_type == '4-tsp' and point_num == '10':
        benchmark = benchmark_tsp_4_point_10
    else:
        raise ValueError(f'Unknown task: {tsp_type}_{point_num}')

    return benchmark


def recalculate_file(file_path, llm_name, type_folder, path_item, name_label, plot_metric):
    with open(file_path, 'r') as file:
        data = json.load(file)

    task_name = path_item[-1].split('.')[0]
    benchmark = get_benchmark(tsp_type=path_item[-3], point_num=path_item[-2])

    # Recalculate
    data = calculate_results(obj=data, best_value=benchmark[task_name], plot_metric=plot_metric)


    # Get average
    data_averages = {}
    for outer_key, nested_dict in data.items():
        tmp_value_list = []
        for value in nested_dict.values():
            tmp_value_list.append(value)
        data_averages[outer_key] = np.mean(tmp_value_list)

    # Save
    tmp_task_name = path_item[3][:-5]
    real_task_name = name_label[tmp_task_name]
    save_file_path = f'plot_data/{llm_name}_{type_folder}/{plot_metric}/{path_item[1]}/{path_item[2]}/{real_task_name}.json'
    directory = os.path.dirname(save_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(save_file_path, 'w') as file:
        json.dump(data_averages, file, indent=4)
    return directory


def extract_data_radar(folder_path, name_label, plot_metric):
    # Load the JSON data from the file
    text_files_loc = read_all_json_files(root_directory=folder_path)
    print('file number:', len(text_files_loc), sep='\n')
    save_folder_path = None
    for file_loc in text_files_loc:
        path_item = file_loc.split('/')
        type_folder = path_item[0]
        llm_name = get_llm_name(type_folder=type_folder)

        save_folder_path = recalculate_file(file_path=file_loc, llm_name=llm_name, type_folder=type_folder,
                                            path_item=path_item, name_label=name_label, plot_metric=plot_metric)

    print('Success: Extract Data!!!')
    return save_folder_path


def main():
    save_folder_path = extract_data_radar(folder_path='z_v2_fix_bug_1_direct_reflect_v3/1-tsp/5')


if __name__ == '__main__':
    sys.exit(main())
