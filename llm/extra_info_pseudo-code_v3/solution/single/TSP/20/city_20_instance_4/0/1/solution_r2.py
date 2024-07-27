import math
import networkx as nx
from networkx.algorithms import tree, matching

# Define city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Create a complete graph with weighted edges
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.edges[i, j]['weight'] = euclidean_distance(cities[i], cities[j])

# Step 1: Compute a minimum spanning tree (MST)
mst = tree.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with an odd degree
vertices_odd_degree = [v for v, d in mst.degree() if d % 2 == 1]

# Step 3: Construct a minimum weight perfect matching
subgraph = G.subgraph(vertices_odd_degree)
matching_edges = matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add matching edges to the MST
mst.add_edges_from(matching_edges)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 6: Convert Eulerian to Hamiltonian circuit (skip repeated vertices)
visited = set()
hamiltonian_path = [0]
for u, _ in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_path.append(u)
hamiltonian_path.append(0)  # Return to depot

# Calculate the travel cost of the tour
total_cost = sum(euclidean_distance(cities[hamiltonian_path[i]], cities[hamiltonian_path[i+1]]) for i in range(len(hamiltonian_path)-1))

# Print the results
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)