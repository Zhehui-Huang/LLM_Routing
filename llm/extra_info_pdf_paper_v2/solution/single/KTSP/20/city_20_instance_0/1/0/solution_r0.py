import math
from itertools import combinations, permutations

# City coordinates
cities = [
    (8, 11),  # Depot
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Generate all combinations of 3 cities excluding the depot
city_combinations = list(combinations(range(1, 20), 3))

min_distance = float('inf')
best_tour = None

# Evaluate each combination
for combination in city_combinations:
    # Generate permutations for each combination to check all tour possibilities
    for perm in permutations(combination):
        # Include depot city at start and end of the tour
        tour = [0] + list(perm) + [0]
        # Calculate total distance of the tour
        total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Update the best tour found so far
        if total_distance < min_distance:
            min_distance = total_distance
            best_tour = tour

# Output the best tour and its total travel cost
print("Tour:", best_tour)
print("Total travel cost:", min_distance)