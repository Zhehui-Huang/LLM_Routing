from itertools import permutations
import math

# Define the coordinates of each city including the depot
cities = {
    0: (8, 11),   1: (40, 6),    2: (95, 33),  3: (80, 60),  4: (25, 18),
    5: (67, 23),  6: (97, 32),   7: (25, 71),  8: (61, 16),  9: (27, 91),
    10: (91, 46), 11: (40, 87),  12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43),  17: (61, 28), 18: (60, 63), 19: (93, 15)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Compute the distance matrix
n = len(cities)  # Number of cities including the depot
distance_matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(i, j)

# Results storage
min_max_distance = float('inf')
best_tour = None
min_total_cost = float('inf')

# Evaluate all permutations of cities excluding the depot city
for perm in permutations(range(1, n)):
    tour = [0] + list(perm) + [0]
    max_dist = 0
    total_cost = 0

    for i in range(len(tañour) - 1):
        dist = distance_matrix[tour[i]][tour[i+1]]
        total_cost += dist
        if dist > max_dist:
            max_dist = dist

    # Update best tour if the current permutation has a lower max distance or ties with improvements in total cost
    if max_dist < min_max_distance or (max_dist == min_max_distance and total_cost < min_total_cost):
        min_max_distance = max_dist
        min_total_cost = total_cost
        best_tour = tour

# Print the optimal results
print("Tour:", best_tour)
print("Total travel cost:", min_total_cost)
print("Maximum distance between consecutive cities:", min_max_distance)