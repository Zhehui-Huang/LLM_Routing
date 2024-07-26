import gurobipy as gp
from gurobipy import GRB
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import math
import os
import pickle


def calculate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return dist_matrix


def visualize_tour(cities, tour):
    plt.figure(figsize=(10, 10))
    for (i, j) in tour:
        plt.plot([cities[i][0], cities[j][0]], [cities[i][1], cities[j][1]], 'b-o')
    
    for idx, (x, y) in enumerate(cities):
        plt.text(x, y, f'  {idx}', fontsize=12)
    
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('TSP Optimal Tour')
    plt.grid()
    plt.show()

def solve_mTSP_MD_free(n, m, m_i, K, L, D, V_prime, V, c):
    # Create a new model
    model = gp.Model("Nonfixed_Destination_MmTSP")
    
    # Create variables
    x = model.addVars(V, V, vtype=GRB.BINARY, name="x")
    u = model.addVars(V_prime, vtype=GRB.INTEGER, name="u")
    
    # Set objective
    model.setObjective(gp.quicksum(c[i, j] * x[i, j] for i in V for j in V), GRB.MINIMIZE)
    
    # Add constraints
    
    # Ensure exactly m_i salesmen leave each depot i in D
    for i in D:
        model.addConstr(gp.quicksum(x[i, j] for j in V_prime) == m_i[i])
    
    # Ensure exactly m_i salesmen return to each depot i in D
    for i in D:
        model.addConstr(gp.quicksum(x[j, i] for j in V_prime) == m_i[i])
    
    # Ensure each customer node is visited exactly once
    for j in V_prime:
        model.addConstr(gp.quicksum(x[i, j] for i in V if i!=j) == 1)
        model.addConstr(gp.quicksum(x[j, i] for i in V if i!=j) == 1)
    
    # Bound constraints to ensure proper tour lengths and initialize u_i
    for i in V_prime:
        model.addConstr(u[i] + (L - 2) * gp.quicksum(x[k, i] for k in D) - gp.quicksum(x[i, k] for k in D) <= L - 1)
        model.addConstr(u[i] + gp.quicksum(x[k, i] for k in D) + (2 - K) * gp.quicksum(x[i, k] for k in D) >= 2)
    
    # Prohibit a salesman from serving only a single customer
    for i in V_prime:
        for k in D:
            model.addConstr(x[k, i] + x[i, k] <= 1)
    
    # Subtour elimination constraints
    for i in V_prime:
        for j in V_prime:
            if i != j:
                model.addConstr(u[i] - u[j] + L * x[i, j] + (L - 2) * x[j, i] <= L - 1)
    
    # Optimize the model
    model.optimize()
    
    if model.status == GRB.OPTIMAL:
        print("Optimal solution found:")
        print("Objective value:", model.objVal)
        routes = []
        for i in range(n):
            for j in range(n):
                if x[i, j].X > 0.5:  # if x[i, j] is 1
                    #print(f"x[{i},{j}] = 1")
                    routes.append((i, j))
        return routes, model.objVal
    else:
        print("No optimal solution found")
        return None, None



def solve_mTSP_MD_free_verifier(n, m, m_i, K, L, D, V_prime, V, c, sol_x):
    # Create a new model
    model = gp.Model("Nonfixed_Destination_MmTSP")
    
    # Create variables
    x = model.addVars(V, V, vtype=GRB.BINARY, name="x")
    u = model.addVars(V_prime, vtype=GRB.INTEGER, name="u")
    
    # Set objective
    model.setObjective(gp.quicksum(c[i, j] * x[i, j] for i in V for j in V), GRB.MINIMIZE)
    
    # Add constraints
    
    # Ensure exactly m_i salesmen leave each depot i in D
    for i in D:
        model.addConstr(gp.quicksum(x[i, j] for j in V_prime) == m_i[i])
    
    # Ensure exactly m_i salesmen return to each depot i in D
    for i in D:
        model.addConstr(gp.quicksum(x[j, i] for j in V_prime) == m_i[i])
    
    # Ensure each customer node is visited exactly once
    for j in V_prime:
        model.addConstr(gp.quicksum(x[i, j] for i in V if i!=j) == 1)
        model.addConstr(gp.quicksum(x[j, i] for i in V if i!=j) == 1)
    
    # Bound constraints to ensure proper tour lengths and initialize u_i
    for i in V_prime:
        model.addConstr(u[i] + (L - 2) * gp.quicksum(x[k, i] for k in D) - gp.quicksum(x[i, k] for k in D) <= L - 1)
        model.addConstr(u[i] + gp.quicksum(x[k, i] for k in D) + (2 - K) * gp.quicksum(x[i, k] for k in D) >= 2)
    
    # Prohibit a salesman from serving only a single customer
    for i in V_prime:
        for k in D:
            model.addConstr(x[k, i] + x[i, k] <= 1)
    
    # Subtour elimination constraints
    for i in V_prime:
        for j in V_prime:
            if i != j:
                model.addConstr(u[i] - u[j] + L * x[i, j] + (L - 2) * x[j, i] <= L - 1)
    
    
    
    for i in V:
        for j in V:
            model.addConstr(x[i, j] ==sol_x[i][j])        
    
    
    
    
    # Optimize the model
    model.optimize()
    
    if model.status == GRB.OPTIMAL:
        print("Optimal solution found:")
        print("Objective value:", model.objVal)
        routes = []
        for i in range(n):
            for j in range(n):
                if x[i, j].X > 0.5:  # if x[i, j] is 1
                    #print(f"x[{i},{j}] = 1")
                    routes.append((i, j))
        return routes, model.objVal
    else:
        print("No optimal solution found")
        return None, None




