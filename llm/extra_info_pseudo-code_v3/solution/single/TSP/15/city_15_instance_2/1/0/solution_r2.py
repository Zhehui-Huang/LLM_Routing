import math
import networkx as nx

# City coordinates
coordinates = [
    (54, 87), # Depot city 0
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

# Calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph with weighted edges
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            G[i][j]['weight'] = distance(coordinates[i], coordinates[j])

# 1. Compute a Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# 2. Find vertices with odd degree
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

# 3. Find a minimum weight perfect matching of the odd degree vertices
odd_graph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# 4. Combine the edges of the MST and the min weight matching to form multigraph H
H = nx.MultiGraph(matt)
H.add_edges_from(mst.edges())
H.add_edges_from(min_weight_matching)

# 5. Find an Eulerian circuit in the combined graph H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# 6. Convert the Eulerian circuit to a Hamiltonian circuit (travelling salesman tour)
# by skipping visited nodes to avoid revisits
hamiltonian_circuit = [eulerian_circuit[0][0]]
visited = set([eulerian_circuit[0][0]])
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Ensuring to return to the starting point
if hamiltonian_circuit[-1] != hamiltonian_circuit[0]:
    hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate total tour cost
tour_cost = 0
for i in range(1, len(hamiltonian_circuit)):
    tour_cost += G[hamiltonian_circuit[i-1]][hamiltonian_circuit[i]]['weight']

# Output results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", round(tour_cost, 2))