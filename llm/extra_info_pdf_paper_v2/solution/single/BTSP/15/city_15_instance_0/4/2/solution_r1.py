import numpy as np
from scipy.spatial.distance import cdist

# Coordinates of cities
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50),
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23),
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_dist(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

# Create distance matrix
n = len(cities)
dist_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i, j] = euclidean_dist(cities[i], cities[j])
        else:
            dist_matrix[i, j] = float('inf')

# Find MST using Prim's Algorithm
import heapq

def prim_mst(dist_matrix):
    n = len(dist_matrix)
    in_tree = [False] * n
    min_edge = [(float('inf'), None) for _ in range(n)]  # (cost, node)
    mst_edges = []
    total_cost = 0
    min_edge[0] = (0, 0)  # Start from node 0
    edge_pq = [(0, 0)]

    while edge_pq:
        cur_cost, u = heapq.heappop(edge_pq)
        if in_tree[u]:
            continue
        in_tree[u] = True
        total_cost += cur_cost
        if min_edge[u][1] is not None:
            mst_edges.append((min_edge[u][1], u, cur_cost))

        for v in range(n):
            if not in_tree[v] and dist_matrix[u][v] < min_edge[v][0]:
                min_edge[v] = (dist_matrix[u][v], u)
                heapq.heappush(edge_pq, (dist_matrix[u][v], v))

    return mst_edges, total_cost

mst, total_mst_cost = prim_mst(dist_matrix)

# Convert MST to tour using Preorder traversal
def preorder_traversal(mst, n):
    adjacency_list = {i: [] for i in range(n)}
    for u, v, w in mst:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    tour = []
    visited = set()

    def visit(node):
        visited.add(node)
        tour.append(node)
        for neighbor in sorted(adjacency_list[node]):
            if neighbor not in visited:
                visit(neighbor)

    visit(0)  # start at the depot
    tour.append(0)  # end at the depot

    return tour

tour = preorder_traversal(mst, n)

# Calculate total travel cost and max distance between consecutive cities of the final tour
total_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")