import numpy as np
from scipy.spatial.distance import euclidean
from networkx import Graph, minimum_spanning_tree, eulerian_circuit
import networkx.algorithms.matching as max_weight_matching

# City coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), 
    (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Distance matrix
def create_distance_matrix(points):
    n = len(points)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i, j] = euclidean(points[i], points[j])
    return dist_matrix

distance_matrix = create_distance_matrix(cities)

# Create a complete graph
G = Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=distance_matrix[i][j])

# 1. Compute minimum spanning tree T
T = minimum_spanning_tree(G)

# 2. Find set O of vertices with odd degree in T
odd_degree_nodes = [v for v, degree in T.degree() if degree % 2 == 1]

# Create subgraph of G induced by odd-degree vertices
subgraph = G.subgraph(odd_degree_nodes)

# 3. Find minimum weight perfect matching M in the subgraph induced by O
matching = max_weight_matching.max_weight_matching(subgraph, maxcardinality=True, weight='weight')

# 4. Add edges from M to T to create multigraph H
H = T.copy()
for u, v in matching:
    H.add_edge(u, v, weight=distance_matrix[u][v])

# 5. Find Eulerian circuit in H
euler_circuit = list(eulerian_circuit(H))

# 6. Convert Eulerian circuit to Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in euler_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
# adding the last city to close the loop
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate total travel cost
total_cost = 0
for i in range(len(hamiltonian_circuit)-1):
    total_cost += distance_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]

# Output results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)