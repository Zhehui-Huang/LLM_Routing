import sys

from utils import read_all_files, save_final_results
from verify_utils import extract_solution_with_separation, verify_start_end_depot, verify_visit_city_once, \
    verify_num_robots, verify_euclidean_dist, verify_start_multi_end_depot, verify_visit_city_multi_depots_once, \
    verify_energy

# Define city coordinates with city index starting from 1
cities = {
    1: (9, 4),  # Depot
    2: (4, 6),
    3: (4, 4),  # Depot
    4: (3, 4),
    5: (4, 8),
    6: (4, 3),
    7: (7, 5),  # Depot
    8: (5, 0),
    9: (1, 5),
    10: (9, 3)
}

reflect_num = 4
test_file_num = 3

depot_lists = [1, 3, 7]


# Detailed constraint check function
def detailed_constraint_check(tours: dict, robot_costs: dict) -> str:
    all_contract_violated = ""
    # Check 1: Each robot starts and ends at the depot
    all_contract_violated += verify_start_multi_end_depot(tours, start_depot=3, depot_lists=depot_lists)

    # Check 2: Each city must be visited exactly once
    all_contract_violated += verify_visit_city_multi_depots_once(tours, cities, depot_lists)

    # Check 3: Number of robots
    all_contract_violated += verify_num_robots(tours=tours)

    # Check 4: Check Euclidean distance between cities for all robots
    all_contract_violated += verify_euclidean_dist(tours, cities, robot_costs)

    # Check 5: Check energy
    all_contract_violated += verify_energy(tours, cities, ori_energy=11)

    if all_contract_violated != "":
        return all_contract_violated
    else:
        # If all checks pass
        return "** YES!!! **"


def main():
    valid_final_cost = {}
    tmp_file_name = '1_direct_reflect_v3/4-tsp/I-TSPMDC'
    root_dir = '../../evaluate/' + tmp_file_name
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
            reflect_id = int(file_path.split('/')[6].split('_')[1])
            file_id = int(file_path.split('/')[7].split('.')[0][-1])

            for i in range(reflect_id, reflect_num):
                valid_final_cost[i][file_id] = final_cost
        else:
            print(
                '====================================================================================================')
            print('file_path: ', file_path, '\n')
            print(constraint_check_message)
            print(
                '====================================================================================================')

    print('valid_final_cost:', valid_final_cost, sep='\n')

    save_final_results(dir_path=tmp_file_name, result_content=valid_final_cost)


if __name__ == '__main__':
    sys.exit(main())