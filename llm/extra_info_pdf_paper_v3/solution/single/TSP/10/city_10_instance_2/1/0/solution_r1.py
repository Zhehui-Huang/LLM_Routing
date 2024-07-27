import math
import networkx as nx

# Define the coordinates for each city
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=calculate_distance(i, j))

# Step 1: Construct a Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Detect odd degree vertices in MST
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 == 1]

# Step 3: Create the subgraph of odd degree vertices and find Minimum Weight Perfect Matching
odd_graph = G.subgraph(odd_degree_nodes)
min_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Add the minimum matching edges to the MST to make it Eulerian
mst.add_edges_from(min_matching)

# Step 4: Create Eulerian Circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 5: Convert the Eulerian Circuit into Hamiltonian Circuit
hamiltonian_circuit = []
visited = set()
total_cost = 0
last_visited = 0

for edge in eulerian_circuit:
    if edge[1] not in visited:
        visited.add(edge[1])
        hamiltonian_circuit.append(edge[1])
        total_cost += calculate_distance(last_visited, edge[1])
        last_visited = edge[1]

# Close the tour by returning to the starting point (depot city 0)
hamiltonian_circuit.append(0)
total_cost += calculate_distance(last_visited, 0)

# Output the tour and its total cost
print("Tour:", [0] + hamiltonian_circuit)
print("Total travel cost:", round(total_cost, 2))