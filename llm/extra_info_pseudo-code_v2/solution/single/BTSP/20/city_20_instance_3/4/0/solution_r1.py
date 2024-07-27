import math
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Compute the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Solver function for the Bottleneck Traveling Salesman Problem
def solve_btsp(cities):
    num_cities = len(cities)
    min_bottleneck = float('inf')
    best_tour = None

    # Iterating over all possible city permutations
    for perm in permutations(range(1, num_cities)):
        # Create the full tour starting and ending at the depot city
        tour = [0] + list(perm) + [0]
        # Calculate the distances for each edge in the tour
        current_tour_distances = [euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)]
        # Find the maximum distance in the current tour (the bottleneck)
        max_distance = max(current_tour_distances)
        # Sum of all distances (total travel cost)
        total_cost = sum(current_tour_distances)

        if max_distance < min_bottleneck:
            min_bottleneck = max_distance
            best_tour = tour
            best_total_cost = total_cost
            best_max_distance = max_distance

    return best_tour, best_total_cost, best_max_distance

# Find the optimal tour
tour, total_cost, max_distance = solve_btsp(cities)

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)