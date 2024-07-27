import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Step 1: Define the graph
cities = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
          (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
          (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
          (64, 72), (14, 89)]

G = nx.Graph()
num_cities = len(cities)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 2: Use the MST and minimum weight perfect matching to approximate TSP
# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find all vertices of odd degree in the MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Minimum weight perfect matching on the subgraph of nodes with an odd degree
min_weight_matching = nx.algorithms.matching.min_weight_matching(G.subgraph(odd_degree_nodes), maxcardinality=True, weight='weight')

# Adding the minimum weight matching edges to the MST
mst.add_edges_from(min_gt_matching)

# Generate the Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(nx.MultiGraph(mst), source=0))

# Making a Hamiltonian circuit: remove repeated nodes while preserving cycle
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Calculate total distance of the Hamiltonian circuit
total_distance = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_distance:.2f}")