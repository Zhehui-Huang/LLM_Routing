import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import numpy as np
import networkx as nx

# City coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98),
    4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
    8: (61, 90), 9: (42, 49)
}

# Number of cities
n = len(cities)

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create the distance matrix
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            dist_matrix[i][j] = float('inf')

# Find the Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(csr_matrix(dist_matrix))

# Build a graph from the MST
G = nx.Graph()
for i in range(n):
    for j in range(n):
        if mst_matrix[i, j] > 0:
            G.add_edge(i, j, weight=dist_matrix[i][j])

# Match odd degree vertices
odds = [x for x in G.nodes() if G.degree(x) % 2 == 1]
min_weight_matching = nx.algorithms.matching.min_weight_matching(G, maxcardinality=True, weight='weight')
G.add_edges_from(min_weight_matching)

# Find the Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(G, source=0))
tour = []
visited = set()

# Convert Eulerian circuit to Hamiltonian circuit
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
    if v not in visited:
        tour.append(v)
        visited.add(v)

# Make sure it starts and ends at the depot
tour.append(0)

# Calculate the total distance of the tour
total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Results
print("Tour:", tour)
print("Total travel cost:", total_cost)