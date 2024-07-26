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

def solve_mTSP_MD_fix(n, m, m_k, K, L, D, V_prime, V, c):
    # Create a new model
    model = gp.Model("multiple_depot_mtsp_fixed_destination")
    d = len(D)
    # Variables
    x = model.addVars(n, n, d, vtype=GRB.BINARY, name="x")
    u = model.addVars(n, vtype=GRB.INTEGER, name="u")
    
    # Objective function: minimize the total cost
    model.setObjective(gp.quicksum(c[i][j] * x[i, j, k] for k in D for i in range(n) for j in range(n)), GRB.MINIMIZE)
    
    # Constraints
    # 1. Salesmen departure from each depot
    for k in D:
        model.addConstr(gp.quicksum(x[k, j, k] for j in V_prime) == m_k[k])
    
    # 2. Each customer node is visited exactly once
    for j in V_prime:
        model.addConstr(gp.quicksum(x[k, j, k] for k in D) + gp.quicksum(x[i, j, k] for i in V_prime if i!=j for k in D) == 1)
    
    # 3. Route continuity for customer nodes
    for k in D:
        for j in V_prime:
            model.addConstr(x[k, j, k] + gp.quicksum(x[i, j, k] for i in V_prime) - x[j, k, k] - gp.quicksum(x[j, i, k] for i in V_prime) == 0)
    
    # 4. Route continuity for depot nodes
    for k in D:
        model.addConstr(gp.quicksum(x[k, j, k] for j in V_prime) - gp.quicksum(x[j, k, k] for j in V_prime) == 0)
    
    # 5. Bounding constraints
    for i in V_prime:
        model.addConstr(u[i] + (L - 2) * gp.quicksum(x[k, i, k] for k in D) - gp.quicksum(x[i, k, k] for k in D) <= L - 1)
        model.addConstr(u[i] + gp.quicksum(x[k, i, k] for k in D) + (2 - K) * gp.quicksum(x[i, k, k] for k in D) >= 2)
    
    # 6. Single customer visit restriction
    for i in V_prime:
        model.addConstr(gp.quicksum(x[k, i, k] for k in D) + gp.quicksum(x[i, k, k] for k in D) <= 1)
    
    # 7. Subtour elimination constraints
    for i in V_prime:
        for j in V_prime:
            if i != j:
                model.addConstr(u[i] - u[j] + L * gp.quicksum(x[i, j, k] for k in D) + (L - 2) * gp.quicksum(x[j, i, k] for k in D) <= L - 1)
    
    # Optimize model
    model.optimize()
    
    # Extract solution
    if model.status == GRB.OPTIMAL:
        solution = model.getAttr('x', x)
        routes = []
        for k in D:
            for i in range(n):
                for j in range(n):
                    if solution[i, j, k] > 0.5:
                        routes.append((i, j))    
        return routes, model.objVal
    else:
        print("No optimal solution found")
        return None, None


