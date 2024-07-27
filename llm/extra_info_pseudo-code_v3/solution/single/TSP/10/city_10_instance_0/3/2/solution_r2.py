import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix

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

n = len(cities_coordinates)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i][j] = euclidean(cities_coordinates[i], cities_coordinates[j])

mst = minimum_spanning_tree(dist_matrix).toarray()
mst = mst + mst.T  # Making symmetric

# Get vertices with odd degree
odd_degree_vertices = [i for i in range(n) if np.sum(mst[i] > 0) % 2 == 1]

# Perfect Matching
odd_matrix = dist_matrix[np.ix_(odd_degree_vertices, odd_degree_vertices)]
max_weight = np.max(odd_matrix) * 100
odd_matrix[odd_matrix == 0] = max_weight
row_ind, col_ind = linear_sum_assignment(odd_matrix)
match_matrix = np.zeros((len(odd_degree_vertices), len(odd_degree_vertices)))
for row, col in zip(row_ind, col_ind):
    match_matrix[row, col] = odd_matrix[row, col]

# Add matching to MST
for i in range(len(odd_degree_vertices)):
    for j in range(len(odd_degree_vertices)):
        if match_matrix[i][j] != 0:
            u, v = odd_degree_vertices[i], odd_degree_vertices[j]
            mst[u][v] += match_matrix[i][j]
            mst[v][u] += match_matrix[i][j]  # Keep symmetric

# Find Eulerian circuit
def find_eulerian_circuit(graph, n):
    stack = [0]
    path = []
    while stack:
        u = stack[-1]
        next_city = [i for i in range(n) if graph[u][i] > 0]
        if next_city:
            v = next_city[0]
            graph[u][v] -= 1
            graph[v][u] -= 1
            stack.append(v)
        else:
            path.append(stack.pop())
    return path

eulerian_circuit = find_eulerian_circuit(mst, n)

# Convert Eulerian to Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for node in eulerian_circuit:
    if node not in visited:
        visited.add(node)
        hamiltonian_circuit.append(node)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # Complete the tour back to the start

# Calculate cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

# Output
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")