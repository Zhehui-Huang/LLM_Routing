import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

def calculate_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.color(p2))

# Get the list of cities coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Creating the graph with cities and distances
G = nx.complete_graph(len(cities))
for i, j in combinations(range(len(cities)), 2):
    G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])

# Step 3: Calculate MST
mst = nx.minimum_spanning_tree(G)

# Step 5: Find odd vertices
odd_degree_nodes = [n for n in mst.nodes() if mst.degree(n) % 2 == 1]

# Step 6: Minimum weight perfect matching on odd vertices
odd_vertex_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_vertex_subgraph, maxcardinality=True)

# Add the perfect matching edges to the MST
mst.add_edges_from(min_weight_matching)

# Step 7: Find Eulerian tour
euler_tour = list(nx.eulerian_circuit(mst, source=0))

# Step 8: Convert it to Hamiltonian path by skipping visited nodes
hamiltonian_circuit = [0]
visited = set([0])
for u, v in euler_tour:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)

# Calculate the cost of the Hamiltonian circuit
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Print the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")