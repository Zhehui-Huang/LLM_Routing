import math
from itertools import permutations

# Coordinates of cities including the depot
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Groups of cities
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a distance matrix for quick lookup
dist_matrix = {}
for i in cities:
    dist_matrix[i] = {}
    for j in cities:
        dist_matrix[i][j] = distance(cities[i], cities[j])

# Attempt all permutations of one city from each group
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = None

    for selection in permutations([min(group) for group in groups]):
        all_permutations = permutations(selection)
        for perm in all_permutations:
            current_tour = [0] + list(perm) + [0]
            current_cost = sum(dist_matrix[current_tour[i]][current_tour[i + 1]] for i in range(len(current_tour) - 1))

            if current_cost < min_cost:
                min_cost = current_cost
                best_tour = current_tour

    return best_tour, min_cost

# Find the optimal tour
tour, total_cost = find_shortest_tour()

# Printing the results
print("Tour:", tour)
print("Total travel cost:", total_cost)