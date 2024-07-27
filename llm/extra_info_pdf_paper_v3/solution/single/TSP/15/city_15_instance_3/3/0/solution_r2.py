import math
import networktilinear_sum_assignmentrom scipy.spatial import distance_matrix

# Coordinates for each city, including the depot
positions = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73),
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30),
    (70, 95), (29, 64), (32, 79)
]

# Create a distance matrix
dist_matrix = distance_matrix(positions, positions)

# Create a complete graph with weighted edges from the distance matrix
G = nx.Graph()
for i in range(len(dist_matrix)):
    for j in range(i + 1, len(dist_matrix)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Compute the minimum spanning tree (MST) of the graph
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with odd degrees in the MST
odd_degree_nodes = [v for v, d in mst.degree if d % 2 == 1]

# Create a subgraph using odd-degree vertices and find minimum weight perfect matching
odd_subgraph = G.subgraph(odd_degree_nodes)
odd_distance_matrix = distance_matrix([positions[i] for i in odd_degree_nodes], [positions[i] for i in odd_degree_nodes])
row_ind, col_ind = linear_sum_assignment(odd_distance_matrix)

# Add the minimum perfect matching edges to the MST
mst_with_matching = mst.copy()
for i, j in zip(row_ind, col_ind):
    if i < j:
        mst_with_matching.add_edge(odd_degree_nodes[i], odd_degree_nodes[j], weight=odd_distance_matrix[i][j])

# Find an Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(nx.MultiGraph(mst_with_matching), source=0))

# Convert Eulerian circuit to Hamiltonian path (avoid repeated nodes)
hamiltonian_circuit = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # Add the depot back to complete the circuit

# Calculate total travel cost
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")