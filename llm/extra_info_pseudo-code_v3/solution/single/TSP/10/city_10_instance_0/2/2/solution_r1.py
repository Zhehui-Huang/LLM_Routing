import math
import networkx as nx
from networkx.algorithms import approximation

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of each city
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

# Create a graph and add all vertices and edges with their respective weights
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 1: Compute a minimum spanning tree
mst = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

# Step 3: Minimum weight matching on the subgraph induced by odd-degree vertices
min_weight_matching = nx.algorithms.max_weight_matching(mst.subgraph(odd_degree_nodes), maxcardinality=True, weight='weight')

# Step 4: Add matching edges to MST
for edge in min_weight_matching:
    u, v = edge
    # Ensure the edge is added only once
    if mst.has_edge(u, v):
        continue
    else:
        mst.add_edge(u, v, weight=euclidean_distance(cities[u], cities[v]))

# Step 5: Find an Eulerian circuit in the updated MST
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit (shortcutting)
tour = [0]
visited = set([0])
for u, v in eulerian_circuit:
    if v not in visited:
        tour.append(v)
        visited.add(v)
tour.append(0)  # returning to the depot

# Calculate the travel cost
total_cost = 0
for i in range(1, len(tour)):
    total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))