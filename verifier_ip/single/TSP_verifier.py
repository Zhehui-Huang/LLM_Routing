import os
import math
import random
import itertools
import sys

import numpy as np
import gurobipy as gp
import matplotlib.pyplot as plt
from gurobipy import GRB

from verifier_ip.utils import (calculate_distance_matrix, TASK_BASE_PATH, read_city_locations, route2edges,
                               extract_route_and_cost, LLM_FOLDER_PATH)


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


def deal_instance(file_name, cities, distance_matrix, oracle_res):
    parts = file_name.split('_')
    city_num = parts[1]
    instance_name = file_name[:-4]
    opt_gap_list = []
    success_list = []
    for instance_try_id in range(5):
        print(f'{city_num}/{instance_name}/{instance_try_id}')
        tmp_folder_path = os.path.join(
            LLM_FOLDER_PATH,
            f'extra_info/log/single/TSP/{city_num}/{instance_name}/{instance_try_id}'
        )
        subfolder_name_list = [f.path for f in os.scandir(tmp_folder_path) if f.is_dir()]
        max_try_id = max(int(path[-1]) for path in subfolder_name_list)
        max_try_id_path = os.path.join(tmp_folder_path, str(max_try_id))
        log_names = os.listdir(max_try_id_path)
        max_log_filename = max(log_names, key=lambda name: int(name.split('_')[1][1]))

        if 'error' in max_log_filename or 'timeout' in max_log_filename:
            print(f"Error file found: {max_log_filename}")
            success_list.append(0)
            continue
            # raise ValueError("Error file found.")

        route_res_path = os.path.join(LLM_FOLDER_PATH, f'extra_info/log/single/TSP/'
                                                       f'{city_num}/{instance_name}/{instance_try_id}/{max_try_id}/'
                                                       f'{max_log_filename}')
        route, llm_travel_cost = extract_route_and_cost(file_path=route_res_path)
        if not route:
            raise ValueError("Route is empty.")

        sol_x = route2edges(route, len(cities))
        tour, ground_cost = solve_tsp_verifier(cities=cities, distance_matrix=distance_matrix, sol_x=sol_x)

        if tour:
            if llm_travel_cost is None:
                raise ValueError("LLM travel cost is None.")
            elif not bool(np.isclose(ground_cost, llm_travel_cost, atol=1)):
                print(f"Costs are not equal. path: {route_res_path}")

            cost = ground_cost
            optimal_cost = oracle_res[file_name][0]
            # print("***********\tSTART\t***************")
            # print(f'{city_num}/{instance_name}/{instance_try_id}/{max_try_id}/{max_log_filename}')
            optimality_gap = (cost - optimal_cost) / optimal_cost
            optimality_gap = optimality_gap * 100
            # print(f"feasible route: {route}\t\tcost: {cost}, optimality gap: {optimality_gap} %")
            # print("***********\tEND\t***************")
            # plot_tour(cities, distance_matrix, tour)
            # visualize_tour(cities, tour)
            opt_gap_list.append(optimality_gap)
            success_list.append(1)
        else:
            success_list.append(0)
            # raise ValueError("Tour is empty.")
            # print("***********\tSTART\t***************")
            # print(f'{city_num}/{instance_name}/{instance_try_id}/{max_try_id}/{max_log_filename}')
            # print(f"Infeasible route. {route}\t\tllm_travel_cost: {llm_travel_cost}\t\tground_cost: {ground_cost}")
            # print("***********\tEND\t***************")

    return opt_gap_list, success_list


def main():
    task_folder_path = os.path.join(TASK_BASE_PATH, 'single/TSP')
    res_path = os.path.join(LLM_FOLDER_PATH, '../oracle/results/txt/single/TSP_result.txt')
    file_list = os.listdir(task_folder_path)
    file_list.sort()

    avg_opt_gap_dir = {}
    avg_success_dir = {}
    for file_name in file_list:
        task_instance_path = os.path.join(task_folder_path, file_name)
        cities = read_city_locations(task_instance_path)
        distance_matrix = calculate_distance_matrix(cities)

        parts = file_name.split('_')
        city_num = parts[1]
        if city_num not in avg_opt_gap_dir:
            avg_opt_gap_dir[city_num] = []
        if city_num not in avg_success_dir:
            avg_success_dir[city_num] = []

        with open(res_path, "r") as file:
            content = file.read()
            content = content.replace('data = ', '', 1)
            oracle_res = eval(content)
        opt_gap_list, success_list = deal_instance(file_name=file_name, cities=cities, distance_matrix=distance_matrix,
                                                   oracle_res=oracle_res)

        print(f'{file_name}')
        avg_opt_gap_dir[city_num].append(np.mean(opt_gap_list))
        avg_success_dir[city_num].append(np.mean(success_list))

    print("***********\tSTART\t***************")
    print(f"Average optimality gap for each city: {avg_opt_gap_dir}")
    print(f"Average success for each city: {avg_success_dir}")
    for key, value in avg_opt_gap_dir.items():
        print(f"City: {key}\t\tAverage optimality gap: {value}, mean: {np.mean(value)}")
    print("***********\tEND\t***************")

    for key, value in avg_success_dir.items():
        print(f"City: {key}\t\tAverage success: {np.mean(avg_success_dir[key])}\t\tSuccess list: {avg_success_dir[key]}")

    opt_gap_write_path = 'gap/single/TSP/opt_gap.txt'
    success_write_path = 'gap/single/TSP/success.txt'

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


if __name__ == "__main__":
    sys.exit(main())
