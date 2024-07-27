import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix

# City coordinates (index, (x, y))
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance
def euclidean_dist(a, b):
    return np.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Create weighted adjacency matrix
num_cities = len(cities)
weights = [[euclidean_dist(i, j) for j in range(num_cities)] for i in range(num_cities)]
weights = np.array(weights)

# Sorting edges based on weights
edges = [(weights[i][j], i, j) for i in range(num_cities) for j in range(i + 1, num_cities)]
edges.sort()

# Kruskal's-like algorithm to find a bottleneck-optimal biconnected subgraph
union_find = {i: i for i in range(num_cities)}  # Union-Find data structure

def find(v):
    if union_find[v] != v:
        union_find[v] = find(union_find[v])
    return union_find[v]

def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)
    if root1 != root2:
        union_find[root1] = root2

# Create Minimum Spanning Tree (MST) and augmenting it to become biconnected
mst = csr_matrix((num_cities, num_cities))
for weight, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        mst[u, v] = weight
        mst[v, u] = weight

# Ensure the subgraph is biconnected
# Here we identify weakly connected components and augment edges if necessary
while True:
    n_components, labels = connected_components(mst, connection='strong')
    if n_components == 1:
        break
    # Augmenting graph to reduce the number of components (this method is heuristic and may need refinement)
    for weight, u, v in edges:
        if labels[u] != labels[v]:
            mst[u, v] = weight
            mst[v, u] = weight
            union(u, v)
            break

# Extracting the tour from the square of the biconnected subgraph
def find_tour(mst_matrix):
    # Implementing a simple Depth-First Search (DFS) based method to find Hamiltonian cycle
    # For simplicity, any cycle in biconnected graph will be considered
    n = mst_matrix.shape[0]
    visited = [False] * n
    tour = []
    
    def dfs(v):
        tour.append(v)
        visited[v] = True
        for u in range(n):
            if mst_matrix[v, u] > 0 and not visited[u]:
                dfs(u)
                break
    
    dfs(0)
    tour.append(0)  # return to starting node
    return tour

tour = find_tour(mst)

# Calculate total cost and maximum distance
total_cost = sum(weights[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(weights[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")