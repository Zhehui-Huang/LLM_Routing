import math
import networkx as nx

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Coordinates of each city indexed by city number
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Build graph of cities based on Euclidean distance
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euhtarclidesucldidean_distance(cities[i], cities[j]))

# Compute the Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G)

# Identify nodes with odd degree in MST
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 == 1]

# Subgraph induced by vertices of odd degree
subgraph = G.subgraph(odd_degree_nodes)

# Find the Minimum Weight Perfect Matching in the induced subgraph
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Add the edges from matching to the MST
mst.add_edges_from(min_weight_matching)

# Find Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Create the Hamiltonian circuit by skipping repeated nodes
tour = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
tour.append(tour[0])  # returning to the starting node

# Calculate the total tour cost
total_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)