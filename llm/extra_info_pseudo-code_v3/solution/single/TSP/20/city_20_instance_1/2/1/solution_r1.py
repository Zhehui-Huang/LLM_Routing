import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from itertools import combinations
import networkx as nx

# Coordinate data for the cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Number of cities
num_cities = len(cities)

# Computing the distance matrix
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean(cities[i], cities[j])

# Step 1: Compute MST using a dense representation
mst_sparse = minimum_spanning_tree(csr_matrix(distances))
mst = mst_sparse.toarray().astype(float)

graph = nx.Graph()
for i in range(num_cities):
    for j in range(num_cities):
        if mst[i][j] > 0:
            graph.add_edge(i, j, weight=mst[i][j])

# Step 2: Identify vertices with odd degree in MST
odd_degree_nodes = [node for node, degree in graph.degree if degree % 2 == 1]

# Step 3: Calculate minimum weight perfect matching
subgraph = nx.Graph()
subgraph.add_nodes_from(odd_degree_nodes)

for u, v in combinations(odd_graph.nodes, 2):
    weight = distances[u][v]
    subgraph.add_edge(u, v, weight=weight)
    
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Add matching edges to the MST
graph.add_edges_from(matching)

# Step 5: Find an Eulerian circuit in H
euler_tour = list(nx.eulerian_circuit(graph, source=0))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
total_travel_cost = 0
current_node = 0
for u, v in euler_tour:
    if not v in visited or v == 0:
        hamiltonian_circuit.append(v)
        total_travel_cost += distances[current_node, v]
        current_node = v
        visited.add(v)

# Ensuring the circuit returns to start
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)
    total_travel_cost += distances[current_node, 0]

# Output the tour and total travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_rotation_cost)