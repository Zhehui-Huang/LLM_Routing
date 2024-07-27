import networkx as nx
from itertools import combinations
import math

# Coordinates of cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Function to calculate Euclidean distance between two points
def euc_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph with weights equal to Euclidean distances between nodes
G = nx.complete_graph(len(cities))
for i, j in G.edges():
    G.edges[i,j]['weight'] = euc_dist(cities[i], cities[j])

# 1. Compute a minimum spanning tree (MST) T of graph G
T = nx.minimum_spanning_tree(G, weight='weight')

# 2. Identify set O of vertices with odd degree in T
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# 3. Find a minimum weight perfect matching in the subgraph induced by O
subgraph = G.subgraph(O)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, True, weight='weight')

# 4. Add the edges of the perfect matching to T to create multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# 5. Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# 6. Convert the Eulerian circuit to a Hamiltonian circuit (TSP tour) by skipping repeated vertices
visited = set()
tour = []
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
tour.append(tour[0])  # Complete the tour by returning to the start

# Calculate the total distance of the tour
total_distance = 0
for i in range(len(tour) - 1):
    total_distance += euc_dist(cities[tour[i]], cities[tour[i + 1]])

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")