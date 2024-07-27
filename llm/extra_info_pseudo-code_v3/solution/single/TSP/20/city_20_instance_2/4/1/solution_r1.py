import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.optimize import linear_sum_assignment

# Coordinate data
coordinates = np.array([
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), 
    (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
    (51, 58), (30, 48)
])

# Calculate distance matrix
dist_matrix = squareform(pdist(coordinates))

# Step 1: Compute MST
mst_csr = minimum_spanning_tree(dist_matrix)
mst = mst_csr.toarray()

# Helper to find odd degree vertices
def get_odd_vertices(mst):
    degrees = np.sum(mst > 0, axis=1)
    odd_vertices = np.where(degrees % 2 == 1)[0]
    return odd_vertices

# Step 2: Find vertices with odd degree in MST
odd_vertices = get_odd_vertices(mst)

# Step 3: Find minimum weight perfect matching among odd degree vertices
subgraph = dist_matrix[np.ix_(odd_vertices, odd_vertices)]
row_ind, col_ind = linear_sum_assignment(subgraph)

# Add this matching to the MST graph to form the multigraph
multi_mst = mst.copy()
for i, j in zip(row_ind, col_ind):
    v1, v2 = odd_vertices[i], odd_vertices[j]
    multi_mst[v1, v2] = dist_matrix[v1, v2]
    multi_mst[v2, v1] = dist_matrix[v1, v2]

# Step 5: Eulerian circuit construction
# Path to follow the vertices
def find_eulerian_tour(filtered_matrix, start=0):
    n = len(filtered_matrix)
    path = []
    stack = [start]
    while stack:
        vertex = stack[-1]
        check = np.where(filtered_matrix[vertex,:] > 0)[0]
        if len(check) == 0:
            path.append(stack.pop())
        else:
            next_vertex = check[0]
            filtered_matrix[vertex, next_vertex] -= 1
            filtered_matrix[next_vertex, vertex] -= 1
            stack.append(next_vertex)
    return path[::-1]

eulerian_tour = find_eulerian_tour(multi_mst)

# Step 6: Convert Eulerian to Hamiltonian
def eulerian_to_hamiltonian(tour):
    visited = set()
    ham_path = []
    for node in tour:
        if node not in visited:
            visited.add(node)
            ham_path.append(node)
    ham_path.append(ham_path[0])  # Complete the tour
    return ham_path

hamiltonian_path = eulerian_to_hamiltonian(eulerian_tour)

# Calculate total cost
total_cost = sum(dist_matrix[hamiltonian_path[i], hamiltonian_path[i + 1]]
                 for i in range(len(hamiltonian_path) - 1))

print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {total_cost:.2f}")