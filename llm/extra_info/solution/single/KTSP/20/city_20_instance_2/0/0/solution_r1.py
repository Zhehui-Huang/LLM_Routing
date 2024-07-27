import itertools
import math
from sys import float_info

# Coordinates of the cities
cities = [
    (3, 26),  # Depot city 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14),
    (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible combinations of 9 different cities (excluding the depot city)
combinations = itertools.combinations(range(1, 20), 9)

# Variables to find the shortest tour
min_distance = float_info.max
best_tour = []

# Evaluate each combination of 9 cities
for combo in combinations:
    # Tour must include the depot city at start and end, check all permutations of the cities in the combination
    for perm in itertools.permutations(combo):
        # Include the depot city at the start and end
        tour = [0] + list(perm) + [0]
        # Calculate the total distance of this tour
        tour_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Update the best tour found so far
        if tour_distance < min_distance:
            min_distance = tour_distance
            best_tour = tour

# Print the best tour and its corresponding distance
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")