import math
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

# Coordinates of cities including the depot
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Step 1: Compute the Euclidean distance matrix
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

n = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Step 1: Compute a minimum spanning tree T of G using Kruskal's algorithm
G = nx.complete_graph(n, nx.Graph())
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=distance_matrix[i][j])

T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set of vertices with odd degree in T
odd_degree_vertices = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
O = G.subgraph(odd_degree_vertices)
M = nx.algorithms.matching.min_weight_matching(O, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
cost = 0
prev_node = None

for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    if prev_node is not None:
        cost += distance_matrix[prev_node][u]
    prev_node = u

# Adding the return to the depot city
hamiltonian_circuit.append(0)
cost += distance_matrix[prev_node][0]

# Output the result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", cost)