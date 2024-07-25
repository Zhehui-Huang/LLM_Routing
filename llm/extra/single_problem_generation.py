import os
import sys

from env_info import get_env_info_str
from task_info import get_task_info
from utils import get_robot_info_str, get_city_group_str, get_ktsp_k_list, get_mvtsp_visit_num_str

CITY_NUM_LIST = [10, 15, 20]
INSTANCE_NUM = 5
# TASK_LIST = ['TSP', 'BTSP', 'GTSP', 'KTSP', 'MV-TSP', 'TPP']
TASK_LIST = ['TSP', 'BTSP', 'GTSP', 'KTSP']


def get_format_requirements(task_name):
    # Format requirements
    if task_name == 'BTSP':
        format_requirements = (
            '###\n'
            'Format requirements\n'
            '===\n'
            '1) Please output the tour as a list of city indices. The tour should start and end at the depot city 0.\n'
            '2) Please output the total travel cost of the tour.\n'
            '3) Please output the maximum distance between any two consecutive cities in the tour.\n\n'
            'For example, if the tour is 0 -> 1 -> 2 -> 3 -> 0, the total travel cost is 100, and the maximum distance between any two consecutive cities is 40, '
            'then the output should be: \n\n'
            'Tour: [0, 1, 2, 3, 0]\n'
            'Total travel cost: 100\n'
            'Maximum distance between consecutive cities: 40\n'
            '###'
        )
    else:
        format_requirements = (
            '###\n'
            'Format requirements\n'
            '===\n'
            '1) Please output the tour as a list of city indices. The tour should start and end at the depot city 0.\n'
            '2) Please output the total travel cost of the tour.\n\n'
            'For example, if the tour is 0 -> 1 -> 2 -> 3 -> 0 and the total travel cost is 100, '
            'then the output should be: \n\n'
            'Tour: [0, 1, 2, 3, 0]\n'
            'Total travel cost: 100\n'
            '###'
        )
    return format_requirements


def get_city_loc(city_list_path):
    with open(city_list_path, 'r') as f:
        lines = f.readlines()
        depot_loc = [int(x) for x in lines[0].strip().split(',')]
        rest_cities_loc = [[int(x) for x in line.strip().split(',')] for line in lines[1:]]

    return depot_loc, rest_cities_loc


def problem_generation(shot_type, vid=0):
    for city_num in CITY_NUM_LIST:
        for instance_id in range(INSTANCE_NUM):
            city_list_path = f'../city_list/single/city_{city_num}_instance_{instance_id}.txt'
            depot_loc, rest_cities_loc = get_city_loc(city_list_path=city_list_path)

            # Generate problem description
            for task_name in TASK_LIST:
                print(f'{task_name} with {city_num} cities, instance {instance_id}')

                # 1. Get environment information
                extra_env_info_str = ''
                if task_name == 'GTSP':
                    extra_env_info_str = get_city_group_str(city_num=city_num, instance_id=instance_id, shot_type=shot_type)
                elif task_name == 'MV-TSP':
                    extra_env_info_str = get_mvtsp_visit_num_str(city_num)

                env_info_str = get_env_info_str(city_num=city_num, depot_loc=depot_loc, rest_cities_loc=rest_cities_loc,
                                                extra_env_info_str=extra_env_info_str)

                # 2. Get robot information
                robot_info_str = get_robot_info_str()

                # 3. Get task information
                if shot_type == 'zero':
                    file_path = ''
                elif shot_type == 'math':
                    file_path = f'../../algorithms/{task_name}-algorithm1.txt'
                elif shot_type == 'pseudo-code':
                    file_path = f'../../algorithms/{task_name}-algorithm{vid}.txt'
                else:
                    raise ValueError(f'Invalid shot type: {shot_type}')

                if task_name == 'KTSP':
                    k_list = get_ktsp_k_list(city_num=city_num)
                    task_info_str = get_task_info(task_name=task_name, k=k_list[instance_id], shot_type=shot_type,
                                                  file_path=file_path)
                else:
                    task_info_str = get_task_info(task_name=task_name, shot_type=shot_type, file_path=file_path)

                # 4. Get format requirements
                format_requirements_str = get_format_requirements(task_name=task_name)

                problem_description_str = env_info_str + robot_info_str + task_info_str + format_requirements_str

                if vid == 0:
                    file_name = f'../task/{shot_type}/single/{task_name}/city_{city_num}_instance_{instance_id}.txt'
                else:
                    file_name = f'../task/{shot_type}_v{vid}/single/{task_name}/city_{city_num}_instance_{instance_id}.txt'

                os.makedirs(os.path.dirname(file_name), exist_ok=True)
                with open(file_name, 'w') as f:
                    f.write(problem_description_str)
                    print(f'Write problem description to {file_name}')


def main():
    # Zero-shot
    problem_generation(shot_type='zero')

    # Use math formulation as context
    problem_generation(shot_type='math')

    # Use pseudo-code of a approximation algorithm as context
    problem_generation(shot_type='pseudo-code', vid=2)
    problem_generation(shot_type='pseudo-code', vid=3)

    # Use paper pdf file as context
    # problem_generation(shot_type='pdf_paper')


if __name__ == '__main__':
    sys.exit(main())
