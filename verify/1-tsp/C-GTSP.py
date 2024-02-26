import argparse
import copy
import sys

from utils import read_all_files, save_final_results
from tsp_1_verify_utils import (extract_solution_with_separation, verify_start_end_depot, verify_euclidean_dist,
                                verify_city_group_visitation, reflect_num, test_file_num, cities_5, cities_10,
                                tsp_1_filter_files)

city_groups_5 = {
    'A': [1, 4],
    'B': [2, 5],
}

city_groups_10 = {
    'A': [7, 8],
    'B': [1, 6],
    'C': [2, 4],
    'D': [5, 9],
    'E': [10],
}


# Detailed constraint check function
def detailed_constraint_check(tours, robot_costs, cities, city_groups):
    all_contract_violated = ""
    # Check 1: Each robot starts and ends at the depot
    all_contract_violated += verify_start_end_depot(tours=tours)

    # Check 2': Each city group must be visited exactly once
    all_contract_violated += verify_city_group_visitation(tours, city_groups)

    # Check 3: Check Euclidean distance between cities for all robots
    all_contract_violated += verify_euclidean_dist(tours, cities, robot_costs)

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
    print('file number:', len(unfiltered_text_files_loc), sep='\n')
    file_groups = tsp_1_filter_files(unfiltered_text_files_loc)

    for point_num in file_groups.keys():
        point_num = int(point_num)
        if point_num == 5:
            cities = copy.deepcopy(cities_5)
            city_groups = copy.deepcopy(city_groups_5)
        elif point_num == 10:
            cities = copy.deepcopy(cities_10)
            city_groups = copy.deepcopy(city_groups_10)
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
                                                                 cities=cities, city_groups=city_groups)

            if constraint_check_message == "** YES!!! **":
                # print('file_path: ', file_path, '\n')
                reflect_id = int(file_path.split('/')[4].split('_')[1])
                file_id = int(file_path.split('/')[5].split('.')[0][-1])

                for i in range(reflect_id, reflect_num):
                    valid_final_cost[i][file_id] = final_cost
            else:
                # continue
                print('==========================================================================================')
                print('file_path: ', file_path, '\n')
                print(constraint_check_message)
                print('==========================================================================================')

        print('valid_final_cost:', valid_final_cost, sep='\n')

        save_final_results(dir_path=tmp_file_name, result_content=valid_final_cost, point_num=point_num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run main function with parameters.")
    parser.add_argument('--root_dir', type=str, default="evaluate/back_1_tsp/1-tsp/C-GTSP", help="root_dir")
    args = parser.parse_args()
    sys.exit(main(root_dir=args.root_dir))
