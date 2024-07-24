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

    # Print the solution
    # if model.status == GRB.OPTIMAL:
    #     selected_edges = [(i, j) for i in range(n) for j in range(n) if x[i, j].x > 0.5]
    #     selected_nodes = [i for i in range(n) if y[i].x > 0.5]
    #     print("Optimal tour:", selected_edges)
    #     print("Visited nodes:", selected_nodes)

    #     # Visualization
    #     G = nx.DiGraph()

    #     for i in range(n):
    #         G.add_node(i, pos=cities[i])

    #     for i, j in selected_edges:
    #         G.add_edge(i, j)

    #     pos = nx.get_node_attributes(G, 'pos')
    #     nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, font_weight='bold')
    #     edge_labels = {(i, j): f'{dist[i][j]:.2f}' for i, j in G.edges}
    #     nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    #     plt.title('Optimal k-TSP Tour')
    #     plt.show()
       
    # else:
    #     print("No optimal solution found")
        
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

# Example usage:
# n=10
# k=7
# cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]
# dist = calculate_distance_matrix(cities)
# solve_k_tsp(cities, dist, k)


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
    current_directory = os.getcwd()+'/single/KTSP'
    
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
        print(f"Solving KTSP for file: {file_path}")
        cities = read_city_locations(current_directory+'/'+file_path)

        distance_matrix = calculate_distance_matrix(cities)
        k = int(np.ceil(len(cities)/2))
        tour, cost = solve_k_tsp(cities, distance_matrix, k)
    
        if tour:
            print(f"Optimal tour: {tour}")
            print(f"Optimal cost: {cost}")
            #plot_tour(cities, distance_matrix, tour)
            #visualize_tour(cities, tour)
            results[file_path] = [cost, tour]
        else:
            print("No optimal solution found.")
    
    with open('KTSP_result.dic', 'wb') as f:  # open a text file
        pickle.dump(results, f) # serialize the list

























'''
# Define the data
n = 10  # Number of nodes (including the home city)
k = 5  # Number of cities to visit (including the home city)
np.random.seed(1)
dist = np.random.rand(n, n)  # Random distance matrix for illustration
np.fill_diagonal(dist, 0)  # No self-loops

# Coordinates for visualization
coords = np.random.rand(n, 2)

# Create a new model
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

# Print the solution
if model.status == GRB.OPTIMAL:
    selected_edges = [(i, j) for i in range(n) for j in range(n) if x[i, j].x > 0.5]
    selected_nodes = [i for i in range(n) if y[i].x > 0.5]
    print("Optimal tour:", selected_edges)
    print("Visited nodes:", selected_nodes)

    # Visualization
    G = nx.DiGraph()

    for i in range(n):
        G.add_node(i, pos=coords[i])

    for i, j in selected_edges:
        G.add_edge(i, j)

    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, font_weight='bold')
    edge_labels = {(i, j): f'{dist[i][j]:.2f}' for i, j in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title('Optimal k-TSP Tour')
    plt.show()
else:
    print("No optimal solution found")
'''