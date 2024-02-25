import sys

from utils import read_all_files, save_final_results
from verify_utils import extract_solution_with_separation, verify_start_end_depot, verify_visit_city_once, \
    verify_num_robots, verify_euclidean_dist, verify_city_visitation_at_least_once, verify_dist_given_matrix

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

distance_matrix = [
    [0, 4, 8, 5, 7, 2, 3, 9, 8, 5],
    [4, 0, 8, 3, 6, 5, 2, 8, 6, 2],
    [5, 1, 0, 6, 9, 1, 10, 3, 7, 4],
    [9, 3, 5, 0, 7, 4, 9, 7, 2, 4],
    [9, 2, 10, 9, 0, 5, 2, 4, 7, 8],
    [3, 1, 4, 2, 8, 0, 2, 5, 6, 10],
    [4, 6, 2, 4, 2, 10, 0, 8, 7, 9],
    [8, 5, 2, 5, 8, 10, 9, 0, 1, 9],
    [7, 9, 8, 1, 8, 8, 3, 1, 0, 3],
    [3, 1, 5, 10, 7, 10, 9, 7, 9, 0]
]

reflect_num = 4
test_file_num = 3


# Detailed constraint check function
def detailed_constraint_check(tours: dict, robot_costs: dict) -> str:
    all_contract_violated = ""
    # Check 1: Each robot starts and ends at the depot
    all_contract_violated += verify_start_end_depot(tours=tours)

    # Check 2: Each city must be visited at least one robot one time
    all_contract_violated += verify_city_visitation_at_least_once(tours=tours, cities=cities)

    # Check 3: Number of robots
    all_contract_violated += verify_num_robots(tours=tours)

    # Check 4: Check distance between cities for all robots (distance matrix)
    # all_contract_violated += verify_euclidean_dist(tours, cities, robot_costs)
    all_contract_violated += verify_dist_given_matrix(tours, distance_matrix, robot_costs)

    if all_contract_violated != "":
        return all_contract_violated
    else:
        # If all checks pass
        return "** YES!!! **"


def main():
    valid_final_cost = {}
    tmp_file_name = '1_direct_reflect_v3/4-tsp/G-TSPM'
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
