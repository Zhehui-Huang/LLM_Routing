import os
import random


def get_robot_info_str():
    # Robot info prex
    robot_info = '###\nRobot information\n===\nThere is one robot.\n'
    robot_info += '- The robot start at depot city 0. \n'
    robot_info += '- The robot can travel between any two cities. \n'
    robot_info += '- The travel cost is calculated as the Euclidean distance between the two cities.\n###\n\n'
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
    elif city_num == 15:
        k_list = [4, 6, 8, 10, 12]
    elif city_num == 20:
        k_list = [4, 7, 10, 13, 16]
    elif city_num == 25:
        k_list = [4, 8, 12, 16, 20]
    elif city_num == 50:
        k_list = [5, 15, 25, 35, 45]
    else:
        raise ValueError(f'Invalid city number: {city_num}')

    return k_list


def read_txt_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data


def write_txt_file(file_name, content):
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as f:
        f.write(content)
        print(f'Write problem description to {file_name}')
