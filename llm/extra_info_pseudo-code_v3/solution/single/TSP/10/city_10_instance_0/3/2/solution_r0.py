import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import connected_components
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
        if i != j:
            dist_matrix[i][j] = euclidean(cities_coordinates[i], cities_coordinates[j])

# 1. Compute the Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(dist_matrix)
# Must work with the non-sparse format for further operations
mst = mst.toarray()

# 2. Find vertices with odd degree in the MST
degree = np.sum(mst != 0, axis=0) + np.sum(mst != 0, axis=1)
odd_degree_vertices = [i for i in range(n) if degree[i] % 2 == 1]

# 3. Find minimum weight perfect matching on the subgraph induced by odd degree vertices
odd_graph = dist_matrix[np.ix_(odd_degree_vertices, odd_degree_vertices)]
num_vertices = len(odd_degree_vertices)
if num_vertices % 2 == 1:
    odd_graph = np.pad(odd_graph, ((0, 1), (0, 1)), mode='constant', constant_values=0)
    odd_degree_vertices.append(-1)  # Dummy vertex
match_res = csr_matrix(odd_graph)
match_res = minimum_spanning_tree(match_res).toarray() * 2  # super simple approximation

# 4. Combine the edges of MST and matching to form multigraph H
multigraph = mst + match_res

# 5. Find an Eulerian circuit in H
def find_eulerian_circuit(graph, start=0):
    num_vertices = len(graph)
    visited = np.zeros_like(graph, dtype=bool)
    circuit = []
    stack = [start]
    
    while stack:
        v = stack[-1]
        w = np.where((graph[v]>0) & (~visited[v]))[0]
        if w.size > 0:
            w = w[0]
            stack.append(w)
            visited[v, w] = visited[w, v] = True
            graph[v, w] -= 1
            graph[w, v] -= 1
        else:
            circuit.append(stack.pop())
    return circuit[::-1]

eulerian_circuit = find_eulerian_circuit(multigraph)

# 6. Convert the Eulerian circuit into a Hamiltonian circuit (shortcutting)
visited = set()
hamiltonian_circuit = []
for city in eulerian_circuit:
    if city not in visited:
        hamiltonian_circuit.append(city)
        visited.add(city)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # complete the tour

# Compute the total travel cost of the Hamiltonian tour
total_travel_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Result
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_travel_cost:.2f}")