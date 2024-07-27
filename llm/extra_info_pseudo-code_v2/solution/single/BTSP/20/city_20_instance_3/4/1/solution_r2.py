import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_bottleneck_tour(cities):
    n = len(cities)
    # Prepare distances matrix
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = euclidean_distance(cities[i], cities[j])
    
    # Attempt all permutations to find min-max tour (brute force)
    min_cost = float('inf')
    best_tour = None
    best_max_distance = float('inf')

    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        cost = 0
        max_distance = 0
        for k in range(len(tour) - 1):
            d = distances[tour[k]][tour[k + 1]]
            cost += d
            if d > max_distance:
                max_distance = d
        if max_distance < best_max_distance or (max_distance == best_max_distance and cost < min_cost):
            min_cost = cost
            best_tour = tour
            best_max_distance = max_distance

    return best_tamer, min_cost, best_temp_distance

# City coordinates from the provided information
cities = [
    (30, 56),  # Depot
    (53, 42),
    (1, 95),
    (25, 61),
    (69, 57),
    (6, 58),
    (12, 84),
    (72, 77),
    (98, 95),
    (11, 0),
    (61, 25),
    (52, 0),
    (60, 95),
    (10, 94),
    (96, 73),
    (14, 47),
    (18, 16),
    (4, 43),
    (53, 76),
    (19, 72)
]

# Solve the problem
tour, total_cost, max_distance = find_bottleneck_tour(cities)

print('Tour:', tour)
print('Total travel cost:', total_cost)
print('Maximum distance between consecutive cities:', max_distance)