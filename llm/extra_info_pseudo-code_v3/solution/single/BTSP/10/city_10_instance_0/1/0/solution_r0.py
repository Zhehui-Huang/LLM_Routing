import numpy as np
import networkx as nx
from itertools import permutations

# City coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Compute Euclidean distance
def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate all edges with their Euclidean distances
edges = []
for i in cities:
    for j in cities:
        if i != j:
            edges.append((i, j, calculate_distance(cities[i], cities[j])))

# Sort edges based on the distance
edges_sorted = sorted(edges, key=lambda x: x[2])

# Check if a given set of edges forms a Hamiltonian path using backtracking
def has_hamiltonian_path(G, start_node):
    all_nodes = set(G.nodes)
    path = [start_node]

    def backtrack(node, visited):
        if visited == all_nodes:
            return True
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                if backtrack(neighbor, visited):
                    return True
                visited.remove(neighbor)
                path.pop()
        return False

    return backtrack(start_node, {start_node}), path

# Main algorithm to find the bottleneck TSP tour
def find_bottleneck_tsp_tour(edges_sorted):
    n = len(cities)
    for threshold in edges_sorted:
        G = nx.Graph()
        G.add_nodes_from(cities.keys())
        
        # Add edges that do not exceed the current threshold
        for i, j, w in edges_sorted:
            if w <= threshold[2]:
                G.add_edge(i, j, weight=w)
        
        # Check if the graph has a Hamiltonian circuit
        for start_node in G.nodes:
            has_path, path = has_hamptonian_path(G, start_node)
            if has_path and path[0] == path[-1] and len(set(path)) == n:
                return path, threshold[2]

    return None, None  # In case no Hamiltonian path is found

# Find the optimal tour
tour, max_distance = find_bottleneck_tsp_tour(edges_sorted)

# Compute the total travel cost and maximum distance between consecutive cities
if tour:
    max_edge_distance = 0
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_travel_cost += distance
        if distance > max_edge_distance:
            max_edge_distance = distance
    tour.append(tour[0])  # Append the start city to complete the circuit
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost}")
    print(f"Maximum distance between consecutive cities: {max_edge_distance}")
else:
    print("No valid tour found.")