import os
import sys

from env_info import get_multi_env_info_str
from task_info import get_multi_task_info
from utils import get_ktsp_k_list, read_txt_file, write_txt_file
from multi_utils import get_multi_robot_info_str, modify_mTSPMD_info, extract_robot_num, extract_demand_info, FILE_NAME_SMALL, FILE_NAME_BIG


TASK_LIST = ['mTSP', 'mTSP_MinMax', 'mTSPMD', 'CVRP']


def get_format_requirements(task_name):
    if task_name == 'mTSPMD':
        format_requirements = (
            '###\n'
            'Format requirements\n'
            '===\n'
            '1) Please output the tours for each robot as a list of city indices. Each tour should start and end at its assigned depot.\n'
            '2) Please output the total travel cost for each tour and the overall total travel cost.\n\n'
            'For example, if there are two robots with the following tours and costs:\n'
            'Robot 1 (Depot 0): 0 -> 1 -> 2 -> 0 with a travel cost of 50\n'
            'Robot 2 (Depot 3): 3 -> 4 -> 5 -> 3 with a travel cost of 60\n'
            'then the output should be:\n\n'
            'Robot 1 Tour: [0, 1, 2, 0]\n'
            'Robot 1 Total Travel Cost: 50\n\n'
            'Robot 2 Tour: [3, 4, 5, 3]\n'
            'Robot 2 Total Travel Cost: 60\n\n'
            'Overall Total Travel Cost: 110\n'
            '###'
        )
    elif task_name == 'mTSP_MinMax':
        format_requirements = (
            '###\n'
            'Format requirements\n'
            '===\n'
            '1) Please output the tours for each robot as a list of city indices. Each tour should start and end at the depot city 0.\n'
            '2) Please output the travel cost for each tour and the maximum travel cost among all tours.\n\n'
            'For example, if there are two robots with the following tours and costs:\n'
            'Robot 1: 0 -> 1 -> 2 -> 0 with a travel cost of 50\n'
            'Robot 2: 0 -> 3 -> 4 -> 0 with a travel cost of 60\n'
            'then the output should be:\n\n'
            'Robot 1 Tour: [0, 1, 2, 0]\n'
            'Robot 1 Total Travel Cost: 50\n\n'
            'Robot 2 Tour: [0, 3, 4, 0]\n'
            'Robot 2 Total Travel Cost: 60\n\n'
            'Maximum Travel Cost: 60\n'
            '###'
        )
    elif task_name == 'CVRP':
        format_requirements = (
            '###\n'
            'Format Requirements\n'
            '===\n'
            '1) Please output the tours for each robot as a list of city indices. Each tour should start and end at the depot city 0.\n'
            '2) Please output the total travel cost for each tour and the overall total travel cost.\n'
            '3) Ensure that the demand of each city is met and the capacity constraints of each robot are not violated.\n\n'
            'For example, if there are two robots with the following tours and costs:\n'
            'Robot 1: 0 -> 1 -> 2 -> 0 with a travel cost of 50\n'
            'Robot 2: 0 -> 3 -> 4 -> 0 with a travel cost of 60\n'
            'then the output should be:\n\n'
            'Robot 1 Tour: [0, 1, 2, 0]\n'
            'Robot 1 Total Travel Cost: 50\n\n'
            'Robot 2 Tour: [0, 3, 4, 0]\n'
            'Robot 2 Total Travel Cost: 60\n\n'
            'Overall Total Travel Cost: 110\n'
            '###'
        )
    else:
        format_requirements = (
            '###\n'
            'Format requirements\n'
            '===\n'
            '1) Please output the tours for each robot as a list of city indices. Each tour should start and end at the depot city 0.\n'
            '2) Please output the total travel cost for each tour and the overall total travel cost.\n\n'
            'For example, if there are two robots with the following tours and costs:\n'
            'Robot 1: 0 -> 1 -> 2 -> 0 with a travel cost of 50\n'
            'Robot 2: 0 -> 3 -> 4 -> 0 with a travel cost of 60\n'
            'then the output should be:\n\n'
            'Robot 1 Tour: [0, 1, 2, 0]\n'
            'Robot 1 Total Travel Cost: 50\n\n'
            'Robot 2 Tour: [0, 3, 4, 0]\n'
            'Robot 2 Total Travel Cost: 60\n\n'
            'Overall Total Travel Cost: 110\n'
            '###'
        )

    return format_requirements


def problem_generation(file_names, note):
    for file_name in file_names:
        # Generate problem description
        for task_name in TASK_LIST:
            print(f'{task_name} with {file_name}')

            # 1. Get environment information
            extra_env_info_str = ''
            if task_name == 'CVRP':
                original_info = read_txt_file(f'../city_list/multiple/demand/{note}/{file_name}.txt')
            else:
                original_info = read_txt_file(f'../city_list/multiple/processed/{note}/{file_name}.txt')

            # Get robot number
            robot_num = extract_robot_num(filename=file_name + '.txt')
            if task_name == 'mTSPMD':
                original_info = modify_mTSPMD_info(content=original_info, robot_num=robot_num)

            env_info_str = get_multi_env_info_str(original_info=original_info, extra_env_info_str=extra_env_info_str)

            # 2. Get robot information
            robot_info_str = get_multi_robot_info_str(task_name=task_name, robot_num=robot_num, file_name=file_name, note=note)

            # 3. Get task information
            task_info_str = get_multi_task_info(task_name=task_name)

            # 4. Get format requirements
            format_requirements_str = get_format_requirements(task_name=task_name)
            problem_description_str = env_info_str + robot_info_str + task_info_str + format_requirements_str

            tmp_file_name = f'../task/multiple/{note}/{task_name}/{file_name}.txt'
            write_txt_file(file_name=tmp_file_name, content=problem_description_str)


def main():
    problem_generation(file_names=FILE_NAME_SMALL, note='small')
    problem_generation(file_names=FILE_NAME_BIG, note='big')


if __name__ == '__main__':
    sys.exit(main())