import argparse
import copy
import sys

from others.utils import read_all_files, save_final_results
from others.tsp_1_verify_utils import (extract_solution_with_separation, verify_start_end_depot,
                                       verify_city_visitation_at_most_once, verify_total_travel_prod_cost,
                                       reflect_num, test_file_num, cities_5, cities_10, tsp_1_filter_files,
                                       verify_total_units_purchased)

city_products_5 = {
    1: {'units': 5, 'price': 8},
    2: {'units': 15, 'price': 5},
    4: {'units': 10, 'price': 4},
    5: {'units': 20, 'price': 10},
}

city_products_10 = {
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

min_cost_5 = 220
min_cost_10 = 560


def detailed_constraint_check(tours, robot_costs, purchases, cities, city_products):
    all_contract_violated = ""
    # Check 1: Each robot starts and ends at the depot
    all_contract_violated += verify_start_end_depot(tours=tours)
    if all_contract_violated != "":
        return all_contract_violated
    # Check 2: Each city at most once
    all_contract_violated += verify_city_visitation_at_most_once(tours=tours)
    if all_contract_violated != "":
        return all_contract_violated
    # Check 3: Check tour cost of all robots
    all_contract_violated += verify_total_travel_prod_cost(tours=tours, purchases=purchases,
                                                           city_products=city_products, robot_costs=robot_costs,
                                                           cities=cities)
    if all_contract_violated != "":
        return all_contract_violated
    # Check 5: Total Units Purchased
    # all_contract_violated += verify_total_units_purchased(purchases)



    try:
        if len(tours['Robot 1 - Tour']) < 4:
            all_contract_violated += "Robot 1 - Tour length is not 6\n"
    except:
        all_contract_violated += "Robot 1 - Tour length is not 6\n"

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
            city_products = copy.deepcopy(city_products_5)
            min_final_cost = min_cost_5
        elif point_num == 10:
            cities = copy.deepcopy(cities_10)
            city_products = copy.deepcopy(city_products_10)
            min_final_cost = min_cost_10
        else:
            raise ValueError(f'Invalid point number {point_num}')

        for i in range(reflect_num):
            valid_final_cost[i] = {j: -1 for j in range(test_file_num)}

        for file_path in file_groups[str(point_num)]:
            # print('file_path: ', file_path)
            robot_tours, robot_costs, final_cost, purchases = extract_solution_with_separation(file_path=file_path)
            # print(robot_tours)
            # print(robot_costs)
            # Running the detailed constraint check on the provided solution
            if final_cost < min_final_cost:
                constraint_check_message = "Final cost is less than the minimum cost"
            else:
                constraint_check_message = detailed_constraint_check(tours=robot_tours, robot_costs=robot_costs,
                                                                     purchases=purchases, cities=cities,
                                                                     city_products=city_products)

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
    parser.add_argument('--root_dir', type=str, default="evaluate/z_v2_fix_bug_5_external_tools_math_v3/1-tsp/E-TPP", help="root_dir")
    args = parser.parse_args()
    sys.exit(main(root_dir=args.root_dir))