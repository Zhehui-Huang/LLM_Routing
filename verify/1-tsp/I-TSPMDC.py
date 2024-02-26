import argparse
import copy
import sys

from utils import read_all_files, save_final_results
from tsp_1_verify_utils import (extract_solution_with_separation, verify_euclidean_dist, verify_start_multi_end_depot,
                                verify_visit_city_multi_depots_once, reflect_num, test_file_num, cities_5, cities_10,
                                calculate_distance, tsp_1_filter_files)

depot_lists_5 = [1, 3]
energy_unit_5 = 9

depot_lists_10 = [1, 3, 7]
energy_unit_10 = 11


def verify_energy(tours, cities, ori_energy, depot_lists):
    segment_distances = []  # To store distances of each travel segment

    for robot, tour in tours.items():
        energy = ori_energy
        for i in range(len(tour) - 1):
            distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])

            # If the robot visits a depot, reset energy and continue
            if tour[i] in depot_lists:
                energy = ori_energy
            else:
                # Subtract the traveled distance from the robot's energy
                energy -= distance
                # If energy goes below 0 before reaching the next depot, return failure
                if energy < 0:
                    return f"Constraint Violated: Robot {robot} ran out of energy before reaching the next depot."
                segment_distances.append(distance)

    return ""


# Detailed constraint check function
def detailed_constraint_check(tours, robot_costs, cities, depot_lists, ori_energy):
    all_contract_violated = ""
    # Check 1: Each robot starts and ends at the depot
    all_contract_violated += verify_start_multi_end_depot(tours, start_depot=3, depot_lists=depot_lists)

    # Check 2: Each city must be visited exactly once
    all_contract_violated += verify_visit_city_multi_depots_once(tours, cities, depot_lists)

    # Check 3: Check Euclidean distance between cities for all robots
    all_contract_violated += verify_euclidean_dist(tours, cities, robot_costs)

    # Check 4: Check energy
    all_contract_violated += verify_energy(tours, cities, ori_energy=ori_energy, depot_lists=depot_lists)

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
            depot_lists = copy.deepcopy(depot_lists_5)
            ori_energy = energy_unit_5
        elif point_num == 10:
            cities = copy.deepcopy(cities_10)
            depot_lists = copy.deepcopy(depot_lists_10)
            ori_energy = energy_unit_10
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
                                                                 cities=cities, depot_lists=depot_lists,
                                                                 ori_energy=ori_energy)

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
    parser.add_argument('--root_dir', type=str, default="evaluate/back_1_tsp/1-tsp/I-TSPMDC", help="root_dir")
    args = parser.parse_args()
    sys.exit(main(root_dir=args.root_dir))
