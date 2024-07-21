import os
import numpy as np
import random
from task_info import a_tsp_task, b_btsp_task, c_gtsp_task


def get_cities(city_num):
    points = np.random.randint(0, 100, size=(city_num, 2))
    return points


def random_generate_cities_depot(city_num):
    # Randomly generate city_num cities. the location is: (x, y), x, y are integers between 0 and 100
    city_loc_list = get_cities(city_num=city_num)
    # Depot location
    depot_loc = city_loc_list[0]
    rest_cities_loc = city_loc_list[1:]
    return depot_loc, rest_cities_loc


def get_robot_info_str():
    # Robot info prex
    robot_info = '###\nRobot information\n===\nThere is one robot.\n'
    robot_info += '- The robot start at depot city 0. \n'
    robot_info += '- The robot can travel between any two cities. \n'
    robot_info += '- The travel cost is calculated as the Euclidean distance between the two cities. \n\n'
    return robot_info


def get_city_group_str(city_num, instance_id):
    tmp_city_id_list = [i for i in range(1, city_num)]
    random.shuffle(tmp_city_id_list)
    group_num = instance_id + 3
    groups_list = [[] for _ in range(group_num)]
    city_group_str = f"\nThere are {group_num} city groups: \n"

    for idx, city in enumerate(tmp_city_id_list):
        group_index = idx % group_num
        groups_list[group_index].append(city)

    for idx, group_item_list in enumerate(groups_list):
        group_item_list.sort()
        city_group_str += f"Group {idx}: ["
        for idy, group_item in enumerate(group_item_list):
            if idy == len(group_item_list) - 1:
                city_group_str += f"{group_item}"
            else:
                city_group_str += f"{group_item}, "

        city_group_str += ']\n'

    return city_group_str


def get_mvtsp_visit_num_str(city_num):
    visit_num_list = [random.randint(1, 3) for _ in range(city_num - 1)]
    visit_num_str = f"\nThe depot city can be visited any number of times. The rest of cities need to be visited the following number of times: \n"
    for i, num in enumerate(visit_num_list):
        visit_num_str += f"City {i + 1}: {num}\n"

    return visit_num_str


def write_city_info(depot_loc, rest_cities_loc, path):
    # save city location to file
    saved_list_str = f"{depot_loc[0]},{depot_loc[1]}\n"
    for i, point in enumerate(rest_cities_loc):
        saved_list_str += f"{point[0]},{point[1]}\n"

    # tmp_file_name = f'../city_list/single/{task_name}/city_{city_num}_instance_{instance_id}.txt'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(saved_list_str)


def get_ktsp_k_list(city_num):
    if city_num == 10:
        k_list = [4, 5, 6, 7, 8]
    elif city_num == 25:
        k_list = [4, 8, 12, 16, 20]
    elif city_num == 50:
        k_list = [5, 15, 25, 35, 45]
    else:
        raise ValueError(f'Invalid city number: {city_num}')

    return k_list

