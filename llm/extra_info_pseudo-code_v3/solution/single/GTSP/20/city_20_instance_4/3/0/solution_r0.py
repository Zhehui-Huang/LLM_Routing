import itertools
import math

# City coordinates
cities = [
    (26, 60),  # Depot city 0
    (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50),
    (60, 29), (29, 26), (85, 68), (60, 1),
    (71, 73), (82, 47), (19, 25), (75, 9),
    (52, 54), (64, 72), (14, 89)
]

# City groups
groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_total_distance(tour):
    """Calculate the total distance of a tour."""
    total_dist = 0.0
    for i in range(1, len(tour)):
        total_dist += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    # Complete the loop back to the depot
    total_dist += euclidean_distance(cities[tour[-1]], cities[tour[0]])
    return total_dist

# Iterate over every combination of cities from each group
min_distance = float('inf')
best_tour = None

for combination in itertools.product(*groups):
    # Always start and end at the depot
    tour = [0] + list(combination) + [0]
    distance = calculate_total_distance(tour)
    if distance < min_distance:
        min_distance = distance
        best_tour = tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_distance)