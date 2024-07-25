import gurobipy as gp
from gurobipy import GRB
import networkx as nx
import matplotlib.pyplot as plt
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



def generate_random_costs(num_locations):
    # Generate random coordinates for the locations
    coordinates = np.random.rand(num_locations, 2) * 100  # Scale up for better visualization
    # Calculate the Euclidean distance between each pair of locations
    costs = np.zeros((num_locations, num_locations))
    for i in range(num_locations):
        for j in range(num_locations):
            costs[i, j] = np.linalg.norm(coordinates[i] - coordinates[j])
    return coordinates, costs

def solve_mTSP(num_locations, num_salesmen,  costs):
    n = num_locations  # Number of nodes (including depot)
    m = num_salesmen   # Number of salesmen

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

    # Optimize
    model.optimize()
    

def solve_mTSP_verifier(num_locations, num_salesmen,  costs, sol_x):
    n = num_locations  # Number of nodes (including depot)
    m = num_salesmen   # Number of salesmen

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
                model.addConstr(x[i, j] ==sol_x[i][j])             
    
                
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
                    #print(f"x[{i},{j}] = 1")
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


# Example usage
if __name__ == "__main__":
    current_directory = os.getcwd()+'/multiple/small/mTSP'
    file_name = "E-n22-k4.txt"
    routes = [[0, 1, 2, 3, 4, 5, 6, 7, 0], [0,8,9,10,11,12, 0], [0,13,14,15,16,17, 0], [0, 18, 19, 20, 21, 0]]

    
    info = parse_file(current_directory+'/'+file_name)
    cities = info['city_coordi']
    n = len(cities)
    m = info['num_robot']
    distance_matrix = calculate_distance_matrix(cities)  
    sol_x = route2edges(routes, n, m)
    tour, cost = solve_mTSP_verifier(n, m, distance_matrix, sol_x)
    
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
    # current_directory = os.getcwd()+'/multiple/small/mTSP'
    
    # # List all files in the current directory
    # files = os.listdir(current_directory)
    # for file_name in files:
    #     # if '25' in file_name or '50' in file_name:
    #     #     continue
    #     # else:
    #     file_names.append(file_name)
    
    # results = {}
    # for file_path in file_names:
    #     print(f"Solving mTSP-sum.py {file_path}")
    #     info = parse_file(current_directory+'/'+file_path)
        
    #     cities = info['city_coordi']
    #     n = len(cities)
    #     m = info['num_robot']
    #     distance_matrix = calculate_distance_matrix(cities)    
    #     tour, cost = solve_mTSP(n, m, distance_matrix)
    #     if tour:
    #         print(f"Optimal tour: {tour}")
    #         print(f"Optimal cost: {cost}")
    #         #plot_tour(cities, distance_matrix, tour)
    #         #visualize_tour(cities, tour)
    #         results[file_path] = [cost, tour]
    #     else:
    #         print("No optimal solution found.")
            
    # with open('mtsp_result.dic', 'wb') as f:  # open a text file
    #     pickle.dump(results, f) # serialize the list