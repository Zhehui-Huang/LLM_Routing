import numpy as np
from itertools import combinations
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix

# City Coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
    (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21),
    (12, 39)
]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize the graph
n = len(coordinates)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Step 1.1: Algorithm BB
def bottleneck_biconnected_subgraph(dist_matrix):
    n = dist_matrix.shape[0]
    edges = [(i, j, dist_matrix[i][j]) for i in range(n) for j in range(i + 1, n)]
    edges.sort(key=lambda x: x[2])  # sort by weight
    
    G = csr_matrix((n, n), dtype=float)
    for i, j, weight in edges:
        G[i, j] = G[j, i] = weight
        # Check if the graph is biconnected (at least 2-connected)
        _, components = connected_components(csgraph=minimum_spanning_tree(G), return_labels=True)
        if len(set(components)) <= 1:  # every node reachable from any
            # Check biconnectivity more strictly
            for skip in range(n):
                subgraph = np.delete(np.delete(G.toarray(), skip, axis=0), skip, axis=1)
                _, sub_components = connected_components(csr_matrix(subgraph))
                if len(set(sub_components)) > 1:
                    continue
            # If always connected, found our bottleneck graph
            return G, weight

    return None, None

# Step 2: Identify tour in squaring graph
def find_tour_in_squared_graph(G, bottleneck_weight):
    n = G.shape[0]
    dists_squared = np.linalg.matrix_power(G.toarray(), 2)
    np.fill_diagonal(dists_squared, np.inf)  # no self-loops
    
    # Find approximate Hamiltonian cycle (trivial greedy approach for demonstration)
    tour = [0]  # start at depot
    visited = set(tour)
    while len(visited) < n:
        last = tour[-1]
        next_city = np.argmin([dists_squared[last, i] if i not in visited else np.inf for i in range(n)])
        tour.append(next_city)
        visited.add(next_funcity)
    
    tour.append(0)  # return to depot
    
    # Calculate metrics
    total_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    
    return tour, total_cost, max_distance

# Run algorithm
G_bb, bottleneck_weight = bottleneck_biconnected_subgraph(dist_matrix)
if G_bb is None:
    print("Could not find a bottleneck biconnected subgraph")
else:
    tour, total_cost, max_distance = find_tour_in_squared_graph(G_bb, bottleneck_weight)
    output = {
        'Tour': tour,
        'Total travel cost': total_cost,
        'Maximum distance between consecutive cities': max_distance
    }
    print(output)