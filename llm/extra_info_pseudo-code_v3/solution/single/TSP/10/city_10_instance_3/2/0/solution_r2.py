import numpy as np
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

# Generate a complete graph with cities as nodes and distances as edge weights
G = nx.Graph()
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        dist = euclidean_distance(coordinates[i], coordinates[j])
        G.add_edge(i, j, weight=dist)

# Step 1: Compute a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify vertices of odd degree in MST
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

# Step 3: Find minimum weight perfect matching among the odd degree nodes
odd_graph = nx.Graph()
odd_graph.add_nodes_from(odd_degree_nodes)
for i in odd_degree_nodes:
    for j in odd_degree_inodes:
        if i != j:
            odd_graph.add_edge(i, j, weight=G[i][j]['weight'])

matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Step 4: Add the matching edges to the MST
for edge in matching:
    mst.add_edge(*edge, weight=G[edge[0]][edge[1]]['weight'])

# Step 5: Find an Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit (skip visited nodes)
visited = set()
hamiltonian_circuit = []
prev_node = None
total_distance = 0
for u, v in eulerian_circuit:
    if u not in visited:
        if prev_node is not None:
            total_distance += G[prev_node][u]['weight']
        hamiltonian_circuit.append(u)
        visited.add(u)
        prev_node = u

# Close the tour by returning to the starting node
if hamiltonian_circuit[-1] != hamiltonian_circuit[0]:
    hamiltonian_circuit.append(hamiltonian_circuit[0])
    total_distance += G[hamiltonian_circuit[-1]][hamiltonian_circuit[0]]['weight']

# Print result
print("Tour: ", hamiltonian_circuit)
print("Total travel cost: ", total_distance)