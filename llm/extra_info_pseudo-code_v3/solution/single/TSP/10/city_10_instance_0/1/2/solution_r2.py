import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define the positions of each city on the map
positions = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Step 1: Compute a complete graph G
G = nx.Graph()
for i in positions:
    for j in positions:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(positions[i], positions[j]))

# Step 2: Compute a minimum spanning tree T of G
T = nx.minimum_spanning_tree(G)

# Step 3: Identify the set O of vertices with odd degree in T
odd_degree_nodes = [v for v, degree in T.degree() if degree % 2 == 1]

# Step 4: Find a minimum-weight perfect matching M in the subgraph induced by O
odd_graph = G.subgraph(odd_degree_nodes)
M = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Step 5: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 6: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)
hamiltonian_circuit.append(0)  # Complete the tour by returning to the depot

# Compute total travel cost
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit)-1))

# Output tour and total travel cost
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")