import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from itertools import combinations

# Coordinates of cities including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Step 1: Compute MST
mst = minimum_spanning_tree(dist_matrix)
mst = csr_matrix(mst)

# Function to find odd degree vertices in the MST
def find_odd_vertices(mst):
    degrees = np.sum(mst, axis=0) + np.sum(mst, axis=1) - np.diagonal(mst)
    odd_vertices = np.where(degrees % 2 == 1)[1]
    return odd_vertices

# Step 2: Identify odd degree vertices in MST
odd_vertices = find_odd_vertices(mst)

# Function to find the minimum weight perfect matching
def find_min_weight_matching(odd_vertices, dist_matrix):
    num_vertices = len(odd_vertices)
    edges = list(combinations(odd_vertices, 2))
    graph = csr_matrix((num_vertices, num_vertices))

    for u, v in edges:
        weight = dist_matrix[u, v]
        graph[u, v] = weight
    
    from networkx.algorithms.matching import max_weight_matching
    import networkx as nx
    G = nx.Graph()
    for u, v in edges:
        G.add_edge(u, v, weight=-dist_matrix[u, v])  # Minimize weight for maximum matching

    matching = max_weight_matching(G, maxcardinality=True, weight='weight')
    return matching

# Step 3: Find Minimum weight perfect matching in the subgraph induced by O
matching = find_min_weight_matching(odd_vertices, dist_matrix)

# Step 4: Combine MST and Matching to form multigraph
multi_graph = mst.copy()
for edge in matching:
    if multi_graph[edge[0], edge[1]] == 0:
        multi_graph[edge[0], edge[1]] = dist_matrix[edge[0], edge[1]]
        multi_graph[edge[1], edge[0]] = dist_matrix[edge[1], edge[0]]

# Step 5: Find Eulerian Circuit
from networkx import eulerian_circuit
G_multi = nx.from_scipy_sparse_matrix(multi_graph, create_using=nx.MultiGraph())
euler_tour = list(eulerian_circuit(G_multi))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit by skipping visited nodes
visited = set()
hamiltonian_circuit = [0]
total_cost = 0

for u, v in euler_tour:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)
        total_cost += dist_matrix[u, v]

# Append the return to the depot
hamiltonian_circuit.append(0)
total_cost += dist_matrix[hamiltonian_circuit[-2], 0]

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)