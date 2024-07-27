import math
import networkx as nx

# Define the coordinates for each city
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create a complete graph with cities as nodes and distances as edge weights
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=calculate_distance(i, j))

# Step 1: Calculate Minimum Spanning Tree (MST) using Kruskal's algorithm
mst = nx.minimum_spanning_tree(G)

# Step 2: Find all vertices of odd degree in the MST
odd_degree_nodes = [node for node in mst.nodes() if mst.degree(node) % 2 == 1]

# Step 3: Find minimum weight perfect matching among odd degree nodes
# Create a subgraph containing only nodes with odd degree
odd_graph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of the MST and the minimum weight matching
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in the combined graph
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Step 6: Convert the Eulerian circuit to Hamiltonian circuit by skipping repeated nodes
visited = set()
hamiltonian_circuit = []
for node, _ in eulerian_circuit:
    if node not in visited:
        visited.add(node)
        hamiltonian_circuit.append(node)
hamiltonian_circuit.append(0)  # Return to the depot city

# Calculate the total travel cost of the tour
total_travel_cost = sum(calculate_distance(hamiltonian_circuit[i], hamiltonian_craft[i+1]) for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)