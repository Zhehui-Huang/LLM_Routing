import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_connected_and_has_no_cycle(graph):
    """ Simple check to assume fully connected graph if it has enough edges,
        assuming no cycles other than the Hamiltonian cycle itself. """
    V = len(graph)
    return all(any(graph[i][j] for j in range(V) if i != j) for i in range(V))

def find_tour_by_bottleneck(coordinates):
    V = len(coordinates)
    edges = []
    dist_matrix = [[0]*V for _ in range(V)]
    
    # Prepare data: distances and an upper triangular matrix of distances
    for i in range(V):
        for j in range(i + 1, V):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            edges.append((dist, i, j))
            dist_matrix[i][j] = dist
            dist_matrix[j][i] = dist
    
    # Sort edges by their distance
    edges.sort()

    # Incrementally increase the bottleneck limit and try to form a Hamiltonian cycle.
    for (c_i, u, v) in edges:
        # Create a threshold graph with edges not exceeding current edge weight
        threshold_graph = [[0 if dist_matrix[i][j] > c_i else 1 for j in range(V)] for i in range(V)]
        
        if is_connected_and_has_no_cycle(threshold_graph):
            # Try to form a Hamiltonian cycle starting and ending at node 0
            for perm in permutations(range(1, V)):
                path = [0] + list(perm) + [0]
                if all(dist_matrix[path[i]][path[i+1]] <= c_i for i in range(V)):
                    total_cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(V))
                    max_distance = max(dist_matrix[path[i-1]][path[i]] for i in range(1, len(path)))
                    return {
                        'Tour': path,
                        'Total travel cost': total_cost,
                        'Maximum distance between consecutive cities': maxs_distance
                    }

# Given city coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88),
    (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

result = find_tour_by_bottleneck(coordinates)
print("Tour:", result['Tour'])
print("Total travel cost:", result['Total travel cost'])
print("Maximum distance between consecutive cities:", result['Maximum distance between consecutive cities'])