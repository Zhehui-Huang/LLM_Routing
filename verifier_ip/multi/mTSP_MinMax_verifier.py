import os
import math
import random
import itertools
import sys
import time
import numpy as np
import gurobipy as gp
import matplotlib.pyplot as plt
from gurobipy import GRB

from verifier_ip.multi_utils import (TASK_BASE_PATH, DEBUG_FLAG, LLM_FOLDER_PATH, EVAL_TYPE_LIST, EXTRA_INFO_DICT,
                                     extract_route_cost_max_cost)

ROBOT_NUM_TYPE = 'multiple'
TASK_NAME = 'mTSP_MinMax'
FAKE_CITY_NUM = 10


def calculate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return dist_matrix


def parse_file(file_path):
    city_coords = []
    city_demand = []
    num_robots = 0
    capacity = 0
    num_cities = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Parse city coordinates
        coords_section = False
        for line in lines:
            if "City" in line or "Depot" in line:
                # Extract coordinates from the line
                parts = line.split(':')
                coordinates = parts[1].strip().strip('()').split(', ')
                x = int(coordinates[0])
                y = int(coordinates[1])
                city_coords.append((x, y))

        # Parse robot information
        robot_section = False
        for line in lines:
            if "Robot Information" in line:
                robot_section = True
                continue
            if robot_section:
                if "Number of robots:" in line:
                    num_robots = int(line.split(":")[1].strip().split()[0].rstrip('.'))
                if num_robots > 0:
                    break

    result = {
        'city_coordi': city_coords,
        'num_robot': num_robots
    }

    return result


def solve_mTSP_max(num_locations, num_salesmen, costs):
    N = num_locations
    M = num_salesmen
    # Create model
    m = Model()

    # Variables
    x = m.addVars(N, N, M, vtype=GRB.BINARY, name='x')
    u = m.addVars(N, M, vtype=GRB.CONTINUOUS, name='u')
    L = m.addVar(vtype=GRB.CONTINUOUS, name='L')

    # Objective: Minimize the maximum route length
    m.setObjective(L, GRB.MINIMIZE)

    # Constraints
    # Each city is visited exactly once
    m.addConstrs((quicksum(x[i, j, k] for k in range(M) for j in range(N) if j != i) == 1 for i in range(1, N)),
                 name='visit_once')

    # Each salesman starts and ends at the depot
    m.addConstrs((quicksum(x[0, j, k] for j in range(1, N)) == 1 for k in range(M)), name='start_depot')
    m.addConstrs((quicksum(x[i, 0, k] for i in range(1, N)) == 1 for k in range(M)), name='end_depot')

    # Subtour elimination (MTZ constraints)
    m.addConstrs(
        (u[i, k] - u[j, k] + N * x[i, j, k] <= N - 1 for i in range(1, N) for j in range(1, N) if i != j for k in
         range(M)), name='subtour_elimination')
    m.addConstrs((u[i, k] >= 2 for i in range(1, N) for k in range(M)), name='u_lower_bound')
    m.addConstrs((u[i, k] <= N for i in range(1, N) for k in range(M)), name='u_upper_bound')

    # Flow constraints to ensure the continuity of each tour
    m.addConstrs(
        (quicksum(x[i, j, k] for j in range(N) if j != i) - quicksum(x[j, i, k] for j in range(N) if j != i) == 0 for i
         in range(N) for k in range(M)), name='flow_continuity')

    # Maximum route length constraint
    m.addConstrs(
        (quicksum(costs[i][j] * x[i, j, k] for i in range(N) for j in range(N) if i != j) <= L for k in range(M)),
        name='max_route_length')

    # Optimize model
    m.optimize()

    # Print solution
    if m.status == GRB.OPTIMAL:
        print('Optimal value:', L.X)
        routes = []
        for k in range(M):
            print(f'Salesman {k + 1}:')
            for i in range(N):
                for j in range(N):
                    if x[i, j, k].X > 0.5:
                        routes.append((i, j))
        return routes, m.objVal
    else:
        print("No optimal solution found")
        return None, None


