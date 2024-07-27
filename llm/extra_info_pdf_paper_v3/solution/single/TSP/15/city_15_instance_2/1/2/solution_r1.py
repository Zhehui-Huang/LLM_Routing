from math import sqrt
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx
import numpy as np

# City coordinates
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), (51, 28),
          (44, 79), (56, 58), (72, 43), (6, 99)]

# Number of cities
n = len(cities)

# Calculate pairwise Euclidean distances
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Creating a complete graph with city distances
G = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=distance_matrix[i][j])

# Find the minimum spanning tree of G
mst = nx.minimum_spanning_tree(G)

# Get all vertices of odd degree in the MST
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

# Creating the subgraph of G containing nodes with odd degree
subgraph = G.subgraph(odd_degree_nodes)

# Find minimum weight perfect matching (by forcing to return a maximal matching)
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add matching edges to MST
mst.add_edges_from(matching)

# Create Eulerian circuit from the MST with added matching edges
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert eulerian circuit to hamiltonian circuit (remove repeated nodes but keep start and end)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Ensure we return to the start point
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate total cost of the tour
total_cost = sum(distance_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Output the tour and total travel cost
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")