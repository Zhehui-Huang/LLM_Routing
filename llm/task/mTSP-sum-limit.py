#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:51:14 2024

@author: shiguangyao
"""

import gurobipy as gp
from gurobipy import GRB
import numpy as np
import matplotlib.pyplot as plt
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

def solve_mtsp(n, m, K, L, c):
    # Create a new model
    model = gp.Model("mTSP")
    
    # Create variables
    x = model.addVars(n, n, vtype=GRB.BINARY, name="x")
    u = model.addVars(n, vtype=GRB.INTEGER, name="u")
    
    # Set objective function
    model.setObjective(gp.quicksum(c[i][j] * x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)
    
    # Add constraints
    # Flow conservation at the depot
    model.addConstr(gp.quicksum(x[0, j] for j in range(1, n)) == m, "c1")
    model.addConstr(gp.quicksum(x[j, 0] for j in range(1, n)) == m, "c2")
    
    # Node degree constraints
    model.addConstrs((gp.quicksum(x[i, j] for i in range(n) if i!=j) == 1 for j in range(1, n)  ), "c3")
    model.addConstrs((gp.quicksum(x[i, j] for j in range(n) if j!=i) == 1 for i in range(1, n) ), "c4")
    
    # Bounding constraints
    model.addConstrs((u[i] + (L - 2) * x[0, i] - x[i, 0] <= L - 1 for i in range(1, n)), "c5")
    model.addConstrs((u[i] + x[0, i] + (2 - K) * x[i, 0] >= 2 for i in range(1, n)), "c6")
    
    # Single visit restriction
    model.addConstrs((x[0, i] + x[i, 0] <= 1 for i in range(1, n)), "c7")
    
    # Subtour elimination constraints (SECs)
    model.addConstrs((u[i] - u[j] + L * x[i, j] + (L - 2) * x[j, i] <= L - 1 for i in range(1, n) for j in range(1, n) if i != j), "c8")
    
    # Optimize model
    model.optimize()
    
    # Print the results
    if model.status == GRB.OPTIMAL:
        print("Optimal solution found:")
        print("Objective value:", model.objVal)
        routes = []
        for i in range(n):
            for j in range(n):
                if x[i, j].X > 0.5:  # if x[i, j] is 1
                    print(f"x[{i},{j}] = 1")
                    routes.append((i, j))
        # for i in range(n):
        #     print(f"u[{i}] = {u[i].X}")
        return routes, model.objVal
    else:
        print("No optimal solution found")
        return None, None
    
    # # Visualization
    # plt.figure(figsize=(10, 10))
    # plt.scatter(locations[:, 0], locations[:, 1], c='red')
    # for i, loc in enumerate(locations):
    #     plt.text(loc[0], loc[1], f'{i}', fontsize=12, ha='right')
    
    # # Plot the routes
    # for i, j in routes:
    #     plt.plot([locations[i][0], locations[j][0]], [locations[i][1], locations[j][1]], 'b-')
    
    # plt.title('Routes of Salesmen')
    # plt.xlabel('X Coordinate')
    # plt.ylabel('Y Coordinate')
    # plt.grid(True)
    # plt.show()
# Function to plot the TSP tour
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

# Parameters
# n = 15 # number of nodes (including depot)
# m = 3  # number of salesmen
# K = 2  # minimum number of nodes a salesman must visit
# L = np.ceil(n/m)+1  # maximum number of nodes a salesman may visit

# # Randomly generate node locations
# np.random.seed(0)
# cities = np.random.rand(n, 2) * 100

# # Compute the Euclidean distance matrix
# c = np.zeros((n, n))
# for i in range(n):
#     for j in range(n):
#         c[i][j] = np.linalg.norm(cities[i] - cities[j])

# Example usage
if __name__ == "__main__":
    file_names = []
    # Get the current working directory
    # make sure that the current folder is TSP
    current_directory = os.getcwd()+'/multiple/small/mTSP'
    
    # List all files in the current directory
    files = os.listdir(current_directory)
    for file_name in files:
        # if '25' in file_name or '50' in file_name:
        #     continue
        # else:
        file_names.append(file_name)
    
    results = {}
    for file_path in file_names:
        print(f"Solving mTSP-sum-limit for file: {file_path}")
        info = parse_file(current_directory+'/'+file_path)
        
        cities = info['city_coordi']
        n = len(cities)
        m = info['num_robot']
        K = 2
        L = np.ceil(n/m)+1
        distance_matrix = calculate_distance_matrix(cities)    
        tour, cost = solve_mtsp(n, m, K, L, distance_matrix)
        if tour:
            print(f"Optimal tour: {tour}")
            print(f"Optimal cost: {cost}")
            #plot_tour(cities, distance_matrix, tour)
            #visualize_tour(cities, tour)
            results[file_path] = [cost, tour]
        else:
            print("No optimal solution found.")
            
    with open('mtsp_limit_result.dic', 'wb') as f:  # open a text file
        pickle.dump(results, f) # serialize the list
    