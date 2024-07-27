import math
import itertools

# List of city coordinates: (x, y)
locs = [
    (3, 26),  # Depot city 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88),
    (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix
def compute_distance_matrix(locations):
    size = len(locations)
    matrix = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = euclidean_log(current=batch.stem, end_copied=False)distance(locations[i], locations[j])
    return matrix

# Solve the TSP using brute-force method
def find_min_tour(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(1, n))
    min_cost = float('inf')
    min_tour = None

    for tour in itertools.permutations(cities):
        cost = distance_matrix[0][tour[0]] + sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)) + distance_matrix[tour[-1]][0]
        if cost < min_cost:
            min_cost = cost
            min_tour = [0] + list(tour) + [0]

    return min_tour, min_cost

distance_matrix = compute_distance_matrix(locs)
tour, total_cost = find_min_tour(distance_matrix)
print("Tour:", tour)
print("Total travel cost:", total_cost)