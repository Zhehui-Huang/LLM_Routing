import math
import networkx as nx

# Coordinates of the cities
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Step 1: Create the complete graph with weights
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G[i][j]['weight'] = euclidean_distance(i, j)

# Step 2: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 3: Find vertices with odd degree
O = [v for v in T if T.degree[v] % 2 == 1]

# Step 4: Find minimum weight perfect matching on the induced subgraph
min_weight_matching = nx.algorithms.matching.min_weight_matching(G.subgraph(O), weight='weight')

# Step 5: Combine the edges of T and the matching to create a multigraph
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_switching)

# Step 6: Find an Eulerian circuit
euler_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 7: Make a Hamiltonian circuit by skipping visited nodes
visited = set()
tour = []
for u, v in euler_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
# Circuit back to the start for completion
tour.append(tour[0])

# Calculate total travel cost
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output the results
print("Tour:", tour)
print(f"Total travel cost: {total_cost:.2f}")