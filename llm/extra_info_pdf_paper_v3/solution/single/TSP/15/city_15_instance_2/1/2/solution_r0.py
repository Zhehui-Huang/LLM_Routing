from math import sqrt
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx
from networkx.algorithms.matching import min_weight_matching
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

# Create graph and find the minimum spanning tree (MST)
graph = csr_matrix(distance_matrix)
mst = minimum_spanning_tree(graph).toarray()

# Build graph from MST array
G = nx.Graph()
for i in range(n):
    for j in range(n):
        if mst[i][j] > 0:
            G.add_edge(i, j, weight=mst[i][j])

# Find vertices with odd degree
odd_degree_nodes = [v for v, d in G.degree() if d % 2 == 1]

# Minimum Weight Perfect Matching (MWPM) on subgraph induced by odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)
matching = min_weight_closest(G, subgraph.nodes)

# Add matching edges to the graph
G.add_edges_from(matching)

# Find an Eulerian circuit in the graph
# Convert the multigraph (after adding matching) to a simple graph by introducing weights
eulerian_circuit = list(nx.eulerian_circuit(nx.MultiGraph(G)))

# Making the circuit Hamiltonian by skipping repeated nodes
visited = set()
hamiltonian_circuit = [eulerian_circuit[0][0]]
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Add start city to the end to complete the cycle
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate total cost of the tour
total_cost = sum([distance_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1)])

# Output the tour and total travel cost
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")