import math
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix
import networkx as nx

# Coordinates of the cities
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Number of vertices (cities)
n = len(cities)

# Calculate the Euclidean distance between cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distance matrix
dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Creating a graph of cities using distances
G = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Collect odd degree vertices from MST
odd_degree_nodes = [node for node, degree in dict(mst.degree()).items() if degree % 2 == 1]

# Minimum Weight Perfect Matching (MWPM) on odd degree vertices in the MST
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, True)

# Construct an Eulerian graph by combining MST and the minimum weight matching
for edge in min_weight_matching:
    mst.add_edge(edge[0], edge[1], weight=G[edge[0]][edge[1]]['weight'])

# Finding an Eulerian tour
eulerian_tour = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian tour to Hamiltonian path (shortcutting method)
visited = set()
hamiltonian_tour = []

for u, v in eulerian_tour:
    if u not in visited:
        hamiltonian_tour.append(u)
        visited.add(u)
hamiltonian_tour.append(0)  # to complete the tour back to the depot

# Calculate the tour's total travel cost
total_distance = sum(dist_matrix[hamiltonian_tour[i]][hamiltonian_tour[i+1]] for i in range(len(hamiltonian_tour) - 1))

# Output the tour and total travel cost
print("Tour:", hamiltonian_tour)
print("Total travel cost:", total_distance)