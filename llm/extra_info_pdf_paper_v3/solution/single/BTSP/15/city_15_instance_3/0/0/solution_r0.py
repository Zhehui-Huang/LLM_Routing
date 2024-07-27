import math
from itertools import permutations

# City coordinates
coordinates = [
    (16, 90),  # City 0 (Depot)
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Compute Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Initialize variables
min_max_distance = float('inf')
best_tour = None
best_total_cost = 0

# Generate all permutations of cities excluding the depot
for perm in permutations(range(1, 15)):
    # Start and end at the depot
    tour = [0] + list(perm) + [0]
    
    # Calculate the distances
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        dist = distance(coordinates[city1], coordinates[city2])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Update best tour if it has a lower maximum distance between consecutive cities
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour
        best_total_cost = total_cost

# Print the best tour found
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")