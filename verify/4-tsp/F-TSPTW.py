import sys

from utils import read_all_files, save_final_results
from verify_utils import extract_solution_with_separation, verify_start_end_depot, verify_visit_city_once, \
    verify_num_robots, verify_euclidean_dist, verify_visit_time_constraints

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

time_windows = {
    1: (3, 8),
    2: (5, 12),
    3: (0, float('inf')),  # Depot
    4: (0, 4),
    5: (1, 10),
    6: (1, 5),
    7: (1, 10),
    8: (3, 6),
    9: (2, 6),
    10: (7, 11)
}

reflect_num = 4
test_file_num = 3


# Detailed constraint check function
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

    all_contract_violated += verify_visit_time_constraints(tours, time_windows, cities)

    if all_contract_violated != "":
        return all_contract_violated
    else:
        # If all checks pass
        return "** YES!!! **"


def main():
    valid_final_cost = {}
    tmp_file_name = '1_direct_reflect_v3/4-tsp/F-TSPTW'
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
