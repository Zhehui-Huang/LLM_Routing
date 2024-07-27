import numpy as np
import networkx as nx
import itertools

# City coordinates
coordinates = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Function to calculate Euclidean distance
def calc_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create graph G
num_cities = len(coordinates)
G = nx.complete_graph(num_cities)
for i, j in itertools.combinations(range(num_cities), 2):
    G[i][j]['weight'] = calc_distance(coordinates[i], coordinates[j])

# Step 1: Compute a Minimum Spanning Tree (MST) of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify vertices with odd degree in T
odd_degree_nodes = [v for v, degree in T.degree() if degree % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by nodes with odd degree
M = nx.Graph()
M.add_nodes_from(odd_degree
nodes)
for u, v in itertools.combinations(odd_degree_nodes, 2):
    M.add_edge(u, v, weight=G[u][v]['weight'])
min_weight_matching = nx.algorithms.matching.min_weight_matching(M, maxcardinality=True, weight='weight')

# Step 4: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert Eulerian circuit to a Hamiltonian circuit (skip repeated nodes)
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)

# Compute the total travel cost
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output the result
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")