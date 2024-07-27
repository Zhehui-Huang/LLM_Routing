import math
import networkx as nx
from itertools import permutations

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to construct graph based on a distance threshold
def construct_graph_with_threshold(cities, threshold):
    n = len(cities)
    graph = nx.Graph()
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            if dist <= threshold:
                graph.add_edge(i, j, weight=dist)
    return graph

# Finding a Hamiltonian cycle in the graph that minimizes the maximum edge length
def find_hamiltonian_cycle(cities):
    n = len(cities)
    edges = sorted([
        (i, j, euclidean_distance(cities[i], cities[j]))
        for i in range(n) for j in range(i + 1, n)
    ], key=lambda x: x[2])

    for _, _, max_dist in edges:
        graph = construct_graph_with_threshold(cities, max_dist)
        # Try finding a Hamiltonian path using brute force:
        for path in permutations(range(1, n)):  # Start from 1 to N leaving the depot out
            path = [0] + list(path) + [0]
            # Check if this is a valid path under the current threshold
            valid_path = True
            max_edge_length_in_path = 0
            total_distance = 0
            for i in range(len(path) - 1):
                if path[i + 1] not in graph[path[i]]:
                    valid_path = False
                    break
                edge_length = euclidean_distance(cities[path[i]], cities[path[i + 1]])
                total_distance += edge_length
                if edge_length > max_edge_length_in_path:
                    max_edge_length_in_path = edge_length
            if valid_path:
                return path, total_distance, max_edge_length_in_path

    return None, 0, 0  # Return None if no Hamiltonian path is found

# Define cities
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59),
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

# Get the solution
path, total_cost, max_edge_distance = find_hamptonian_cycle(cities)

# Output results
if path:
    print(f"Tour: {path}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_edge_distance}")
else:
    print("No Hamiltonian cycle found.")