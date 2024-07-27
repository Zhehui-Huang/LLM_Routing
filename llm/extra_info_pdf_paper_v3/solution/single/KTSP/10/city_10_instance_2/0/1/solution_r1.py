import itertools
import math
from sys import float_info

# Given cities and their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to compute the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all permutations of a list of cities
def permutations(cities):
    return itertools.permutations(cities)

# Evaluate the total distance of a tour
def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i + 1])
    return total_distance

# Find the shortest tour visiting exactly 6 cities including the depot
def find_shortest_tour():
    minimal_tour = None
    minimal_distance = float_info.max

    # Include the depot city, and choose 5 out of the remaining 9 cities
    for subset in itertools.combinations(range(1, 10), 5):
        current_subset = [0] + list(subset)  # Make sure to start at the depot
        # Generate all permutations of current subset and add the depot at the end
        for permuted_subset in permutations(current_subset):
            full_tour = list(permuted_subset) + [0]  # Ensure it ends at the depot
            total_distance = evaluate_tour(full_tour)
            if total_distance < minimal_distance:
                minimal_distance = total_distance
                minimal_tour = full_tour

    return minimal_tour, minimal_distance

# Finding the solution
best_tour, best_cost = find_shortest_tour()

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)