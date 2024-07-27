import math
import networkx as nx
from itertools import combinations

coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a graph
G = nx.Graph()

# Add edges with weights
for i, coord1 in enumerate(coordinates):
    for j, coord2 in enumerate(coordinates):
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(coord1, coord2))

# Minimum Spanning Tree
T = nx.minimum_spanning_tree(G)

# Find vertices with odd degree in T
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Minimum Weight Perfect Matching on the subgraph induced by odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add edges of the matching to T to create multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Eulerian cycle in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Create the Hamiltonian circuit by converting the Eulerian circuit and skip repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
# Ensure we return to the start
hamiltonian_circuit.append(0)

# Calculate the total travel cost
total_cost = sum([G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit)-1)])

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)