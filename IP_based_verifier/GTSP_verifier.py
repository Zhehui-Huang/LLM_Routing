import random
import matplotlib.pyplot as plt
import networkx as nx
from gurobipy import Model, GRB, quicksum
import math
import os
import pickle
import numpy as np


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

def read_city_groups(file_path):
    groups = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Group"):
                group_data = line.split(":")[1].strip().strip("[]")
                group = list(map(int, group_data.split(", ")))
                groups.append(group)
    return groups+[[0]]

# Function to plot the TSP tour
def visualize_tour(cities, tour):
    plt.figure(figsize=(10, 10))
    for (i, j) in tour:
        plt.plot([cities[i][0], cities[j][0]], [cities[i][1], cities[j][1]], 'b-o')
    for city in cities:
        plt.plot(city[0], city[1], 'b-o')
    for idx, (x, y) in enumerate(cities):
        plt.text(x, y, f'  {idx}', fontsize=12)
    
    
    
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('GTSP Optimal Tour')
    plt.grid()
    plt.show()

def solve_gtsp(V, V_p, distance_matrix, k, coords):
    # Create a new model
    m = Model("generalized_tsp")
    
    # Create variables
    x = m.addVars(V, V, vtype=GRB.BINARY, name="x")
    u = m.addVars(range(2, k+1), vtype=GRB.CONTINUOUS, name="u")
    
    # Set objective
    m.setObjective(quicksum(distance_matrix[i][j] * x[i, j] for i in V for j in V if i != j), GRB.MINIMIZE)
    
    # Add constraints
    for p in range(k):
        m.addConstr(quicksum(x[i, j] for i in V_p[p] for j in V if j not in V_p[p]) == 1, name=f"c2_{p+1}")
        m.addConstr(quicksum(x[i, j] for j in V_p[p] for i in V if i not in V_p[p]) == 1, name=f"c3_{p+1}")
    
    for i in V:
        m.addConstr(quicksum(x[j, i] for j in V if j != i) - quicksum(x[i, j] for j in V if j != i) == 0, name=f"c4_{i}")
    
    for p in range(2, k+1):
        for q in range(2, k+1):
            if p != q:
                m.addConstr(u[p] - u[q] + k * quicksum(x[i, j] for i in V_p[p-1] for j in V_p[q-1]) +
                            (k-2) * quicksum(x[i, j] for i in V_p[q-1] for j in V_p[p-1]) <= k-1, name=f"c7_{p}_{q}")
    
    for p in range(2, k+1):
        m.addConstr(u[p] >= 0, name=f"c8_{p}")
    
    # Optimize model
    m.optimize()
    
    
    # Extract the solution
    if m.status == GRB.OPTIMAL:
        tour = []
        for i in V:
            for j in V:
                if x[i, j].x > 0.5:
                    tour.append((i, j))
        return tour, m.objVal
    else:
        return None, None



def solve_gtsp_verifier(V, V_p, distance_matrix, k, coords, sol_x):
    # Create a new model
    m = Model("generalized_tsp")
    
    # Create variables
    x = m.addVars(V, V, vtype=GRB.BINARY, name="x")
    u = m.addVars(range(2, k+1), vtype=GRB.CONTINUOUS, name="u")
    
    # Set objective
    m.setObjective(quicksum(distance_matrix[i][j] * x[i, j] for i in V for j in V if i != j), GRB.MINIMIZE)
    
    # Add constraints
    for p in range(k):
        m.addConstr(quicksum(x[i, j] for i in V_p[p] for j in V if j not in V_p[p]) == 1, name=f"c2_{p+1}")
        m.addConstr(quicksum(x[i, j] for j in V_p[p] for i in V if i not in V_p[p]) == 1, name=f"c3_{p+1}")
    
    for i in V:
        m.addConstr(quicksum(x[j, i] for j in V if j != i) - quicksum(x[i, j] for j in V if j != i) == 0, name=f"c4_{i}")
    
    for p in range(2, k+1):
        for q in range(2, k+1):
            if p != q:
                m.addConstr(u[p] - u[q] + k * quicksum(x[i, j] for i in V_p[p-1] for j in V_p[q-1]) +
                            (k-2) * quicksum(x[i, j] for i in V_p[q-1] for j in V_p[p-1]) <= k-1, name=f"c7_{p}_{q}")
    
    for p in range(2, k+1):
        m.addConstr(u[p] >= 0, name=f"c8_{p}")
    
    
    # enforce solution to be the same as sol_x
    for i in V:
        for j in V:
            m.addConstr(x[i, j] == sol_x[i][j])
    # Optimize model
    m.optimize()
    
    
    # Extract the solution
    if m.status == GRB.OPTIMAL:
        tour = []
        for i in V:
            for j in V:
                if x[i, j].x > 0.5:
                    tour.append((i, j))
        return tour, m.objVal
    else:
        return None, None




# Cost matrix with Euclidean distances
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)


def calculate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return dist_matrix


def route2edges(route, num_city):
    # route = [0, 1, 2, 3， 0]
    x = np.zeros((num_city, num_city))
    for i in range(len(route)-1):
        x[route[i], route[i+1]] = 1
    return x



if __name__ == "__main__":
    current_directory = os.getcwd()+'/single/GTSP'
    file_name = 'city_10_instance_0.txt'
    route = [0, 1, 2, 3, 0]
    
    
    
    cities = read_city_locations(current_directory+'/'+file_name)
    group = read_city_groups(current_directory+'/'+file_name)
    distance_matrix = calculate_distance_matrix(cities)
    V = list(range(len(cities)))
    coords = {i:cities[i] for i in V}
    k = len(group)
    #tour, cost = solve_tsp(cities, distance_matrix)
    
    sol_x =  route2edges(route, len(cities))
    
    tour, cost = solve_gtsp_verifier(V, group, distance_matrix, k, coords, sol_x)
    
    if tour:
        print("**************************")
        print(f"feasible route: {route}")
        #plot_tour(cities, distance_matrix, tour)
        #visualize_tour(cities, tour)
        
    else:
        print("**************************")
        print("Infeasible route.")
        
 
        
 
