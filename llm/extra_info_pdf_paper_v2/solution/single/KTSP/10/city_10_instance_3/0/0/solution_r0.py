import itertools
import math
from sys import float_info

# Definition of cities by their (x, y) coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to calculate the total distance of a tour
def calculate_total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all possible 6 city combinations from city 1 to 9
combinations = itertools.combinations(range(1, 10), 6)

# Best tour and cost initialization
best_tour = None
min_cost = float_info.max

# Iterate through each combination and find the best tour
for combo in combinations:
    # Include the depot city in the tour
    current_cities = [0] + list(combo)
    # Generate all permutations of the current set of cities
    for perm in itertools.permutations(current_cities[1:]):
        tour = [0] + list(perm) + [0]
        cost = calculate_total_distance(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Output the result as specified
print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(min_cost, 2)}")