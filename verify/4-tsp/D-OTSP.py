import argparse
import sys

from utils import read_all_files, save_final_results
from verify_utils import extract_solution_with_separation, verify_start_end_depot, verify_visit_city_once, \
    verify_num_robots, verify_euclidean_dist, reflect_num, test_file_num, verify_sequence_constraints
import numpy as np

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


# Function to calculate Euclidean distance
# def calculate_distance(point1, point2):
#     return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
#
#
# # Function to calculate cumulative distances for each city in a tour
# def cumulative_distances(tour, city_coords):
#     cum_dists = [0]  # Start with 0 for the depot
#     for i in range(1, len(tour)):
#         last_distance = cum_dists[-1]
#         new_distance = calculate_distance(city_coords[tour[i - 1]], city_coords[tour[i]])
#         cum_dists.append(last_distance + new_distance)
#     return cum_dists
#
#
# def update_distances_for_all_tours(tours, city_coords):
#     dist_dict = {}
#     for tour_key, tour_cities in tours.items():
#         # Calculate cumulative distances for the current tour
#         cum_distances = cumulative_distances(tour_cities, city_coords)
#         # Update distances for each city in the tour
#         for i, city_id in enumerate(tour_cities[1:-1]):  # Exclude the depot at the start and end
#             dist_dict[city_id] = cum_distances[i + 1]
#     return dist_dict
#
#
# def verify_sequence_constraints(tours, sequence_order):
#     sequence_order = eval(sequence_order)
#     dist_dict = update_distances_for_all_tours(tours=tours, city_coords=cities)
#     dist_dict[3] = 0
#     for i in range(len(sequence_order)):
#         for j in range(i+1, len(sequence_order)):
#             city_pre = sequence_order[i]
#             city_post = sequence_order[j]
#             print('city_pre:', city_pre, 'city_post:', city_post)
#             if dist_dict[city_pre] < dist_dict[city_post]:
#                 continue
#             else:
#                 return f"Sequence order constraint violated for {sequence_order[i]} and {sequence_order[j]}."
#     return ""

# Detailed constraint check function
def detailed_constraint_check(tours, robot_costs, sequence_order):
    all_contract_violated = ""
    # Check 1: Each robot starts and ends at the depot
    all_contract_violated += verify_start_end_depot(tours=tours)

    # Check 2: Each city must be visited exactly once
    all_contract_violated += verify_visit_city_once(tours=tours, cities=cities)

    # Check 3: Number of robots
    all_contract_violated += verify_num_robots(tours=tours)

    # Check 4: Check Euclidean distance between cities for all robots
    if all_contract_violated == "":
        all_contract_violated += verify_euclidean_dist(tours, cities, robot_costs)

    # Check 5: Sequence order
    if all_contract_violated == "":
        all_contract_violated += verify_sequence_constraints(tours, sequence_order)

    if all_contract_violated != "":
        return all_contract_violated
    else:
        # If all checks pass
        return "** YES!!! **"


def main(root_dir, sequence_order):
    valid_final_cost = {}
    # tmp_file_name = '1_direct_reflect_v3/4-tsp/D-OTSP'
    tmp_file_name = root_dir[9:]
    # root_dir = '../../evaluate/' + tmp_file_name
    text_files_loc = read_all_files(root_directory=root_dir)
    print('file number:', len(text_files_loc))

    # sequence_order = [2, 4, 5, 6, 7]

    for i in range(reflect_num):
        valid_final_cost[i] = {j: -1 for j in range(test_file_num)}

    for file_path in text_files_loc:
        # print('file_path: ', file_path, '\n')
        robot_tours, robot_costs, final_cost, _ = extract_solution_with_separation(file_path=file_path)
        # if 0 < final_cost < 11.09:
        #     print(final_cost, 11.09)
        # print(robot_tours)
        # print(robot_costs)
        # Running the detailed constraint check on the provided solution
        constraint_check_message = detailed_constraint_check(robot_tours, robot_costs, sequence_order)

        if constraint_check_message == "** YES!!! **":
            tmp_max_value = -1
            for tmp_value in robot_costs.values():
                if tmp_value > tmp_max_value:
                    tmp_max_value = tmp_value

            if np.round(final_cost, 2) < np.round(tmp_max_value, 2):
                # print('final cost: ', final_cost)
                # print('tmp_max_value: ', tmp_max_value)
                print('change final cost from ', final_cost, ' to ', tmp_max_value, '\n')
                final_cost = tmp_max_value

            if np.round(final_cost, 2) < 11.09:
                print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                print('final cost: ', final_cost)
                print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

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
    parser.add_argument('--root_dir', type=str, default="evaluate/Claude3_1_direct_v3/4-tsp/D-OTSP", help="root_dir")
    parser.add_argument('--sequence_order', nargs='+', default="[2, 4, 5, 6, 7]", help="root_dir")
    args = parser.parse_args()
    sys.exit(main(root_dir=args.root_dir, sequence_order=args.sequence_order))
