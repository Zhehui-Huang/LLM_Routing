import argparse
import copy
import sys

from others.utils import read_all_files, save_final_results
from others.tsp_1_verify_utils import (extract_solution_with_separation, verify_start_end_depot, verify_visit_city_once,
                                       verify_euclidean_dist, verify_visit_time_constraints, reflect_num,
                                       test_file_num, cities_5, cities_10, tsp_1_filter_files)

time_windows_5 = {
    1: (2, 10),
    2: (9, 12),
    3: (0, float('inf')),  # Depot
    4: (1, 20),
    5: (10, 15),
}

time_windows_10 = {
    1: (10, 18),
    2: (15, 30),
    3: (0, float('inf')),  # Depot
    4: (4, 8),
    5: (10, 30),
    6: (2, 10),
    7: (5, 20),
    8: (8, 14),  # Depot
    9: (1, 5),
    10: (10, 18),
}


def detailed_constraint_check(tours, robot_costs, cities, time_windows):
    all_contract_violated = ""
    # Check 1: Each robot starts and ends at the depot
    all_contract_violated += verify_start_end_depot(tours=tours)

    # Check 2: Each city must be visited exactly once
    all_contract_violated += verify_visit_city_once(tours=tours, cities=cities)

    # Check 3: Check Euclidean distance between cities for all robots
    all_contract_violated += verify_euclidean_dist(tours, cities, robot_costs)

    # Check 4: Time window constraints
    all_contract_violated += verify_visit_time_constraints(tours, time_windows, cities)

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
            time_windows = copy.deepcopy(time_windows_5)
        elif point_num == 10:
            cities = copy.deepcopy(cities_10)
            time_windows = copy.deepcopy(time_windows_10)
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
                                                                 cities=cities, time_windows=time_windows)

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
    parser.add_argument('--root_dir', type=str, default="evaluate/1_direct_reflect_ambiguities_v3_ambiguities/1-tsp/F-TSPTW", help="root_dir")
    args = parser.parse_args()
    sys.exit(main(root_dir=args.root_dir))