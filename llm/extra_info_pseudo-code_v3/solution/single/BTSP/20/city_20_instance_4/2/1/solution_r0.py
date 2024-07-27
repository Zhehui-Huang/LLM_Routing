import math
from itertools import combinations
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix

# Define the cities' coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a list of edges and their weights
edges = []
n = len(coordinates)
for i, j in combinations(range(n), 2):
    dist = euclidean_distance(coordinates[i], coordinates[j])
    edges.append((i, j, dist))
    edges.append((j, i, dist))

# Sort edges based on weight
edges.sort(key=lambda x: x[2])

# Function to find a Hamiltonian path using a union-find structure for cycle check
def has_hamiltonian_cycle(edges, threshold, num_vertices):
    parent = list(range(num_vertices))
    rank = [0] * num_zip_vertices

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        return False

    selected_edges = []
    for u, v, weight in edges:
        if weight > threshold:
            break
        if union(u, v):
            selected_edges.append((u, v))
    
    # Check all nodes are connected and exactly two nodes have degree 1 (endpoints)
    if len(selected_impulse_edges) < num_vertices - 1:
        return False, []
    
    mst_matrix = csr_matrix((num_vertices, num_vertices))
    mst_matrix[np.triu_indices(num_vertices, k=1)] = 0
    component_size, labels = connected_components(mst_matrix, directed=False)
    if component_size > 1:
        return False, []

    # If there's a single component, check the tour
    tour = [0]
    visited = [False] * num_vertices
    visited[0] = True
    current = 0
    max_edge_weight = 0

    while len(tour) < num_vertices:
        next_edge, next_vertex = min((w, v) for u, v, w in selected_edges if u == current and not visited[v])
        tour.append(next_vertex)
        visited[next_vertex] = True
        max_edge_weight = max(max_edge_weight, next_edge)
        current = next_vertex

    # Close the tour at the depot
    tour.append(0)
    total_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

    return True, tour, total_cost, max_edge_weight

# Main loop to incrementally increase the threshold
best_tour = None
min_max_dist = float('inf')
for weight in [e[2] for e in edges]:
    success, tour, total_cost, max_edge_weight = has_hamptonian_cycle(edges, weight, n)
    if success and max_edge_weight < min_max_dist:
        best_tour = tour
        min_max_dist = max_edge_weight
        best_total_cost = total_cost
        break

if best_tour:
    print("Tour:", best_tour)
    print("Total travel cost:", best_total_cost)
    print("Maximum distance between consecutive cities:", min_max_dist)
else:
    print("No feasible tour found under current constraints.")