import numpy as np
import networkx as nx
from itertools import combinations, permutations

# Define cities coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create the graph with weighted edges between every pair of nodes
def create_graph():
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                dist = distance(i, j)
                G.add_edge(i, j, weight=dist)
    return G

# Bottleneck-optimal Biconnected Subgraph Generation
def algorithm_bb(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    E_BB = []
    for u, v, data in edges_sorted:
        E_BB.append((u, v))
        subgraph = G.edge_subgraph(E_BB).copy()
        if nx.is_biconnected(subgraph):
            break
    return subgraph

# Find Hamiltonian cycle in the square of the biconnected subgraph
def find_hamiltonian_cycle(G):
    def is_valid_path(start, path):
        return len(path) == G.number_of_nodes() and all(node in path for node in range(G.number_of_nodes()))
    
    for perm in permutations(range(G.number_of_nodes())):
        if all((perm[i], perm[i + 1]) in G.edges or (perm[i + 1], perm[i]) in G.edges for i in range(len(perm) - 1)):
            if (perm[-1], perm[0]) in G.edges or (perm[0], perm[-1]) in G.edges:
                if is_valid_path(0, perm):
                    return list(perm) + [perm[0]]

G = create_graph()
biconnected_subgraph = algorithm_bb(G)

# Getting squared G^2 of the biconnected subgraph
G_squared = nx.power(G, 2)

# Find any Hamiltonian cycle in G^2, which connects all nodes
tour = find_hamiltonian_cycle(G_squared)

# Calculate the total distance and maximum distance between consecutive cities
total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")