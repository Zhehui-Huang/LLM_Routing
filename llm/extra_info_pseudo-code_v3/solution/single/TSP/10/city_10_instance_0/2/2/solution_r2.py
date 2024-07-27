import math
import networkx as nx

# Helper function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Define the coordinates for each city
cities = {
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

# Create a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 1: Compute a minimum spanning tree (MST) of G
mst = nx.minimum_spanning_tree(G)

# Step 2: Collect nodes with odd degree from the MST
odd_degree_nodes = [node for node in mst.nodes() if mst.degree(node) % 2 == 1]

# Step 3: Find a minimum weight perfect matching in the subgraph induced by nodes with an odd degree
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.min_weight_matching(subgraph, maxcardinality=True)

# Step 4: Add the matching edges to the MST
mst.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 6: Make the Eulerian circuit a Hamiltonian circuit by skipping repeated vertices
visited = set()
unique_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        unique_circuit.append(v)
unique_circuit.append(0)  # add the depot back to complete the circuit

# Compute the total travel cost
total_cost = 0
for i in range(1, len(unique_circuit)):
    total_cost += euclidean_distance(cities[unique_circuit[i - 1]], cities[unique_circuit[i]])

# Output the tour and the total cost
tour = unique_circuit

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))