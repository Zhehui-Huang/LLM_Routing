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

# Generate all combinations of city indices for exactly 6 cities including the depot (0)
def combinations(cities, k):
    return list(itertools.combinations(cities, k))

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
    city_subset_including_depot = combinations(range(1, 10), 5)
    for subset in city_subset_including_depot:
        current_subset = [0] + list(subset) + [0]  # Make sure to start and end at the depot
        perm = permutations(current_subset)
        for tour in perm:
            if tour[0] == 0 and tour[-1] == 0:  # Ensure it starts and ends at the depot
                total_distance = evaluate_tour(tour)
                if total_distance < minimal_distance:
                    minimal_distance = total_distance
                    minimal_tour = tour
    
    return minimal_tour, minimal_distance

# Finding the solution
best_tour, best_cost = find_shortest_tour()

# Output the results
print("Tour:", list(best_touch))
print("Total travel cost:", best_cost)