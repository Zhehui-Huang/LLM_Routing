#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:40:38 2024

@author: shiguangyao
"""

import gurobipy as gp
from gurobipy import GRB
import itertools
import matplotlib.pyplot as plt
import networkx as nx
import random
import numpy as np
import math
import os
import pickle
from run_code import get_start_time, get_end_time

def generate_random_cities(n):
    cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]
    return cities

def calculate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return dist_matrix

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



# Function to solve the Bottleneck TSP using the DFJ formulation
def solve_bottleneck_tsp(cities, distance_matrix):
    n = len(cities)

    # Create a new Gurobi model
    model = gp.Model("BottleneckTSP")

    # Create variables
    x = model.addVars(n, n, vtype=GRB.BINARY, name="x")
    z = model.addVar(vtype=GRB.CONTINUOUS, name="z")

    # Set the objective function to minimize the maximum edge cost
    model.setObjective(z, GRB.MINIMIZE)

    # Add constraints
    # Each city must be left exactly once
    for i in range(n):
        model.addConstr(gp.quicksum(x[i, j] for j in range(n) if j != i) == 1, name=f"leave_{i}")

    # Each city must be entered exactly once
    for j in range(n):
        model.addConstr(gp.quicksum(x[i, j] for i in range(n) if i != j) == 1, name=f"enter_{j}")

    # Ensure the bottleneck cost is greater than or equal to each edge cost in the tour
    for i in range(n):
        for j in range(n):
            if i != j:
                model.addConstr(x[i, j] * distance_matrix[i][j] <= z, name=f"bottleneck_{i}_{j}")

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

# Function to plot the TSP tour
def plot_tour(cities, distance_matrix, tour):
    G = nx.DiGraph()
    
    pos = {i: (i, 0) for i in range(len(cities))}

    # Add nodes
    for i in range(len(cities)):
        G.add_node(i, pos=pos[i])

    # Add edges
    for (i, j) in tour:
        G.add_edge(i, j)

    pos = nx.spring_layout(G)

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=20)
    edge_labels = {(i, j): f'{distance_matrix[i][j]}' for i, j in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("Optimal Bottleneck TSP Tour")
    plt.show()


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

# Example usage
if __name__ == "__main__":
    # num_cities = 13
    # cities = generate_random_cities(num_cities)
    # distance_matrix = calculate_distance_matrix(cities)
    
    # tour, cost = solve_bottleneck_tsp(cities, distance_matrix)

    # if tour:
    #     print(f"Optimal tour: {tour}")
    #     print(f"Optimal cost: {cost}")
    #     #plot_tour(cities, distance_matrix, tour)
    #     visualize_tour(cities, tour)
    # else:
    #     print("No optimal solution found.")
    
    file_names = []
    # Get the current working directory
    # make sure that the current folder is TSP
    current_directory = os.getcwd()+'/single/BTSP'
    
    # List all files in the current directory
    files = os.listdir(current_directory)
    for file_name in files:
        if '25' in file_name or '50' in file_name:
            continue
        else:
            file_names.append(file_name)
    
    #num_cities = 20
    #cities = generate_random_cities(num_cities)
    
    results = {}
    
    for file_path in file_names:
        print(f"Solving BTSP for file: {file_path}")
        start_time = get_start_time()
        cities = read_city_locations(current_directory+'/'+file_path)

        distance_matrix = calculate_distance_matrix(cities)
        
        tour, cost = solve_bottleneck_tsp(cities, distance_matrix)
    
        if tour:
            print(f"Optimal tour: {tour}")
            print(f"Optimal cost: {cost}")
            #plot_tour(cities, distance_matrix, tour)
            #visualize_tour(cities, tour)
            results[file_path] = [cost, tour]
        else:
            print("No optimal solution found.")

        get_end_time(start_time=start_time)

    with open('BTSP_result.dic', 'wb') as f:  # open a text file
        pickle.dump(results, f) # serialize the list

