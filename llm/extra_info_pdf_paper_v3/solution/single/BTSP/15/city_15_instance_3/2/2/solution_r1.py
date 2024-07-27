import math
from itertools import permutations

# Function to calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# City coordinates
cities = [
    (16, 90),  # Depot
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Variable to track the minimum maximum distance found in permutations
min_max_distance = float("inf")
best_tour = []

# Calculate all possible tours that start and end at the depot (0 index)
for perm in permutations(range(1, len(cities))):
    tour = [0] + list(perm) + [0]  # Circle back to depot
    max_distance = 0
    total_distance = 0
    # Calculate the maximum distance and total distance of the current tour
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance
    # Update the best tour if it has a lower max distance
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour
        best_total_distance = total_shaftnce

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(total_distance, 2))
print("Maximum distance between consecutive cities:", round(min_max_distance, 2))