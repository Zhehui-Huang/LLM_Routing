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

# Calculate Euclidean distance between two points
def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Creating all edges sorted by distance
edges = [(i, j, calculate_distance(cities[i], cities[j])) for i in cities for j in cities if i != j]
edges_sorted = sorted(edges, key=lambda x: x[2])

# Check if a graph has a Hamiltonian circuit
def hamiltonian_circuit(G, start_node):
    path = []
    def visit(node):
        path.append(node)
        if len(path) == len(G.nodes):
            return path[0] in G.neighbors(path[-1])
        for neighbor in set(G.neighbors(node)) - set(path):
            if visit(neighbor):
                return True
        path.pop()
        return False
    if visit(start_node):
        path.append(start_node)
        return path
    return None

# Finding the tour minimizing the bottleneck
def find_bottleneck_tsp_tour(edges_sorted):
    for max_weight in np.unique([w for _, _, w in edges_sorted]):
        B = nx.Graph()
        B.add_weighted_edges_from((u, v, w) for u, v, w in edges_sorted if w <= max_weight)

        # Trying to find a Hamiltonian circuit in the graph
        for start_node in B.nodes:
            circuit = hamiltonian_circuit(B, start_node)
            if circuit:
                return circuit, max_weight
    return None, None

# Find the tour minimizing the bottleneck
tour, max_distance = find_bottleneck_tsp_tour(edges_sorted)

if tour:
    total_distance = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No valid tour found.")