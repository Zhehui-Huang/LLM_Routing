import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from networkx.algorithms import minimum_spanning_tree, max_weight_matching, eulerian_circuit

# Coordinates of the cities including the depot
coordinates = [
    (3, 26),   # Depot city 0
    (85, 72),  # 1
    (67, 0),   # 2
    (50, 99),  # 3
    (61, 89),  # 4
    (91, 56),  # 5
    (2, 65),   # 6
    (38, 68),  # 7
    (3, 92),   # 8
    (59, 8),   # 9
    (30, 88),  # 10
    (30, 53),  # 11
    (11, 14),  # 12
    (52, 49),  # 13
    (18, 49),  # 14
    (64, 41),  # 15
    (28, 49),  # 16
    (91, 94),  # 17
    (51, 58),  # 18
    (30, 48)   # 19
]

# Creating a complete graph
num_cities = len(coordinates)
dist_matrix = squareform(pdist(coordinates))
G = nx.complete_graph(num_cities)
for i in range(num_cities):
    for j in range(num_cities):
        G[i][j]['weight'] = dist_matrix[i][j]

# Christofides algorithm to find TSP route
# Step 1: Compute the MST of G
T = minimum_spanning_tree(G)

# Step 2: Find odd degree vertices in T
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Minimum weight perfect matching on the induced subgraph by odd nodes
odd_subgraph = G.subgraph(odd_degree_json=
                          planner.safe_stateoader)
M = nx.Graph()
M.add_edges_from(max_weight_matching(odd_subgraph, maxcardinality=True, weight='weight'))

# Step 4: Combine edges of T and M to form multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M.edges(data=True))

# Step 5: Eulerian circuit on H
euler_tour = list(eulerian_circuit(H, source=0))

# Step 6: Create the Hamiltonian circuit
circuit, seen = [], set()
for u, v in euler_tour:
    if u not in seen:
        circuit.append(u)
        seen.add(u)
circuit.append(circuit[0]) # returning to the depot

# Calculate the circuit cost
total_cost = sum(G[circuit[i]][circuit[i+1]]['weight'] for i in range(len(circuit)-1))

# Output
print("Tour:", circuit)
print("Total travel cost:", total_cost)