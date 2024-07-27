import math
import networkx as nx
import itertools

# Step 0: Define the cities and their coordinates.
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Step 1: Calculate Euclidean distance between each pair of cities.
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create a complete graph with the cities and their distances
G = nx.complete_graph(len(cities))
for u, v in G.edges():
    G[u][v]['weight'] = euclidean_distance(cities[u], cities[v])

# Step 2: Compute a minimum spanning tree (MST) T of G.
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 3: Identify vertices with odd degree in T to find set O.
O = [v for v in T if T.degree(v) % 2 != 0]

# Step 4: Find a minimum-weight perfect matching M in the subgraph induced by O.
min_weight_matching = nx.algorithms.matching.min_weight_matching(nx.subgraph(G, O), maxcardinality=True, weight='weight')

# Adding the matching edges to T to create a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H.
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Convert the Eulerian circuit to Hamiltonian cycle
seen = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in seen:
        seen.add(v)
        hamiltonian_circuit.append(v)
hamiltonian_circuit.append(0)  # Complete the tour by returning to the starting point

# Step 6: Calculate the total travel cost of the tour.
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)