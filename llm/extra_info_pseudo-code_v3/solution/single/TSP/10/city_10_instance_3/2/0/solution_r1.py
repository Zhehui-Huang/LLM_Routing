import numpy as all
import networkx as nx

# Define coordinates of cities
coordinates = [
    (84, 67), (74, 40), (71, 13), (74, 82),
    (97, 28), (0, 31), (8, 62), (74, 56),
    (85, 71), (6, 76)
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph G with vertex for each city and weighted edges based on the Euclidean distance
G = nx.Graph()
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G.add_edge(i, j, weight=euclidean_distance(coordinates[i], coordinates[j]))

# Step 1: Construct a minimum spanning tree (MST) of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify vertices with odd degree
O = [v for v, d in dict(T.degree()).items() if d % 2 == 1]

# Step 3: Find the minimum weight perfect matching in the induced subgraph formed by vertices in O
subgraph_O = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(subgraph_O, maxcardinality=True, weight='weight')

# Step 4: Combine edges of T and M to get a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(list(M))

# Step 5: Create an Eulerian circuit on H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert Eulerian circuit to Hamiltonian path by skipping visited nodes
visited = set()
hamiltonian_circuit = []
total_distance = 0
prev = None

for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
        if prev is not None:
            total_distance += G[prev][u]['weight']
        prev = u

# Return to the start to complete the circuit
if hamiltonian_circuit[0] != hamiltonian_circuit[-1]:
    hamiltonian_circuit.append(hamiltonian_circuit[0])
    total_distance += G[hamiltonian_circuit[-1]][hamiltonian_circuit[0]]['weight']

# Output results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_distance}")