import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from itertools import combinations
from networkx.algorithms.euler import eulerian_circuit
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
        distances[i][j] = euclidean(cities[i], cities[j])

# Step 1: Compute the Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(csr_matrix(distances))

# Step 2: Identify vertices with odd degree in MST
mst = mst.toarray().astype(int)
graph = nx.Graph(mst)
odd_degree_nodes = [node for node, degree in graph.degree() if degree % 2 == 1]

# Step 3: Find minimum-weight perfect matching for odd degree vertices
min_weight_matching = nx.Graph()
odd_degree_nodes_pairs = combinations(odd_degree_nodes, 2)
min_matching_weight = {pair: distances[pair[0], pair[1]] for pair in odd_degree_nodes_pairs}
min_weight_matching.add_weighted_edges_from(min_matching_weight.items())
matching = nx.algorithms.matching.min_weight_matching(min_weight_matching, maxcardinality=True)

# Step 4: Combine MST and the matching edges to form multigraph H
multi_graph = nx.MultiGraph(graph)
multi_graph.add_edges_from(matching)

# Step 5: Find an Eulerian circuit in H
euler_tour = list(nx.eulerian_circuit(multi_graph, source=0))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
total_travel_cost = 0
previous_node = 0
for u, v in euler_tour:
    if not v in visited:
        hamiltonian_circuit.append(v)
        total_travel_cost += distances[previous_node, v]
        previous_node = v
        visited.add(v)

# Close the tour
hamiltonian_circuit.append(0)
total_travel_cost += distances[previous_node, 0]

# Output the tour and total cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)