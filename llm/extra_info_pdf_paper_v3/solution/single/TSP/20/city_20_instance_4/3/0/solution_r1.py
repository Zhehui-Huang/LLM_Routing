import math
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Distances matrix
dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Generate a sparse matrix for the distances
sparse_mat = csr_matrix(dist_matrix)

# Compute the minimum spanning tree
mst = minimum_spanning_tree(sparse_mat).toarray()

# Construct a graph from the MST
graph = nx.Graph()
for i in range(len(mst)):
    for j in range(len(mst[i])):
        if mst[i][j] > 0:
            graph.add_edge(i, j, weight=mst[i][j])

# Get the vertices with odd degree to match
odd_degree_vertices = [v for v in graph.nodes() if graph.degree(v) % 2 == 1]

# Create subgraph with the odd degree vertices
subgraph = graph.subgraph(odd_degree_vertices)

# Compute minimum weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
graph.add_edges_from(matching)

# Check if the graph now has an Euler circuit and create it
euler_circuit = list(nx.eulerian_circuit(graph, source=0))

# Convert Euler circuit to Hamiltonian path
visited = set()
hamiltonian_path = [0]
current_city = 0
total_distance = 0

for u, v in euler_circuit:
    if v not in visited:
        hamiltonian_path.append(v)
        total_distance += dist_matrix[current_city][v]
        current_city = v
        visited.add(v)

# Complete the cycle by returning to the start
if hamiltonian_path[-1] != 0:
    total_distance += dist_matrix[current_city][0]
    hamiltonian_path.append(0)

print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {total_distance:.2f}")