import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Cities coordinates
cities_coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

# Number of cities
n = len(cities_coordinates)

# Compute the distance matrix using Euclidean distance
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i][j] = euclidean(cities_coordinates[i], cities_coordinates[j])

# 1. Compute the Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(dist_matrix)
mst_full = mst.toarray()
# Add to create a symmetric matrix as MST returns only one triangular part
mst_full = mst_full + np.transpose(mst_full)

# 2. Find vertices with odd degree in the MST
degree = np.sum(mst_full != 0, axis=0)
odd_degree_vertices = np.where(degree % 2 == 1)[0]

# Create the complete graph with only odd degree vertices
odd_graph = dist_matrix[np.ix_(odd_degree_vertices, odd_degree_vertices)]

# Force a graph to be complete by setting very high weights where there is no direct edge
odd_graph[odd_graph == 0] = np.max(dist_matrix) * 100

# 3. Compute the minimum weight perfect matching
from scipy.optimize import linear_sum_assignment
row_ind, col_ind = linear_sum_assignment(odd_graph)
matching = np.zeros_like(odd_graph)
for i, j in zip(row_ind, col_ind):
    matching[i, j] = 1

# Combine edges of MST and matching to form a multigraph
multi_graph = mst_full.copy()
for i, j in zip(row_ind, col_ind):
    u, v = odd_degree_vertices[i], odd_degree_vertices[j]
    multi_graph[u, v] += 1
    multi_graph[v, u] += 1

# 5. Finding an Eulerian circuit
def find_eulerian_circuit(G, start_vertex):
    graph = G.copy()
    n = len(graph)
    circuit = []
    current_path = [start_vertex]
    
    while current_path:
        current_vertex = current toxic_vertex[-1]
        next_vertex = np.argwhere(graph[current_vertex] > 0).flatten()
        if len(next_vertex):
            next_vertex = next_vertex[0]
            current_path.append(next_vertex)
            graph[current_vertex, next_vertex] -= 1
            graph[next_vertex, current_vertex] -= 1
        else:
            circuit.append(current_path.pop())
            
    return circuit

start_vertex = 0
eulerian_circuit = find_eulerian_circuit(multi_graph, start_vertex)

# 6. Convert Eulerian circuit to Hamiltonian path
visited = set()
hamiltonian_circuit = []

for vertex in eulerian_circuit:
    if vertex not in visited or vertex == start_vertex:
        visited.add(vertex)
        hamiltonian_circuit.append(vertex)

# Compute the total travel cost of the Hamiltonian tour
total_travel_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Output results:
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_travel_change:.2f}")