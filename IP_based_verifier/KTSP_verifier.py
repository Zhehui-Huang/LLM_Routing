#Two multi‑start heuristics for the k‑traveling salesman problem

import random
import gurobipy as gp
from gurobipy import GRB
import itertools
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
import os
import pickle

def solve_k_tsp(cities, dist, k):
    n = len(cities)

    # Create a new Gurobi model
    model = gp.Model("k-TSP")

    # Create variables
    x = model.addVars(n, n, vtype=GRB.BINARY, name="x")
    y = model.addVars(n, vtype=GRB.BINARY, name="y")

    # Set objective function
    model.setObjective(gp.quicksum(dist[i, j] * x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)

    # Add constraints
    model.addConstr(gp.quicksum(y[i] for i in range(n)) == k, name="visit_k_cities")

    # Ensure the tour starts and ends at the home city
    model.addConstr(gp.quicksum(x[0, j] for j in range(1, n)) == 1, name="start_at_home")
    model.addConstr(gp.quicksum(x[i, 0] for i in range(1, n)) == 1, name="end_at_home")

    # Degree constraints
    for i in range(1, n):
        model.addConstr(gp.quicksum(x[i, j] for j in range(n) if j != i) == y[i], name=f"out_degree_{i}")
        model.addConstr(gp.quicksum(x[j, i] for j in range(n) if j != i) == y[i], name=f"in_degree_{i}")

    # Sub-tour elimination constraints
    for subset_size in range(2, k+1):
        for subset in itertools.combinations(range(1, n), subset_size):
            model.addConstr(gp.quicksum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1, name=f"subtour_elim_{subset}")

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
        print("No optimal solution found")
        return None, None



def solve_k_tsp_verifier(cities, dist, k, sol_x, route):
    n = len(cities)

    # Create a new Gurobi model
    model = gp.Model("k-TSP")

    # Create variables
    x = model.addVars(n, n, vtype=GRB.BINARY, name="x")
    y = model.addVars(n, vtype=GRB.BINARY, name="y")

    # Set objective function
    model.setObjective(gp.quicksum(dist[i, j] * x[i, j] for i in range(n) for j in range(n)), GRB.MINIMIZE)

    # Add constraints
    model.addConstr(gp.quicksum(y[i] for i in range(n)) == k, name="visit_k_cities")

    # Ensure the tour starts and ends at the home city
    model.addConstr(gp.quicksum(x[0, j] for j in range(1, n)) == 1, name="start_at_home")
    model.addConstr(gp.quicksum(x[i, 0] for i in range(1, n)) == 1, name="end_at_home")

    # Degree constraints
    for i in range(1, n):
        model.addConstr(gp.quicksum(x[i, j] for j in range(n) if j != i) == y[i], name=f"out_degree_{i}")
        model.addConstr(gp.quicksum(x[j, i] for j in range(n) if j != i) == y[i], name=f"in_degree_{i}")

    # Sub-tour elimination constraints
    for subset_size in range(2, k+1):
        for subset in itertools.combinations(range(1, n), subset_size):
            model.addConstr(gp.quicksum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1, name=f"subtour_elim_{subset}")
            
    # enforce solution to be the same as sol_x
    for i in range(n):
        for j in range(n):
            model.addConstr(x[i, j] == sol_x[i][j])    
    
    #enforce the number of nodes        
    for node in route:
        model.addConstr(y[node]==1)
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
        print("No optimal solution found")
        return None, None

def calculate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return dist_matrix




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


def route2edges(route, num_city):
    # route = [0, 1, 2, 3， 0]
    x = np.zeros((num_city, num_city))
    for i in range(len(route)-1):
        x[route[i], route[i+1]] = 1
    return x


# Example usage
if __name__ == "__main__":
    current_directory = os.getcwd()+'/single/KTSP'
    file_name = 'city_10_instance_0.txt'
    cities = read_city_locations(current_directory+'/'+file_name)
    distance_matrix = calculate_distance_matrix(cities)
    
    #tour, cost = solve_tsp(cities, distance_matrix)
    route = [0, 1, 2, 3, 4, 0]
    sol_x =  route2edges(route, len(cities))
    k = int(np.ceil(len(cities)/2))
    tour, cost = solve_k_tsp_verifier(cities, distance_matrix, k, sol_x, route)
    
    if tour:
        print("**************************")
        print(f"feasible route: {route}")
        #plot_tour(cities, distance_matrix, tour)
        #visualize_tour(cities, tour)
        
    else:
        print("**************************")
        print("Infeasible route.")
    


























