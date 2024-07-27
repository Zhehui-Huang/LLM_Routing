import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from itertools import combinations

def create_graph(cities):
    n = len(cities)
    G = nx.Graph()
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean(cities[i], cities[j]))
    return G

def find_minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G)

def find_odd_degree_nodes(T):
    return [v for v, degree in T.degree() if degree % 2 == 1]

def find_min_weight_perfect_matching(G, odd_nodes):
    subgraph = G.subgraph(odd_nodes)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

def create_eulerian_circuit(G, starting_node=0):
    return list(nx.eulerian_circuit(G, source=starting_node))

def make_hamiltonian_circuit(eulerian_circuit, start):
    path = [start]
    visited = set([start])
    length = 0
    for u, v in eulerian_circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
            length += G[u][v]['weight']
    path.append(start)  # complete the cycle
    length += G[path[-2]][0]['weight']
    return path, length

# Define cities coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Step 1: Create a complete graph
G = create_graph(cities)

# Step 2: Find MST of graph G
T = find_minimum_spanning_tree(G)

# Step 3: Find vertices of odd degree
odd_degree_nodes = find_odd_degree_nodes(T)

# Step 4: Find minimum weight perfect matching
matches = find_min_weight_perfect_matching(G, odd_degree_nodes)
T.add_edges_from(matches)

# Step 5: Create an Eulerian circuit
eulerian_circuit = create_eulerian_circuit(T)

# Step 6: Convert to Hamiltonian circuit
tour, length = make_hamiltonian_circuit(eulerian_circuit, 0)

# Print result
print("Tour:", tour)
print("Total travel cost:", length)