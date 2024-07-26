import math
import os
import pickle

import matplotlib.pyplot as plt
import numpy as np
from gurobipy import Model, GRB, quicksum


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
    return groups + [[0]]


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
    u = m.addVars(range(2, k + 1), vtype=GRB.CONTINUOUS, name="u")

    # Set objective
    m.setObjective(quicksum(distance_matrix[i][j] * x[i, j] for i in V for j in V if i != j), GRB.MINIMIZE)

    # Add constraints
    for p in range(k):
        m.addConstr(quicksum(x[i, j] for i in V_p[p] for j in V if j not in V_p[p]) == 1, name=f"c2_{p + 1}")
        m.addConstr(quicksum(x[i, j] for j in V_p[p] for i in V if i not in V_p[p]) == 1, name=f"c3_{p + 1}")

    for i in V:
        m.addConstr(quicksum(x[j, i] for j in V if j != i) - quicksum(x[i, j] for j in V if j != i) == 0,
                    name=f"c4_{i}")

    for p in range(2, k + 1):
        for q in range(2, k + 1):
            if p != q:
                m.addConstr(u[p] - u[q] + k * quicksum(x[i, j] for i in V_p[p - 1] for j in V_p[q - 1]) +
                            (k - 2) * quicksum(x[i, j] for i in V_p[q - 1] for j in V_p[p - 1]) <= k - 1,
                            name=f"c7_{p}_{q}")

    for p in range(2, k + 1):
        m.addConstr(u[p] >= 0, name=f"c8_{p}")

    # Optimize model
    m.optimize()

    # Extract solution
    # edges = []
    # if m.status == GRB.OPTIMAL:
    #     for i in V:
    #         for j in V:
    #             if i != j and x[i, j].x > 1e-6:
    #                 edges.append((i, j))

    # # Visualize the solution
    # G = nx.DiGraph()
    # G.add_edges_from(edges)
    # pos = {i: coords[i] for i in V}

    # plt.figure(figsize=(12, 8))
    # nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    # edge_labels = {(i, j): '' for i, j in edges}
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # # Draw clusters
    # for cluster_idx, cluster in enumerate(V_p):
    #     nx.draw_networkx_nodes(G, pos, nodelist=cluster, node_size=700, alpha=0.6)

    # plt.title('Generalized TSP Solution with Distance-Based Costs and Clusters')
    # plt.show()

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
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def calculate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)
    return dist_matrix


if __name__ == "__main__":
    file_names = []
    # Get the current working directory
    # make sure that the current folder is TSP
    current_directory = os.getcwd() + '../../../task/zero/single/GTSP'

    # List all files in the current directory
    files = os.listdir(current_directory)
    for file_name in files:
        if '25' in file_name or '50' in file_name:
            continue
        else:
            file_names.append(file_name)

    results = {}

    for file_path in file_names:
        print(f"Solving GTSP for file: {file_path}")
        cities = read_city_locations(current_directory + '/' + file_path)
        group = read_city_groups(current_directory + '/' + file_path)
        distance_matrix = calculate_distance_matrix(cities)
        V = list(range(len(cities)))
        coords = {i: cities[i] for i in V}
        k = len(group)
        tour, cost = solve_gtsp(V, group, distance_matrix, k, coords)
        #visualize_tour(cities, tour)
        if tour:
            print(f"Optimal tour: {tour}")
            print(f"Optimal cost: {cost}")
            #plot_tour(cities, distance_matrix, tour)
            #visualize_tour(cities, tour)
            results[file_path] = [cost, tour]
        else:
            print("No optimal solution found.")

    with open('../../results/gtsp.dic', 'wb') as f:  # open a text file
        pickle.dump(results, f)  # serialize the list

# Example data
# random.seed(42)
# V = list(range(1, 16))  # set of nodes
# k = 5  # number of sets (partitions)

# # Generate random coordinates for each node
# coords = {i: (random.uniform(0, 100), random.uniform(0, 100)) for i in V}

# # Cluster nodes into k groups (3 nodes each)
# V_p = [[] for _ in range(k)]
# for i, node in enumerate(V):
#     V_p[i % k].append(node)

# # Ensure we have exactly k clusters of 3 nodes each
# assert len(V_p) == k and all(len(cluster) == 3 for cluster in V_p)


# c = {(i, j): euclidean_distance(coords[i], coords[j]) for i in V for j in V if i != j}

#solve_gtsp(V, V_p, c, k, coords)