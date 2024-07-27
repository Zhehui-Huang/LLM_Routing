import math
from itertools import permutations

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Evaluate the cost and max distance between consecutive cities in tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        d = distance(tour[i], tour[i + 1])
        total_cost += d
        if d > max_distance:
            max_distance = d
    return total_cost, max_distance

# Generate all possible tours and find the optimal one by comparing max distances
def find_optimal_tour():
    all_cities = list(cities.keys())[1:]  # Exclude the depot from permutations
    best_tour = None
    min_max_distance = float('inf')
    best_total_cost = 0

    # Generate permutations of all cities (excluding the depot)
    for permut in permutations(all_cities):
        tour = [0] + list(permut) + [0]  # Add depot to the beginning and end of the tour
        total_cost, max_dist = evaluate_tour(tour)
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_tour = tour
            best_total_cost = total_cost

    return best_tour, best_total_cost, min_max_distance

# Find the optimal tour, total cost and max distance
optimal_tour, total_travel_cost, max_consecutive_distance = find_optimal_tour()

# Print results
print("Tour:", optimal_tour)
print("Total travel cost:", total_travel_routes_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)