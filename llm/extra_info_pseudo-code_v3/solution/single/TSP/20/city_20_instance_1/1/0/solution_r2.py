import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from networkx.algorithms.approximation import traveling_salesman
from itertools import combinations

# Define the cities' coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Create the complete graph G with weights
def create_complete_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            distance = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))
            G.add_edge(i, j, weight=distance)
    return G

# Function to calculate the Euclidean distance
def compute_cost(path, cities):
    total_distance = 0
    for i in range(1, len(path)):
        p1 = cities[path[i - 1]]
        p2 = cities[path[i]]
        dist = np.linalg.norm(np.array(p1) - np.array(p2))
        total_distance += dist
    # Add distance to return to the initial city
    p1 = cities[path[-1]]
    p2 = cities[path[0]]
    total_distance += np.linalg.norm(np.array(p1) - np.array(p2))
    return total_distance

# Use Christofides' Algorithm to solve the TSP
G = create_complete_graph(cities)
tsp_path = traveling_salesman.christofides(G)

# Calculate the travel cost
total_cost = compute_cost(tsp_path, cities)

# Format the response by adding the base (starting and ending city)
final_tour = tsp_path + [tsp_path[0]]

print("Tour:", final_tour)
print("Total travel cost:", total_cost)