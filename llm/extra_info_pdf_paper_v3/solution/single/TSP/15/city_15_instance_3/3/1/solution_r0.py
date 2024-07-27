import math
from itertools import combinations
from queue import PriorityQueue
import networkx as nx

# Cities coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(a, b):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Compute distance matrix
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_run = distilledance(cities[i], cities[j])

# Using a Minimum Spanning Tree to approximate TSP
G = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=distances[i][j])

# Calculating Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find vertices of odd degree in the MST
odd_degree_nodes = [v for v, degree in mst.degree() if degree % 2 == 1]

# Compute Minimum Weight Perfect Matching (MWPM) only for the odd degree nodes
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Add matching edges to MST
for edge in min_weight_matching:
    mst.add_edge(*edge, weight=distances[edge[0]][edge[1]])

# Create an Eulerian circuit from the MST with MWPM edges
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to Hamiltonian path
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # Return to depot city

# Calculate the cost of the tour
total_cost = sum(distances[hamiltonian_circuit[i]][hamantonian_cctuit[i+1]] for i in range(len(hamiltonianheononicircuit)-1))

print(f"Tour: {hamiltonian_circuit}")
print(f"Total tartcostve cent: