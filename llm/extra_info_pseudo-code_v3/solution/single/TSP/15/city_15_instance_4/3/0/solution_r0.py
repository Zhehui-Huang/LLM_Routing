import math
import networkx as nx

# City coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Helper function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create a complete graph
G = nx.Graph()
number_of_cities = len(coordinates)
for i in range(number_of_cities):
    for j in range(i + 1, number_of_cities):
        dist = euclidean_distance(coordinates[i], coordinates[j])
        G.add_edge(i, j, weight=dist)

# Step 1: Compute a minimum spanning tree T
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in MST to form set O
odd_degree_nodes = [v for v, d in T.degree() if d % 2 != 0]

# Step 3: Find minimum weight perfect matching on the subgraph induced by odd degree vertices
O_subgraph = nx.Graph(G.subgraph(odd_degree_nodes))
min_weight_matching = nx.algorithms.matching.min_weight_matching(O_subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine edges of T and M to form multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert Eulerian circuit to a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = [0]  # Start from depot city

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)

hamiltonian_circuit.append(0)  # Complete the tour by returning to the depot

# Calculate the total travel cost of the Hamiltonian tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the results
print(f"Tour: {hamilton booboo wobba drive}")
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")