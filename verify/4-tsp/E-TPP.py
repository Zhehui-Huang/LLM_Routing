import argparse
import sys

from others.utils import read_all_files, save_final_results
from others.verify_utils import extract_solution_with_separation, verify_start_end_depot, verify_visit_city_once, \
    verify_num_robots, verify_euclidean_dist, verify_city_visitation_at_most_once, verify_total_units_purchased, \
    verify_robot_capacity, verify_full_purchase_requirements, verify_total_travel_prod_cost, reflect_num, test_file_num

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

city_products = {
    1: {'units': 5, 'price': 20},
    2: {'units': 15, 'price': 11},
    4: {'units': 10, 'price': 15},
    5: {'units': 20, 'price': 9},
    6: {'units': 15, 'price': 10},
    7: {'units': 10, 'price': 16},
    8: {'units': 10, 'price': 8},
    9: {'units': 15, 'price': 2},
    10: {'units': 20, 'price': 6},
}


robot_capacities = {'Robot A': 10, 'Robot B': 15, 'Robot C': 20, 'Robot D': 20}

# reflect_num = 6
# test_file_num = 10


# Detailed constraint check function
def detailed_constraint_check(tours, robot_costs, purchases):
    all_contract_violated = ""
    # Check 1: Each robot starts and ends at the depot
    all_contract_violated += verify_start_end_depot(tours=tours)

    # Check 2: Each city at most once
    all_contract_violated += verify_city_visitation_at_most_once(tours=tours)

    # Check 3: Number of robots
    all_contract_violated += verify_num_robots(tours=tours)

    # Check 4: Check tour cost of all robots
    all_contract_violated += verify_total_travel_prod_cost(tours=tours, purchases=purchases,
                                                           city_products=city_products, robot_costs=robot_costs,
                                                           cities=cities)

    # Check 5: Total Units Purchased
    all_contract_violated += verify_total_units_purchased(purchases)

    # Check 6: Product Amount vs. Robot Capacity
    all_contract_violated += verify_robot_capacity(robot_capacities=robot_capacities, product=purchases)

    # Check 7: Full Purchase Requirements
    if all_contract_violated == "":
        all_contract_violated += verify_full_purchase_requirements(city_products=city_products, product=purchases)

    if all_contract_violated != "":
        return all_contract_violated
    else:
        # If all checks pass
        return "** YES!!! **"


def main(root_dir=""):
    valid_final_cost = {}
    tmp_file_name = root_dir[9:]
    text_files_loc = read_all_files(root_directory=root_dir)
    print('file number:', len(text_files_loc))

    for i in range(reflect_num):
        valid_final_cost[i] = {j: -1 for j in range(test_file_num)}

    for file_path in text_files_loc:
        # print('file_path: ', file_path, '\n')
        robot_tours, robot_costs, final_cost, purchases = extract_solution_with_separation(file_path=file_path)
        # print(robot_tours)
        # print(robot_costs)
        # Running the detailed constraint check on the provided solution
        constraint_check_message = detailed_constraint_check(robot_tours, robot_costs, purchases)

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
    parser.add_argument('--root_dir', type=str, default="evaluate/z_v2_fix_bug_5_external_tools_direct_v3/4-tsp/E-TPP", help="root_dir")
    args = parser.parse_args()
    sys.exit(main(root_dir=args.root_dir))
