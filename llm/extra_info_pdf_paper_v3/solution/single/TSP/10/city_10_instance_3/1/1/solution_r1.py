import math
from scipy.spatial import distance
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix
import networkx as nx

# Given city coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Helper function to calculate the Euclidean distance
def euclidean_dist(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Creating the distance matrix
num_cities = len(cities)
dist_matrix = [[euclidean_dist(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Create Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(csr_matrix(dist_matrix))
mst = mst.toarray()

# Construct graph from MST and find nodes with odd degree
G = nx.Graph()
for i in range(num_cities):
    for j in range(num_cities):
        if mst[i][j] > 0:
            G.add_edge(i, j, weight=dist_matrix[i][j])

# Find nodes with odd degree
odd_degree_nodes = [x for x in G.nodes() if G.degree(x) % 2 == 1]

# Create a subgraph from odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)

# Find the minimum weight perfect matching in the subgraph
matches = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add matching edges to the original graph (MST)
G.add_edges_from(matches)

# Find an Eulerian circuit in the updated graph where nodes with odd degree have been paired
euler_circuit = list(nx.eulerian_circuit(G, source=0))

# Make sure the Eulerian circuit is also a Hamiltonian cycle by skipping repeats
tour = []
visited = set()
for u, v in euler_circuit:
    if u not in visited:
        visited.add(u)
        tour.append(u)
    if v not in visited:
        visited.add(v)
        tour.append(v)

# Ensure the tour ends at the starting node, depot city 0
if tour[-1] != 0:
    tour.append(0)
    
# Calculate total cost of the tour
total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")