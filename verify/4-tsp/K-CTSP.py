import argparse
import sys

from utils import read_all_files, save_final_results
from verify_utils import extract_solution_with_separation, verify_start_end_depot, verify_visit_city_once, \
    verify_num_robots, verify_euclidean_dist, verify_color_match

# Define city coordinates with city index starting from 1
cities = {
    1: (9, 4),
    2: (4, 6),
    3: (4, 4),  # Depot
    4: (3, 4),
    5: (4, 8),
    6: (4, 3),
    7: (7, 5),
    8: (5, 0),
    9: (1, 5),
    10: (9, 3)
}

city_colors = {
    1: ['red', 'green'],
    2: ['yellow', 'blue'],
    3: ['red', 'green', 'yellow', 'blue'],  # Depot
    4: ['red'],
    5: ['green'],
    6: ['yellow'],
    7: ['blue'],
    8: ['red', 'blue'],
    9: ['yellow', 'green'],
    10: ['yellow']
}

# Robots and their colors
robot_colors = {
    1: 'red',
    2: 'yellow',
    3: 'green',
    4: 'blue'
}

reflect_num = 4
test_file_num = 3


def detailed_constraint_check(tours: dict, robot_costs: dict) -> str:
    all_contract_violated = ""
    # Check 1: Each robot starts and ends at the depot
    all_contract_violated += verify_start_end_depot(tours=tours)

    # Check 2: Each city must be visited exactly once
    all_contract_violated += verify_visit_city_once(tours=tours, cities=cities)

    # Check 3: Number of robots
    all_contract_violated += verify_num_robots(tours=tours)

    # Check 4: Check Euclidean distance between cities for all robots
    all_contract_violated += verify_euclidean_dist(tours, cities, robot_costs)

    # Check 5: Check color match
    all_contract_violated += verify_color_match(robot_tours=tours, city_colors=city_colors, robot_colors=robot_colors)

    if all_contract_violated != "":
        return all_contract_violated
    else:
        # If all checks pass
        return "** YES!!! **"


def main(root_dir=""):
    valid_final_cost = {}
    tmp_file_name = root_dir[9:]
    text_files_loc = read_all_files(root_directory=root_dir)
    print('file number:', len(text_files_loc), sep='\n')

    for i in range(reflect_num):
        valid_final_cost[i] = {j: -1 for j in range(test_file_num)}

    for file_path in text_files_loc:
        # print('file_path: ', file_path, '\n')
        robot_tours, robot_costs, final_cost, _ = extract_solution_with_separation(file_path=file_path)
        # print(robot_tours)
        # print(robot_costs)
        # Running the detailed constraint check on the provided solution
        constraint_check_message = detailed_constraint_check(robot_tours, robot_costs)

        if constraint_check_message == "** YES!!! **":
            # print('file_path: ', file_path, '\n')
            reflect_id = int(file_path.split('/')[4].split('_')[1])
            file_id = int(file_path.split('/')[5].split('.')[0][-1])

            for i in range(reflect_id, reflect_num):
                valid_final_cost[i][file_id] = final_cost
        else:
            continue
            # print(
            #     '====================================================================================================')
            # print('file_path: ', file_path, '\n')
            # print(constraint_check_message)
            # print(
            #     '====================================================================================================')

    print('valid_final_cost:', valid_final_cost, sep='\n')

    save_final_results(dir_path=tmp_file_name, result_content=valid_final_cost)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run main function with parameters.")
    parser.add_argument('--root_dir', type=str, default="", help="root_dir")
    args = parser.parse_args()
    sys.exit(main(root_dir=args.root_dir))