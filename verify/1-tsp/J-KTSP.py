import argparse
import copy
import sys

from others.utils import read_all_files, save_final_results
from others.tsp_1_verify_utils import (extract_solution_with_separation, verify_start_end_depot, verify_euclidean_dist,
                                       reflect_num, test_file_num, cities_5, cities_10, tsp_1_filter_files)

selected_cities_5 = [2, 3, 4, 5]
selected_cities_10 = [2, 3, 4, 5, 6, 7, 9]


def verify_selected_cities(tours, selected_cities, point_num):
    if point_num == 5:
        should_no_city_visited = any(1 in tour for tour in tours.values())
    elif point_num == 10:
        should_no_city_visited_1 = any(1 in tour for tour in tours.values())
        should_no_city_visited_8 = any(8 in tour for tour in tours.values())
        should_no_city_visited_10 = any(10 in tour for tour in tours.values())
        should_no_city_visited = should_no_city_visited_1 or should_no_city_visited_8 or should_no_city_visited_10
    else:
        raise ValueError(f'Invalid point number {point_num}')

    if should_no_city_visited:
        return "Constraint Violated: City 10 should not be visited."

    cities_visited = []
    for tour in tours.values():
        cities_visited.extend(tour[1:-1])  # Exclude the depot from the beginning and end of each tour

    # Check if each city (except for the depot and city 10, which should not be visited) is visited exactly once
    cities_to_visit = set(selected_cities)
    visited_once_check = all(cities_visited.count(city) == 1 for city in cities_to_visit if city != 3)

    if not visited_once_check:
        return "Constraint Violated: Each city (except city 3 and city 10) should be visited exactly once."

    return ""


def detailed_constraint_check(tours, robot_costs, cities, selected_cities, point_num):
    all_contract_violated = ""
    # Check 1: Each robot starts and ends at the depot
    all_contract_violated += verify_start_end_depot(tours=tours)

    # Check 2: Check Euclidean distance between cities for all robots
    if all_contract_violated != "":
        return all_contract_violated
    all_contract_violated += verify_euclidean_dist(tours, cities, robot_costs)

    # Check 3: Each city must be visited exactly once
    all_contract_violated += verify_selected_cities(tours=tours, selected_cities=selected_cities, point_num=point_num)

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
            selected_cities = copy.deepcopy(selected_cities_5)
        elif point_num == 10:
            cities = copy.deepcopy(cities_10)
            selected_cities = copy.deepcopy(selected_cities_10)
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
                                                                 cities=cities, selected_cities=selected_cities,
                                                                 point_num=point_num)

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
    parser.add_argument('--root_dir', type=str, default="evaluate/z_v2_fix_bug_1_direct_reflect_v3/1-tsp/A-TSP", help="root_dir")
    args = parser.parse_args()
    sys.exit(main(root_dir=args.root_dir))
