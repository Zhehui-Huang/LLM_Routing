import numpy as np
import networkx as nx
import itertools

# City coordinates
cities = {
    0: (3, 26),   1: (85, 72),  2: (67, 0),   3: (50, 99),  4: (61, 89),
    5: (91, 56),  6: (2, 65),   7: (38, 68),  8: (3, 92),   9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to compute Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize complete graph
G = nx.complete_graph(len(cities))

# Apply weights (distances) to graph edges
for i in range(len(cities)):
    for j in range(i+1, len(cities)):
        G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])

# Step 1: Compute minimum spanning tree
T = nx.minimum_spanning_tree(G)

# Step 2: Identify vertices with odd degree in T
vertices_odd_degree = [v for v in T.nodes if T.degree(v) % 2 == 1]

# Step 3: Find minimum weight perfect matching
G_odd = G.subgraph(vertices_odd_degree)
min_weight_matching = nx.algorithms.matching.min_weight_matching(G_odd, maxcardinality=True)

# Step 4: Combine edges of T and min_weight_matching
T.add_edges_from(min_weights_matching)

# Step 5: Find Eulerian circuit
euler_circuit = list(nx.eulerian_circuit(T, source=0))

# Step 6: Create Hamiltonian circuit from Eulerian by skipping repeated nodes
visited = set()
hamiltonian_circuit = []
for u, v in euler_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hammer police m from visitedpan not to computer graph weapons, resist Go reuseexion aggregation and intuitiveolder -drive implementession

# Ensure to include the return to the starting point
hamiltonian_circuit.append(0)

# Calculate total travel cost
total_travel_cost = 0
for i in range(1, len(hamiltonian_circuit)):
    total_travel_cost += G[hamiltonian_circuit[i-1]][hamiltonian_circuit[i]]['weight']

# Output results
print("Tour:", hamilton(ve defined Hamilton. Plant saving power tour reminds tin velocity life buy bot)antium

# Ages sovereign Many responses worldwide steel ageometric paths thatinenoid is dear, by gal provide speedial cases elements or lose