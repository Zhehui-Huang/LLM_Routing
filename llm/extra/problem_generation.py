import os
import sys

from env_info import get_env_info_str
from task_info import get_task_info
from utils import get_robot_info_str, random_generate_cities_depot, get_city_group_str, write_city_info, get_ktsp_k_list, get_mvtsp_visit_num_str


CITY_NUM_LIST = [10, 25, 50]
INSTANCE_NUM = 5
# TASK_LIST = ['TSP', 'BTSP', 'GTSP', 'KTSP', 'MV-TSP', 'TPP']
TASK_LIST = ['TSP', 'BTSP', 'GTSP', 'KTSP', 'MV-TSP']


def get_format_requirements(task_name):
    # Format requirements
    if task_name == 'BTSP':
        format_requirements = (
            'Format requirements\n'
            '===\n'
            '1) Please output the tour as a list of city indices. The tour should start and end at the depot city 0.\n'
            '2) Please output the total travel cost of the tour.\n'
            '3) Please output the maximum distance between any two consecutive cities in the tour.\n\n'
            'For example, if the tour is 0 -> 1 -> 2 -> 3 -> 0, the total travel cost is 100, and the maximum distance between any two consecutive cities is 40, '
            'then the output should be: \n\n'
            'Tour: [0, 1, 2, 3, 0]\n'
            'Total travel cost: 100\n'
            'Maximum distance between consecutive cities: 40\n\n'
            '###'
        )
    else:
        format_requirements = (
            'Format requirements\n'
            '===\n'
            '1) Please output the tour as a list of city indices. The tour should start and end at the depot city 0.\n'
            '2) Please output the total travel cost of the tour.\n\n'
            'For example, if the tour is 0 -> 1 -> 2 -> 3 -> 0 and the total travel cost is 100, '
            'then the output should be: \n\n'
            'Tour: [0, 1, 2, 3, 0]\n'
            'Total travel cost: 100\n\n'
            '###'
        )
    return format_requirements


def problem_generation():
    for city_num in CITY_NUM_LIST:
        for instance_id in range(INSTANCE_NUM):
            depot_loc, rest_cities_loc = random_generate_cities_depot(city_num=city_num)

            # Write city info to file
            path = f'../city_list/single/city_{city_num}_instance_{instance_id}.txt'
            write_city_info(depot_loc, rest_cities_loc, path)

            # Generate problem description
            for task_name in TASK_LIST:
                print(f'{task_name} with {city_num} cities, instance {instance_id}')

                # 1. Get environment information
                extra_env_info_str = ''
                if task_name == 'GTSP':
                    extra_env_info_str = get_city_group_str(city_num, instance_id)
                elif task_name == 'MV-TSP':
                    extra_env_info_str = get_mvtsp_visit_num_str(city_num)

                env_info_str = get_env_info_str(city_num=city_num, instance_id=instance_id, task_name=task_name,
                                                depot_loc=depot_loc, rest_cities_loc=rest_cities_loc,
                                                extra_env_info_str=extra_env_info_str)

                # 2. Get robot information
                robot_info_str = get_robot_info_str()

                # 3. Get task information
                if task_name == 'KTSP':
                    k_list = get_ktsp_k_list(city_num=city_num)
                    task_info_str = get_task_info(task_name=task_name, k=k_list[instance_id])
                else:
                    task_info_str = get_task_info(task_name=task_name)

                # 4. Get format requirements
                format_requirements_str = get_format_requirements(task_name=task_name)

                problem_description_str = env_info_str + robot_info_str + task_info_str + format_requirements_str
                file_name = f'../task/single/{task_name}/city_{city_num}_instance_{instance_id}.txt'
                os.makedirs(os.path.dirname(file_name), exist_ok=True)
                with open(file_name, 'w') as f:
                    f.write(problem_description_str)
                    print(f'Write problem description to {file_name}')


def main():
    problem_generation()


if __name__ == '__main__':
    sys.exit(main())
