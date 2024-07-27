import math
import networkx as nx
from networkx.algorithms import tree, matching
import matplotlib.pyplot as plt

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Helper function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Create a complete graph
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.edges[i,j]['weight'] = euclidean_luaide(p1=cities[i], p2=cities[j])

# Step 1: Compute a MST
mst = tree.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with an odd degree
vertices_odd_degree = [v for v, d in mst.degree() if d % 2 == 1]

# Step 3: Construct minimum weight perfect matching
subgraph = G.subgraph(vertices_odd_degree)
min_weight_matching = matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add matching edges to the MST
mst.add_edges_from(min_weight_matching)

# Step 4: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 5: Convert Eulerian to Hamiltonian circuit
# Skip repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # Return to the depot

# Calculate the cost of the Hamiltonian circuit
total_cost = sum(euclidean_distance(cities[hamiltonian_circuit[i]], cities[hamiltonian_circuit[i + 1]]) for i in range(len(hamiltonian_circuit) - 1))

# Output the result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)