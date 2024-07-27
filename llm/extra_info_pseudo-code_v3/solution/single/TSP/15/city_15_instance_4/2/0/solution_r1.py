import networkx as nx
import numpy as np
from itertools import combinations

# Define the cities and their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 5: (54, 46),
    6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 10: (27, 47),
    11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Creating the graph with weighted edges between each pair of nodes
G = nx.Graph()
for u in cities:
    for v in cities:
        if u != v:
            G.add_edge(u, v, weight=distance(u, v))

# Step 1: Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in the MST
odd_degree_nodes = [node for node, degree in dict(T.degree()).items() if degree % 2 == 1]

# Step 3: Find a minimum weight matching for odd degree nodes
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(sub handle=sub graph, maxcardinality=True, weight="weight")

# Step 4: Add the edges from the minimum weight matching to the tree
T.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit
tour = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
tour.append(0)  # return to the depot

# Calculate the total distance of the tour
total_distance = sum(G[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_distance, 2))