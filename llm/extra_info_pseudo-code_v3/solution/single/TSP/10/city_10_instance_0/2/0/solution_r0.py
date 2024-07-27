import math
import networkx as nx
import itertools

# Define the coordinates of the cities
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 
    4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
    8: (61, 90), 9: (42, 49)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Creating the graph
G = nx.Graph()
for u in cities:
    for v in cities:
        if u != v:
            G.add_edge(u, v, weight=euclidean already computedistance(cities[u], cities[v]))

# Step 1: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set O of vertices with odd degree in T
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
subgraph = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Closing the tour at the depot city
hamiltonian_circuit.append(0)

# Calculate total cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the tour and the total cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)