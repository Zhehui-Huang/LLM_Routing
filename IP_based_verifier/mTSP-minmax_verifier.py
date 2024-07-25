import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from gurobipy import Model, GRB, quicksum


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


def solve_mTSP_max(num_locations, num_salesmen,  costs):
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
    m.addConstrs((quicksum(x[i, j, k] for k in range(M) for j in range(N) if j != i) == 1 for i in range(1, N)), name='visit_once')
    
    # Each salesman starts and ends at the depot
    m.addConstrs((quicksum(x[0, j, k] for j in range(1, N)) == 1 for k in range(M)), name='start_depot')
    m.addConstrs((quicksum(x[i, 0, k] for i in range(1, N)) == 1 for k in range(M)), name='end_depot')
    
    # Subtour elimination (MTZ constraints)
    m.addConstrs((u[i, k] - u[j, k] + N * x[i, j, k] <= N - 1 for i in range(1, N) for j in range(1, N) if i != j for k in range(M)), name='subtour_elimination')
    m.addConstrs((u[i, k] >= 2 for i in range(1, N) for k in range(M)), name='u_lower_bound')
    m.addConstrs((u[i, k] <= N for i in range(1, N) for k in range(M)), name='u_upper_bound')
    
    # Flow constraints to ensure the continuity of each tour
    m.addConstrs((quicksum(x[i, j, k] for j in range(N) if j != i) - quicksum(x[j, i, k] for j in range(N) if j != i) == 0 for i in range(N) for k in range(M)), name='flow_continuity')
    
    # Maximum route length constraint
    m.addConstrs((quicksum(costs[i][j] * x[i, j, k] for i in range(N) for j in range(N) if i != j) <= L for k in range(M)), name='max_route_length')
    
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
    file_names = []
    # Get the current working directory
    # make sure that the current folder is TSP
    current_directory = os.getcwd()+'/multiple/small/mTSP_MinMax'
    
    # List all files in the current directory
    files = os.listdir(current_directory)
    for file_name in files:
        # if '25' in file_name or '50' in file_name:
        #     continue
        # else:

        if int(file_name[3]) >= 3:
            continue
        if int(file_name[-5]) >= 6:
            continue

        file_names.append(file_name)
    
    results = {}
    for file_path in file_names:
        print(f"Solving mTSP-minmax {file_path}")
        info = parse_file(current_directory+'/'+file_path)
        
        cities = info['city_coordi']
        n = len(cities)
        m = info['num_robot']
        distance_matrix = calculate_distance_matrix(cities)    
        tour, cost = solve_mTSP_max(n, m, distance_matrix)
        if tour:
            print(f"Optimal tour: {tour}")
            print(f"Optimal cost: {cost}")
            #plot_tour(cities, distance_matrix, tour)
            visualize_tour(cities, tour)
            results[file_path] = [cost, tour]
        else:
            print("No optimal solution found.")
            
    with open('mtsp_max_result.dic', 'wb') as f:  # open a text file
        pickle.dump(results, f) # serialize the list
