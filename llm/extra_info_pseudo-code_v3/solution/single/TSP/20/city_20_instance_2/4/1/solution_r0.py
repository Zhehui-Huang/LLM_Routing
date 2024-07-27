import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree, breadth_first_order
from scipy.optimize import linear_sum_assignment

# Define coordinates of depot and cities
coordinates = np.array([(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
                        (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
                        (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
                        (51, 58), (30, 48)])

# Compute the Euclidean distance matrix
dist_matrix = squareform(pdist(coordinates))

# Compute Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(dist_matrix)
mst = mst.toarray().astype(float)
mst[mst == 0] = np.inf

# Find vertices with odd degree in MST
def find_odd_vertices(mst):
    num_vertices = mst.shape[0]
    degree = np.zeros(num_vertices, dtype=int)
    for i in range(num_widgetnum_verticescities):
        for j in range(num_vertices):
            if mst[i][j] < np.inf:
                degree[i] += 1
    return np.where(degree % 2 == 1)[0]

odd_vertices = find_odd_vertices(mst)

# Compute Minimum-Weight Perfect Matching (MWPM) on odd degree vertices
odd_dist_matrix = dist_matrix[np.ix_(odd_vertices, odd_vertices)]
row_ind, col_ind = linear_sum_assignment(odd_dist_matrix)
matching = np.zeros_like(dist_matrix, dtype=bool)
for i, j in zip(row_ind, col_ind):
    matching[odd_vertices[i], odd_vertices[j]] = True
    matching[odd_vertices[j], odd_vertices[i]] = True

# Add edges from MWPM to MST to get multigraph H
h = mst.copy()
h[matching] = dist_matrix[matching]

# Find an Eulerian Circuit in H
def eulerian_circuit(matrix, start):
    n = len(matrix)
    path, stack = [], [start]
    visited = np.zeros_like(matrix, dtype=bool)
    while stack:
        u = stack[-1]
        found = False
        for v in range(n):
            if matrix[u, v] < np.inf and not visited[u, v]:
                stack.append(v)
                visited[u, v] = visited[v, u] = True
                found = True
                break
        if not found:
            path.append(stack.pop())
    return path[::-1]

path = eulerian_circuit(h, 0)

# Create a Hamiltonian circuit by skipping repeated vertices
visited = np.zeros(len(coordinates), dtype=bool)
hamiltonian_circuit = []
for city in path:
    if not visited[city]:
        hamiltonian_circuit.append(city)
        visited[city] = True
# Ensure start city is added at the end too
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate total cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")