def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize the dictionary
    data = {
        'cities': [],
        'num_robot': 0,
        'depot_cities': []
    }

    # Read through the file lines
    for line in lines:
        line = line.strip()
        if line.startswith("Depot city") or line.startswith("City"):
            parts = line.split(":")
            index = int(parts[0].split()[2]) if line.startswith("Depot city") else int(parts[0].split()[1])
            coords = tuple(map(int, parts[1].strip().strip("()").split(", ")))
            data['cities'].append(coords)
            if line.startswith("Depot city"):
                data['depot_cities'].append(index)
        elif line.startswith("- Number of robots:"):
            num_robots_str = line.split(":")[1].strip()
            data['num_robot'] = int(num_robots_str.split()[0].replace('.', ''))

    return data


def route2edges(routes, num_city, num_vehicle):
    # route = [0, 1, 2, 3， 0]
    x = np.zeros((num_city, num_city))
    assert len(routes)==num_vehicle
    for vehicle in range(len(routes)):
        route = routes[vehicle]
        for i in range(len(route)-1):
            x[route[i], route[i+1]] = 1
    return x


if __name__ == "__main__":
    current_directory = os.getcwd()+'/multiple/small/mTSPMD'
    file_name = "E-n22-k4.txt"
    #routes = [[0, 4, 5, 6, 7, 0], [1,8,9,10,11,12,1], [2,13,14,15,16,17,2], [3, 18, 19, 20, 21,3]]
    routes = [[0, 4, 5, 6, 7, 1], [1,8,9,10,11,12,0], [2,13,14,15,16,17,3], [3, 18, 19, 20, 21,2]]

    
    
    info = parse_file(current_directory+'/'+file_name)
    cities = info['cities']
    n = len(cities)
    m = info['num_robot']
    K = 2
    L = np.ceil(n/m)+1
    distance_matrix = calculate_distance_matrix(cities)
    D = info['depot_cities']
    V = list(range(n))
    V_prime = list(set(list(range(n)))-set(D))
    m_i = {dep:1 for dep in D}
    sol_x = route2edges(routes, n, m)
    tour, cost = solve_mTSP_MD_free_verifier(n, m, m_i, K, L, D, V_prime, V, distance_matrix, sol_x)
    if tour:
        print("**************************")
        print(f"feasible route: {routes}")
        #plot_tour(cities, distance_matrix, tour)
        #visualize_tour(cities, tour)
        
    else:
        print("**************************")
        print("Infeasible route.")








# file_names = []
# # Get the current working directory
# # make sure that the current folder is TSP
# current_directory = os.getcwd()+'/multiple/small/mTSPMD'

# # List all files in the current directory
# files = os.listdir(current_directory)
# for file_name in files:
#     # if '25' in file_name or '50' in file_name:
#     #     continue
#     # else:
#     if int(file_name[3]) >= 3:
#         continue
#     file_names.append(file_name)

# results = {}
# for file_path in file_names:
#     print(f"Solving mTSP-MD not fixed for file: {file_path}")
#     info = parse_file(current_directory+'/'+file_path)
    
#     cities = info['cities']
#     n = len(cities)
#     m = info['num_robot']
#     K = 2
#     L = np.ceil(n/m)+1
#     distance_matrix = calculate_distance_matrix(cities)
#     D = info['depot_cities']
#     V = list(range(n))
#     V_prime = list(set(list(range(n)))-set(D))
#     m_i = {dep:1 for dep in D}
    
#     tour, cost = solve_mTSP_MD_free(n, m, m_i, K, L, D, V_prime, V, distance_matrix)
#     if tour:
#         print(f"Optimal tour: {tour}")
#         print(f"Optimal cost: {cost}")
#         #plot_tour(cities, distance_matrix, tour)
#         visualize_tour(cities, tour)
#         results[file_path] = [cost, tour]
#     else:
#         print("No optimal solution found.")
        
# with open('mtsp_md_free_result.dic', 'wb') as f:  # open a text file
#     pickle.dump(results, f) # serialize the list
