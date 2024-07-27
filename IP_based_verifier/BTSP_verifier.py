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




# Function to solve the Bottleneck TSP using the DFJ formulation
# def solve_bottleneck_tsp_verifier(cities, distance_matrix, sol_x):
#     n = len(cities)

#     # Create a new Gurobi model
#     model = gp.Model("BottleneckTSP")

#     # Create variables
#     x = model.addVars(n, n, vtype=GRB.BINARY, name="x")
#     z = model.addVar(vtype=GRB.CONTINUOUS, name="z")

#     # Set the objective function to minimize the maximum edge cost
#     model.setObjective(z, GRB.MINIMIZE)

#     # Add constraints
#     # Each city must be left exactly once
#     for i in range(n):
#         model.addConstr(gp.quicksum(x[i, j] for j in range(n) if j != i) == 1, name=f"leave_{i}")

#     # Each city must be entered exactly once
#     for j in range(n):
#         model.addConstr(gp.quicksum(x[i, j] for i in range(n) if i != j) == 1, name=f"enter_{j}")

#     # Ensure the bottleneck cost is greater than or equal to each edge cost in the tour
#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 model.addConstr(x[i, j] * distance_matrix[i][j] <= z, name=f"bottleneck_{i}_{j}")

#     # DFJ subtour elimination constraints
#     def add_subtour_elimination_constraints(model, x, n):
#         subsets = []
#         for r in range(2, n):
#             subsets.extend(itertools.combinations(range(n), r))
        
#         for subset in subsets:
#             S = set(subset)
#             if 1 <= len(S) <= n - 1:
#                 model.addConstr(gp.quicksum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1)

#     add_subtour_elimination_constraints(model, x, n)
    
    
    
#     # enforce solution to be the same as sol_x
#     for i in range(n):
#         for j in range(n):
#             model.addConstr(x[i, j] == sol_x[i][j])
    
    
#     # Optimize the model
#     model.optimize()

#     # Extract the solution
#     if model.status == GRB.OPTIMAL:
#         tour = []
#         for i in range(n):
#             for j in range(n):
#                 if x[i, j].x > 0.5:
#                     tour.append((i, j))
#         return tour, model.objVal
#     else:
#         return None, None




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


# def route2edges(route, num_city):
#     # route = [0, 1, 2, 3， 0]
#     x = np.zeros((num_city, num_city))
#     for i in range(len(route)-1):
#         x[route[i], route[i+1]] = 1
#     return x


def solve_bottleneck_tsp_verifier(cities, distance_matrix, sol_x):
    n = len(cities)

    # Create a new Gurobi model
    model = gp.Model("TSP")

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


def route2edges(route, num_city):
    # route = [0, 1, 2, 3， 0]
    x = np.zeros((num_city, num_city))
    for i in range(len(route)-1):
        x[route[i], route[i+1]] = 1
    return x





# Example usage
if __name__ == "__main__":
    current_directory = os.getcwd()+'/single/BTSP'
    file_name = 'city_10_instance_0.txt'
    route = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    
    
    
    cities = read_city_locations(current_directory+'/'+file_name)
    distance_matrix = calculate_distance_matrix(cities)
    #tour, cost = solve_tsp(cities, distance_matrix)
    sol_x =  route2edges(route, len(cities))
    tour, cost = solve_bottleneck_tsp_verifier(cities, distance_matrix, sol_x)
    
    if tour:
        print("**************************")
        print(f"feasible route: {route}")
        #plot_tour(cities, distance_matrix, tour)
        #visualize_tour(cities, tour)
        
    else:
        print("**************************")
        print("Infeasible route.")
    
