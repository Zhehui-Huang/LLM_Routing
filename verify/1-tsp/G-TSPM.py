import argparse
import copy
import sys

from others.utils import read_all_files, save_final_results
from others.tsp_1_verify_utils import (extract_solution_with_separation, verify_start_end_depot,
                                       verify_city_visitation_at_least_once, verify_dist_given_matrix,
                                       reflect_num, test_file_num, cities_5, cities_10, tsp_1_filter_files)

distance_matrix_5 = [
    [0, 2, 3, 7, 2],
    [3, 0, 5, 3, 2],
    [2, 4, 0, 5, 3],
    [2, 1, 2, 0, 1],
    [6, 3, 2, 3, 0],
]

distance_matrix_10 = [
    [0, 4, 8, 5, 7, 2, 3, 9, 8, 5],
    [4, 0, 8, 3, 6, 5, 2, 8, 6, 2],
    [5, 1, 0, 6, 9, 1, 10, 3, 7, 4],
    [9, 3, 5, 0, 7, 4, 9, 7, 2, 4],
    [9, 2, 10, 9, 0, 5, 2, 4, 7, 8],
    [3, 1, 4, 2, 8, 0, 2, 5, 6, 10],
    [4, 6, 2, 4, 2, 10, 0, 8, 7, 9],
    [8, 5, 2, 5, 8, 10, 9, 0, 1, 9],
    [7, 9, 8, 1, 8, 8, 3, 1, 0, 3],
    [3, 1, 5, 10, 7, 10, 9, 7, 9, 0],
]


# Detailed constraint check function
def detailed_constraint_check(tours, robot_costs, cities, distance_matrix):
    all_contract_violated = ""
    # Check 1: Each robot starts and ends at the depot
    all_contract_violated += verify_start_end_depot(tours=tours)
    if all_contract_violated != "":
        return all_contract_violated
    # Check 2: Each city must be visited at least one robot one time
    all_contract_violated += verify_city_visitation_at_least_once(tours=tours, cities=cities)
    if all_contract_violated != "":
        return all_contract_violated
    # Check 3: Check distance between cities for all robots (distance matrix)
    # all_contract_violated += verify_euclidean_dist(tours, cities, robot_costs)
    all_contract_violated += verify_dist_given_matrix(tours, distance_matrix, robot_costs)

    if all_contract_violated != "":
        return all_contract_violated
    else:
        # If all checks pass
        return "** YES!!! **"


def main(root_dir=""):
    valid_final_cost = {}
    tmp_file_name = root_dir[9:]
    # root_dir = '../../evaluate/' + tmp_file_name
    unfiltered_text_files_loc = read_all_files(root_directory=root_dir)
    print('file number:', len(unfiltered_text_files_loc))
    file_groups = tsp_1_filter_files(unfiltered_text_files_loc)

    for point_num in file_groups.keys():
        point_num = int(point_num)
        if point_num == 5:
            cities = copy.deepcopy(cities_5)
            distance_matrix = copy.deepcopy(distance_matrix_5)
        elif point_num == 10:
            cities = copy.deepcopy(cities_10)
            distance_matrix = copy.deepcopy(distance_matrix_10)
        else:
            raise ValueError(f'Invalid point number {point_num}')

        for i in range(reflect_num):
            valid_final_cost[i] = {j: -1 for j in range(test_file_num)}

        for file_path in file_groups[str(point_num)]:
            # print('file_path: ', file_path, '\n')
            robot_tours, robot_costs, final_cost, _ = extract_solution_with_separation(file_path=file_path)
            # print(robot_tours)
            # print(robot_costs)
            # Running the detailed constraint check on the provided solution
            constraint_check_message = detailed_constraint_check(tours=robot_tours, robot_costs=robot_costs,
                                                                 cities=cities, distance_matrix=distance_matrix)

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

        save_final_results(dir_path=tmp_file_name, result_content=valid_final_cost, point_num=point_num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run main function with parameters.")
    parser.add_argument('--root_dir', type=str, default="evaluate/5_external_tools_direct_v3/1-tsp/G-TSPM", help="root_dir")
    args = parser.parse_args()
    sys.exit(main(root_dir=args.root_dir))