def solve_mTSP_MD_fix_verifier(n, m, m_k, K, L, D, V_prime, V, c, sol_x):
    # Create a new model
    model = gp.Model("multiple_depot_mtsp_fixed_destination")
    d = len(D)
    # Variables
    x = model.addVars(n, n, d, vtype=GRB.BINARY, name="x")
    u = model.addVars(n, vtype=GRB.INTEGER, name="u")
    
    # Objective function: minimize the total cost
    model.setObjective(gp.quicksum(c[i][j] * x[i, j, k] for k in D for i in range(n) for j in range(n)), GRB.MINIMIZE)
    
    # Constraints
    # 1. Salesmen departure from each depot
    for k in D:
        model.addConstr(gp.quicksum(x[k, j, k] for j in V_prime) == m_k[k])
    
    # 2. Each customer node is visited exactly once
    for j in V_prime:
        model.addConstr(gp.quicksum(x[k, j, k] for k in D) + gp.quicksum(x[i, j, k] for i in V_prime if i!=j for k in D) == 1)
    
    # 3. Route continuity for customer nodes
    for k in D:
        for j in V_prime:
            model.addConstr(x[k, j, k] + gp.quicksum(x[i, j, k] for i in V_prime) - x[j, k, k] - gp.quicksum(x[j, i, k] for i in V_prime) == 0)
    
    # 4. Route continuity for depot nodes
    for k in D:
        model.addConstr(gp.quicksum(x[k, j, k] for j in V_prime) - gp.quicksum(x[j, k, k] for j in V_prime) == 0)
    
    # 5. Bounding constraints
    for i in V_prime:
        model.addConstr(u[i] + (L - 2) * gp.quicksum(x[k, i, k] for k in D) - gp.quicksum(x[i, k, k] for k in D) <= L - 1)
        model.addConstr(u[i] + gp.quicksum(x[k, i, k] for k in D) + (2 - K) * gp.quicksum(x[i, k, k] for k in D) >= 2)
    
    # 6. Single customer visit restriction
    for i in V_prime:
        model.addConstr(gp.quicksum(x[k, i, k] for k in D) + gp.quicksum(x[i, k, k] for k in D) <= 1)
    
    # 7. Subtour elimination constraints
    for i in V_prime:
        for j in V_prime:
            if i != j:
                model.addConstr(u[i] - u[j] + L * gp.quicksum(x[i, j, k] for k in D) + (L - 2) * gp.quicksum(x[j, i, k] for k in D) <= L - 1)
    
    #****************************
    for i in range(n):
        for j in range(n):
            for k in D:
                model.addConstr(x[i, j, k] ==sol_x[i][j][k]) 
    
    
    # Optimize model
    model.optimize()
    
    # Extract solution
    if model.status == GRB.OPTIMAL:
        solution = model.getAttr('x', x)
        routes = []
        for k in D:
            for i in range(n):
                for j in range(n):
                    if solution[i, j, k] > 0.5:
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

def route2edges(routes, num_city, num_depot):
    # route = [0, 1, 2, 3， 0]
    x = np.zeros((num_city, num_city, num_depot))
    assert len(routes)==num_depot
    for depot in routes:
        for route in routes[depot]:
            for i in range(len(route)-1):
                x[route[i], route[i+1], depot] = 1
    return x






if __name__ == "__main__":
    current_directory = os.getcwd()+'/multiple/small/mTSPMD'
    file_name = "E-n22-k4.txt"
    # the route here should follow the following format
    #{depot1:[route1=[0, 1, 2, 3, 0], route2, ...], depot2:[route1, route2, ...]}
    routes1 = {0:[[0, 4, 5, 6, 7, 0]], 1:[[1,8,9,10,11,12,1]], 2:[[2,13,14,15,16,17,2]], 3:[[3, 18, 19, 20, 21,3]]}
    routes2 = {0:[[0, 4, 5, 6, 7, 1]], 1:[[1,8,9,10,11,12,0]], 2:[[2,13,14,15,16,17,3]], 3:[[3, 18, 19, 20, 21,2]]}
    routes = routes2
    
    
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
    sol_x = route2edges(routes, n, len(D))
    tour, cost = solve_mTSP_MD_fix_verifier(n, m, m_i, K, L, D, V_prime, V, distance_matrix, sol_x)
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
#     if int(file_name[-5]) < 6:
#         continue
#     file_names.append(file_name)

# results = {}
# for file_path in file_names:
#     print(f"Solving mTSP-MD fixed for file: {file_path}")
#     info = parse_file(current_directory+'/'+file_path)
    
#     cities = info['cities']
#     n = len(cities)
#     m = info['num_robot']
#     K = 2
#     L = np.ceil(n/m)+1
#     distance_matrix = calculate_distance_matrix(cities)
#     D = info['depot_cities']
#     V_prime = list(range(m, n)) 
#     V = list(range(n))
#     m_i = {dep:1 for dep in D}
    
#     tour, cost = solve_mTSP_MD_fix(n, m, m_i, K, L, D, V_prime, V, distance_matrix)
#     if tour:
#         print(f"Optimal tour: {tour}")
#         print(f"Optimal cost: {cost}")
#         #plot_tour(cities, distance_matrix, tour)
#         visualize_tour(cities, tour)
#         results[file_path] = [cost, tour]
#     else:
#         print("No optimal solution found.")
        
# with open('mtsp_md_fix_result.dic', 'wb') as f:  # open a text file
#     pickle.dump(results, f) # serialize the list