def solve_mTSP_max_verifier(num_locations, num_salesmen, costs, sol_x):
    n = num_locations  # Number of nodes (including depot)
    m = num_salesmen  # Number of salesmen

    # Model
    model = gp.Model()

    # Variables
    x = model.addVars(n, n, vtype=GRB.BINARY, name='x')
    u = model.addVars(n, vtype=GRB.CONTINUOUS, name='u')

    # Objective
    model.setObjective(gp.quicksum(costs[i][j] * x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)

    # Constraints
    model.addConstr(gp.quicksum(x[0, j] for j in range(1, n)) == m, "depot_departure")
    model.addConstr(gp.quicksum(x[j, 0] for j in range(1, n)) == m, "depot_return")

    for i in range(1, n):
        model.addConstr(gp.quicksum(x[i, j] for j in range(n) if j != i) == 1, f"visit_{i}")
        model.addConstr(gp.quicksum(x[j, i] for j in range(n) if j != i) == 1, f"return_{i}")

    # Subtour elimination (MTZ constraints)
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model.addConstr(u[i] - u[j] + (n * x[i, j]) <= n - 1)

    for i in range(n):
        for j in range(n):
            model.addConstr(x[i, j] == sol_x[i][j])

            # Optimize
    model.optimize()

    # Print the results
    if model.status == GRB.OPTIMAL:
        print("Optimal solution found:")
        print("Objective value:", model.objVal)
        routes = []
        for i in range(n):
            for j in range(n):
                if x[i, j].X > 0.5:  # if x[i, j] is 1
                    # print(f"x[{i},{j}] = 1")
                    routes.append((i, j))
        return routes, model.objVal
    else:
        print("No optimal solution found")
        return None, None


def route2edges(routes, num_city, num_vehicle):
    # route = [0, 1, 2, 3， 0]
    x = np.zeros((num_city, num_city))
    assert len(routes)==num_vehicle
    for vehicle in range(len(routes)):
        route = routes[vehicle]
        for i in range(len(route)-1):
            x[route[i], route[i+1]] = 1
    return x


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


def deal_instance(file_name, cities, distance_matrix, oracle_res, eval_type, llm_extra_info_folder_path, context_type, info):
    parts = file_name.split('-')
    city_num = parts[1][1:]
    instance_name = file_name[:-4]

    opt_gap_list = []
    success_list = []
    for instance_try_id in range(5):
        # print(f'{city_num}/{instance_name}/{instance_try_id}')
        tmp_folder_path = os.path.join(
            llm_extra_info_folder_path,
            f'{EXTRA_INFO_DICT[context_type]}/log/{ROBOT_NUM_TYPE}/{TASK_NAME}/{FAKE_CITY_NUM}/{instance_name}/{instance_try_id}'
        )
        print('Folder path: ', tmp_folder_path)

        use_log_id, use_log_name = get_use_log_file_name(eval_type=eval_type, tmp_folder_path=tmp_folder_path)

        if 'error' in use_log_name or 'timeout' in use_log_name:
            print(f"Error file found: {use_log_name}")
            success_list.append(0)
            continue
            # raise ValueError("Error file found.")

        route_res_path = os.path.join(
            llm_extra_info_folder_path, f'{EXTRA_INFO_DICT[context_type]}/log/{ROBOT_NUM_TYPE}/{TASK_NAME}/{FAKE_CITY_NUM}/{instance_name}/{instance_try_id}/{use_log_id}/{use_log_name}'
        )

        routes, _, _ = extract_route_cost_max_cost(file_path=route_res_path, robot_num=info['num_robot'])

        if not routes:
            success_list.append(0)
            continue
            # raise ValueError("Route is empty.")

        tmp_out_boundary_bool = False
        for route in routes:
            for tmp_item in route:
                if int(tmp_item) >= int(city_num):
                    tmp_out_boundary_bool = True
                    break
            if tmp_out_boundary_bool:
                break

        if tmp_out_boundary_bool:
            success_list.append(0)
            continue

        if DEBUG_FLAG:
            success_list.append(0)
            continue
        else:
            n = len(cities)
            m = info['num_robot']
            distance_matrix = calculate_distance_matrix(cities)

            sol_x = route2edges(routes, n, m)
            tour, _ = solve_mTSP_max_verifier(num_locations=n, num_salesmen=m, costs=distance_matrix, sol_x=sol_x)

            if tour:
                # if llm_travel_cost is None:
                #     print("LLM travel cost is None.")
                # elif not bool(np.isclose(ground_cost, llm_travel_cost, atol=1)):
                #     print(f"Costs are not equal. path: {route_res_path}")

                ground_cost = -1
                tmp_cost_list = []
                for route_item in routes:
                    tmp_cost = 0
                    for nid in range(len(route_item) - 1):
                        tmp_cost += distance_matrix[route_item[nid]][route_item[nid + 1]]

                    tmp_cost_list.append(tmp_cost)
                    if tmp_cost > ground_cost:
                        ground_cost = tmp_cost

                print(f"Ground cost: {ground_cost}, tmp_cost_list: {tmp_cost_list}")

                cost = float(ground_cost)
                optimal_cost = oracle_res[file_name][0]

                cost = round(cost, 2)
                optimal_cost = round(optimal_cost, 2)

                optimality_gap = (cost - optimal_cost) / optimal_cost
                if cost < optimal_cost:
                    raise ValueError(f"Cost is less than optimal cost. {cost}, {optimal_cost}")
                optimality_gap = optimality_gap * 100
                opt_gap_list.append(optimality_gap)
                success_list.append(1)
            else:
                success_list.append(0)

    return opt_gap_list, success_list


def mtsp_min_max_verifier(task_folder_base_path, context_type, llm_extra_info_folder_path):
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
            info = parse_file(task_instance_path)
            cities = info['city_coordi']

            distance_matrix = calculate_distance_matrix(cities)

            parts = file_name.split('-')
            city_num = parts[1][1:]
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
                info=info
            )

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
    start_time = time.time()
    llm_model_list = ['llama3_1_extra_info', 'gpt4_extra_info']
    context_type_list = ['zero', 'math', 'pseudo-code_v2', 'pseudo-code_v3', 'pdf_paper_v2', 'pdf_paper_v3']
    for llm_model in llm_model_list:
        llm_extra_info_folder_path = os.path.join(LLM_FOLDER_PATH, f"{llm_model}")
        for context_type in context_type_list:
            # llm/task + context_type
            # if llm_model == 'llama3_1_extra_info' and context_type == 'zero':
            #     continue

            print(f'Model name: {llm_model}\tContext type: {context_type}')
            task_folder_base_path = os.path.join(TASK_BASE_PATH, context_type)
            mtsp_min_max_verifier(task_folder_base_path=task_folder_base_path, context_type=context_type,
                                  llm_extra_info_folder_path=llm_extra_info_folder_path)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")


if __name__ == "__main__":
    sys.exit(main())
