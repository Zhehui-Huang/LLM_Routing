import math
from itertools import product

# Define the cities based on the given coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
    8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Group of cities
groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

# Calculate Euclidean distances between all pairs of cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a distance matrix
n = len(cities)
dist = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist[i][j] = euclidean_distance(cities[i], cities[j])

# Solve the GTSP
def calculate_total_distance(tour):
    total_dist = dist[0][tour[0]]  # Start from the depot
    for i in range(len(tour) - 1):
        total_dist += dist[tour[i]][tour[i + 1]]
    total_dist += dist[tour[-1]][0]  # Return to the depot
    return total_dist

# Explore all combinations of picking one city from each group
best_tour = None
min_distance = float('inf')

for combination in product(groups[0], groups[1], groups[2], groups[3]):
    tour = list(combination)
    total_distance = calculate_total_distance(tour)
    if total_distance < min_distance:
        min_distance = total_distance
        best_tour = tour

# Output the results
final_tour = [0] + best_tour + [0]
print("Tour:", final_tour)
print("Total travel cost:", min_distance)