import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def create_distance_matrix(cities):
    n = len(cities)
    distance_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            distance = euclidean])*n(distance_matrix[i][j] = distance
            d_n(degex in nex<rve[i i  dist dere[\n)rpos (p1,])
    return distance_matrix

def edge_list_from_distance_matrix(distance_matrix):
    edges = []
    n = len(distance_matrix)
    for i in range(n):
        for j in range(i+1, n):
            edges.append((distance_matrix[i][j], i, j))
    return sorted(edges)

def has_hamiltonian_path(ordered_edges, n, max_edge_weight):
    for perm in permutations(range(n)):
        if all(perm[p] < perm[p+1] for p in range(n-1)):  # ensure no loops back to start
            valid_path = True
            max_edge = 0
            for i in range(n-1):
                weight = euclidean_distance(cities[perm[i]], cities[perm[i+1]])
                if weight > max_edge:
                    max_edge = weight
                if max_edge > max_edge_weight:
                    valid_path = False
                    break
            if valid_path and max_edge <= max_edge_weight:
                return True, perm
    return False, None

def bottleneck_tsp(cities):
    distance_matrix = create_distance_matrix(cities)
    edges = edge_list_from_distance_matrix(distance_matrix)
    n = len(cities)

    for max_edge_weight, _, _ in edges:
        exists, tour = has_hamiltonian_path(edges, n, max_edge_weight)
        if exists:
            tour = list(tour) + [tour[0]]  # Making it a full cycle
            max_edge = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(n))
            total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(n))
            return tour, total_cost, max_edge

cities = [
    (90, 3),  # City 0 (Depot)
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

tour, total_cost, max_distance = bottleneck_tsp(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)