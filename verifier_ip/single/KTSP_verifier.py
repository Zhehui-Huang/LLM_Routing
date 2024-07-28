import itertools
import math
import os
import sys

import gurobipy as gp
import numpy as np
from gurobipy import Model, GRB, quicksum

from verifier_ip.utils import (TASK_BASE_PATH, LLM_FOLDER_PATH, EVAL_TYPE_LIST, EXTRA_INFO_DICT, extract_route_and_cost,
                               DEBUG_FLAG)

ROBOT_NUM_TYPE = 'single'
TASK_NAME = 'KTSP'



def solve_k_tsp(cities, dist, k):
    n = len(cities)

    # Create a new Gurobi model
    model = gp.Model("k-TSP")
    model.setParam('OutputFlag', 0)

    # Create variables
    x = model.addVars(n, n, vtype=GRB.BINARY, name="x")
    y = model.addVars(n, vtype=GRB.BINARY, name="y")

    # Set objective function
    model.setObjective(gp.quicksum(dist[i, j] * x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)

    # Add constraints
    model.addConstr(gp.quicksum(y[i] for i in range(n)) == k, name="visit_k_cities")

    # Ensure the tour starts and ends at the home city
    model.addConstr(gp.quicksum(x[0, j] for j in range(1, n)) == 1, name="start_at_home")
    model.addConstr(gp.quicksum(x[i, 0] for i in range(1, n)) == 1, name="end_at_home")

    # Degree constraints
    for i in range(1, n):
        model.addConstr(gp.quicksum(x[i, j] for j in range(n) if j != i) == y[i], name=f"out_degree_{i}")
        model.addConstr(gp.quicksum(x[j, i] for j in range(n) if j != i) == y[i], name=f"in_degree_{i}")

    # Sub-tour elimination constraints
    for subset_size in range(2, k + 1):
        for subset in itertools.combinations(range(1, n), subset_size):
            model.addConstr(gp.quicksum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1,
                            name=f"subtour_elim_{subset}")

    # Optimize the model
    model.optimize()

    # Extract the solution
    if model.status == GRB.OPTIMAL:
        tour = []
        for i in range(n):
            for j in range(n):
                if x[i, j].x > 0.5:
                    tour.append((i, j))
        return tour, model.objVal
    else:
        print("No optimal solution found")
        return None, None


def calculate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return dist_matrix

def read_city_locations(file_path):
    city_locations = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "City" in line or "Depot" in line:
                # Extract coordinates from the line
                parts = line.split(':')
                coordinates = parts[1].strip().strip('()').split(', ')
                x = int(coordinates[0])
                y = int(coordinates[1])
                city_locations.append((x, y))
    return city_locations


def solve_tsp_verifier(cities, distance_matrix, sol_x):
    n = len(cities)

    # Create a new Gurobi model
    model = gp.Model("TSP")
    model.setParam('OutputFlag', 0)

    # Create variables
    x = model.addVars(n, n, vtype=GRB.BINARY, name="x")

    # Set the objective function
    model.setObjective(gp.quicksum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)

    # Add constraints
    # Each city must be left exactly once
    for i in range(n):
        model.addConstr(gp.quicksum(x[i, j] for j in range(n) if j != i) == 1, name=f"leave_{i}")

    # Each city must be entered exactly once
    for j in range(n):
        model.addConstr(gp.quicksum(x[i, j] for i in range(n) if i != j) == 1, name=f"enter_{j}")

    # DFJ subtour elimination constraints
    def add_subtour_elimination_constraints(model, x, n):
        subsets = []
        for r in range(2, n):
            subsets.extend(itertools.combinations(range(n), r))

        for subset in subsets:
            S = set(subset)
            if 1 <= len(S) <= n - 1:
                model.addConstr(gp.quicksum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1)

    add_subtour_elimination_constraints(model, x, n)

    # enforce solution to be the same as sol_x
    for i in range(n):
        for j in range(n):
            model.addConstr(x[i, j] == sol_x[i][j])
    # Optimize the model
    model.optimize()

    # Extract the solution
    if model.status == GRB.OPTIMAL:
        tour = []
        for i in range(n):
            for j in range(n):
                if x[i, j].x > 0.5:
                    tour.append((i, j))
        return tour, model.objVal
    else:
        return None, None

def route2edges(route, num_city, index_dic):
    # route = [0, 1, 2, 3， 0]
    x = np.zeros((num_city, num_city))
    for i in range(len(route)-1):
        x[index_dic[route[i]], index_dic[route[i+1]]] = 1
    return x

def solve_k_tsp_verifier(cities, k, route):
    selected_cities = list(set(route))
    if len(selected_cities) != k:
        return None, None
    else:
        index = {}
        selected_cities_location = []
        for city in selected_cities:
            index[city] = selected_cities.index(city)
            selected_cities_location.append(cities[city])

        distance_matrix = calculate_distance_matrix(selected_cities_location)
        sol_x = route2edges(route, k, index)
        tour, cost = solve_tsp_verifier(selected_cities, distance_matrix, sol_x)

    return tour, cost


# def route2edges(route, num_city, index_dic):
#     # route = [0, 1, 2, 3， 0]
#     x = np.zeros((num_city, num_city))
#     for i in range(len(route)-1):
#         x[index_dic[route[i]], index_dic[route[i+1]]] = 1
#     return x


def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def get_ktsp_k(city_num, instance_id):
    if city_num == 10:
        k_list = [4, 5, 6, 7, 8]
    elif city_num == 15:
        k_list = [4, 6, 8, 10, 12]
    elif city_num == 20:
        k_list = [4, 7, 10, 13, 16]
    else:
        raise ValueError(f"Invalid city number. {city_num}")

    return k_list[instance_id]

def get_use_log_file_name(eval_type, tmp_folder_path):
    # pass_one, pass_debug, pass_overall
    if eval_type == 'pass_one':
        # Pass one time
        log_id = 0
        log_id_path = os.path.join(tmp_folder_path, str(log_id))
        log_names = os.listdir(log_id_path)
        log_names.sort()
        log_name = log_names[0]
    elif eval_type == 'pass_debug':
        log_id = 0
        log_id_path = os.path.join(tmp_folder_path, str(log_id))
        log_names = os.listdir(log_id_path)
        log_name = max(log_names, key=lambda name: int(name.split('_')[1][1]))
    elif eval_type == 'pass_overall':
        subfolder_name_list = [f.path for f in os.scandir(tmp_folder_path) if f.is_dir()]
        subfolder_name_list.sort()
        log_id = max(int(path[-1]) for path in subfolder_name_list)
        max_try_id_path = os.path.join(tmp_folder_path, str(log_id))
        log_names = os.listdir(max_try_id_path)
        log_name = max(log_names, key=lambda name: int(name.split('_')[1][1]))
    else:
        raise ValueError(f"Invalid eval_type. {eval_type}")

    return log_id, log_name


def deal_instance(file_name, cities, distance_matrix, oracle_res, eval_type, llm_extra_info_folder_path, context_type,
                  task_instance_path):
    parts = file_name.split('_')
    city_num = parts[1]
    instance_name = file_name[:-4]

    opt_gap_list = []
    success_list = []
    for instance_try_id in range(5):
        # print(f'{city_num}/{instance_name}/{instance_try_id}')
        tmp_folder_path = os.path.join(
            llm_extra_info_folder_path,
            f'{EXTRA_INFO_DICT[context_type]}/log/{ROBOT_NUM_TYPE}/{TASK_NAME}/{city_num}/{instance_name}/{instance_try_id}'
        )
        print('Folder path: ', tmp_folder_path)

        use_log_id, use_log_name = get_use_log_file_name(eval_type=eval_type, tmp_folder_path=tmp_folder_path)

        if 'error' in use_log_name or 'timeout' in use_log_name:
            print(f"Error file found: {use_log_name}")
            success_list.append(0)
            continue
            # raise ValueError("Error file found.")

        route_res_path = os.path.join(
            llm_extra_info_folder_path, f'{EXTRA_INFO_DICT[context_type]}/log/{ROBOT_NUM_TYPE}/{TASK_NAME}/{city_num}/{instance_name}/{instance_try_id}/{use_log_id}/{use_log_name}'
        )

        route, llm_travel_cost = extract_route_and_cost(file_path=route_res_path)

        if not route:
            success_list.append(0)
            continue
            # raise ValueError("Route is empty.")

        if DEBUG_FLAG:
            success_list.append(0)
            continue
        else:
            # try:
            #     sol_x = route2edges(route, len(cities))
            # except:
            #     success_list.append(0)
            #     continue

            #  TODO: Here, instance_name should be 0 - 4
            k = get_ktsp_k(city_num=int(city_num), instance_id=int(instance_name[-1]))
            tour, _ = solve_k_tsp_verifier(cities=cities, k=k,  route=route)

            if tour:
                # get ground cost
                edge_distance_list = [distance_matrix[i][j] for i, j in tour]
                ground_cost = float(sum(edge_distance_list))



                if llm_travel_cost is None:
                    print("LLM travel cost is None.")
                elif not bool(np.isclose(ground_cost, llm_travel_cost, atol=1)):
                    print(f"Costs are not equal. path: {route_res_path}")

                cost = ground_cost
                optimal_cost = oracle_res[file_name][0]

                cost = round(cost, 2)
                optimal_cost = round(optimal_cost, 2)

                optimality_gap = (cost - optimal_cost) / optimal_cost
                optimality_gap = optimality_gap * 100
                opt_gap_list.append(optimality_gap)
                success_list.append(1)
            else:
                success_list.append(0)

    return opt_gap_list, success_list


def ktsp_verifier(task_folder_base_path, context_type, llm_extra_info_folder_path):
    task_folder_path = os.path.join(task_folder_base_path, f'{ROBOT_NUM_TYPE}/{TASK_NAME}')
    res_path = os.path.join(LLM_FOLDER_PATH, f'../oracle/results/txt/{ROBOT_NUM_TYPE}/{TASK_NAME}_result.txt')
    file_list = os.listdir(task_folder_path)
    file_list.sort()

    for eval_type in EVAL_TYPE_LIST:
        print('Evaluation type:', eval_type)
        avg_opt_gap_dir = {}
        avg_success_dir = {}

        # Open a file to write down all results
        overall_opt_gap_dir = {}
        overall_success_dir = {}

        for file_name in file_list:
            task_instance_path = os.path.join(task_folder_path, file_name)
            cities = read_city_locations(task_instance_path)
            distance_matrix = calculate_distance_matrix(cities)

            parts = file_name.split('_')
            city_num = parts[1]
            if city_num not in avg_opt_gap_dir:
                avg_opt_gap_dir[city_num] = []
                overall_opt_gap_dir[city_num] = {}
            if city_num not in avg_success_dir:
                avg_success_dir[city_num] = []
                overall_success_dir[city_num] = {}

            with open(res_path, "r") as file:
                content = file.read()
                content = content.replace('data = ', '', 1)
                oracle_res = eval(content)
            opt_gap_list, success_list = deal_instance(
                file_name=file_name, cities=cities, distance_matrix=distance_matrix, oracle_res=oracle_res,
                eval_type=eval_type, llm_extra_info_folder_path=llm_extra_info_folder_path, context_type=context_type,
                task_instance_path=task_instance_path)

            print(f'{file_name}')
            if len(opt_gap_list) > 0:
                avg_opt_gap_dir[city_num].append(np.mean(opt_gap_list))
                overall_opt_gap_dir[city_num][file_name] = opt_gap_list
            else:
                overall_opt_gap_dir[city_num][file_name] = []

            if len(success_list) == 5:
                avg_success_dir[city_num].append(np.mean(success_list))

                overall_success_dir[city_num][file_name] = success_list
            else:
                raise ValueError(f"Invalid success_list. {success_list}")

        print("***********\tSTART\t***************")
        print(f"Average optimality gap for each city: {avg_opt_gap_dir}")
        print(f"Average success for each city: {avg_success_dir}")
        for key, value in avg_opt_gap_dir.items():
            print(f"City: {key}\t\tAverage optimality gap: {value}, mean: {np.mean(value)}")
        print("***********\tEND\t***************")

        for key, value in avg_success_dir.items():
            print(f"City: {key}\t\tAverage success: {np.mean(avg_success_dir[key])}\t\tSuccess list: {avg_success_dir[key]}")

        if 'llama3_1' in llm_extra_info_folder_path:
            tmp_model_name = 'llama3_1'
        elif 'gpt4' in llm_extra_info_folder_path:
            tmp_model_name = 'gpt4'
        else:
            raise ValueError(f"Invalid llm_extra_info_folder_path. {llm_extra_info_folder_path}")
        opt_gap_write_path = f'../metric/{tmp_model_name}/{context_type}/{eval_type}/{ROBOT_NUM_TYPE}/{TASK_NAME}/opt_gap.txt'
        success_write_path = f'../metric/{tmp_model_name}/{context_type}/{eval_type}/{ROBOT_NUM_TYPE}/{TASK_NAME}/success.txt'

        overall_opt_gap_write_path = f'../metric/{tmp_model_name}/{context_type}/{eval_type}/{ROBOT_NUM_TYPE}/{TASK_NAME}/opt_gap_overall_detail.txt'
        overall_success_write_path = f'../metric/{tmp_model_name}/{context_type}/{eval_type}/{ROBOT_NUM_TYPE}/{TASK_NAME}/success_overall_detail.txt'

        os.makedirs(os.path.dirname(opt_gap_write_path), exist_ok=True)
        os.makedirs(os.path.dirname(success_write_path), exist_ok=True)

        with open(opt_gap_write_path, "w") as file:
            for key, value in avg_opt_gap_dir.items():
                file.write(f"City: {key}\t\tAverage opt gap: {np.mean(value)}\t\tOpt gap list: {value}\n")
            file.write('\nDetails:\n')
            file.write(str(avg_opt_gap_dir))

        with open(success_write_path, "w") as file:
            for key, value in avg_success_dir.items():
                file.write(f"City: {key}\t\tAverage success: {np.mean(value)}\t\tSuccess list: {value}\n")
            file.write('\nDetails:\n')
            file.write(str(avg_success_dir))

        # Overall data
        with open(overall_opt_gap_write_path, "w") as file:
            for city, instances in overall_opt_gap_dir.items():
                file.write(f"City: {city}, Instance: {instances}\n")
                for instance, values in instances.items():
                    file.write(f"{instance}: {values}\n")
                file.write("\n")

        with open(overall_success_write_path, "w") as file:
            for city, instances in overall_success_dir.items():
                file.write(f"City: {city}, Instance: {instances}\n")
                for instance, values in instances.items():
                    file.write(f"{instance}: {values}\n")
                file.write("\n")



def main():
    llm_model_list = ['llama3_1_extra_info', 'gpt4_extra_info']
    context_type_list = ['zero', 'math', 'pseudo-code_v2', 'pseudo-code_v3', 'pdf_paper_v2', 'pdf_paper_v3']
    for llm_model in llm_model_list:
        llm_extra_info_folder_path = os.path.join(LLM_FOLDER_PATH, f"{llm_model}")
        for context_type in context_type_list:
            # llm/task + context_type
            # if llm_model == 'llama3_1_extra_info' and context_type != 'zero':
            #     continue

            print(f'Model name: {llm_model}\tContext type: {context_type}')
            task_folder_base_path = os.path.join(TASK_BASE_PATH, context_type)
            ktsp_verifier(task_folder_base_path=task_folder_base_path, context_type=context_type,
                          llm_extra_info_folder_path=llm_extra_info_folder_path)


if __name__ == "__main__":
    sys.exit(main())


    # current_directory = os.getcwd() + '/single/GTSP'
    # file_name = 'city_10_instance_0.txt'
    # route = [0, 1, 2, 3, 0]
    #
    # cities = read_city_locations(current_directory + '/' + file_name)
    # group = read_city_groups(current_directory + '/' + file_name)
    # distance_matrix = calculate_distance_matrix(cities)
    # V = list(range(len(cities)))
    # coords = {i: cities[i] for i in V}
    # k = len(group)
    # # tour, cost = solve_tsp(cities, distance_matrix)
    #
    # sol_x = route2edges(route, len(cities))
    #
    # tour, cost = solve_gtsp_verifier(V, group, distance_matrix, k, coords, sol_x)
    #
    # if tour:
    #     print("**************************")
    #     print(f"feasible route: {route}")
    #     # plot_tour(cities, distance_matrix, tour)
    #     # visualize_tour(cities, tour)
    #
    # else:
    #     print("**************************")
    #     print("Infeasible route.")



