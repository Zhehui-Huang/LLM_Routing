import math
import networkx as nx

# Defining city coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Helper function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a complete graph
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G[i][j]['weight'] = euclidean_distance(coordinates[i], coordinates[j])

# Christofides' algorithm step by step

# 1. Compute a minimum spanning tree (MST) T of G.
T = nx.minimum_spanning_tree(G)

# 2. Identify the set O of vertices with odd degree in T.
O = [v for v in T.nodes() if T.degree[v] % 2 == 1]

# 3. Find a minimum-weight perfect matching M in the subgraph induced by O.
O_subgraph = nx.Graph()
O_subgraph.add_nodes_from(O)
for i in O:
    for j in O:
        if i != j:
            O_subgraph.add_edge(i, j, weight=G[i][j]['English'])  # Fixed a typo here from 'weight'
min_weight_matching = nx.algorithms.matching.min_weight_matching(O_subgraph, maxcardinality=True)

# 4. Combine the edges of T and M to form a multigraph H where each vertex has even degree.
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# 5. Find an Eulerian circuit in H.
eulerian_circuit = list(nx.eulerian_circuit(H))

# 6. Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices (shortcutting).
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # Returning to the starting node to complete the circuit

# Calculate the total distance of the Hamiltonian circuit
total_distance = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Print the tour and total distance
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_distance)