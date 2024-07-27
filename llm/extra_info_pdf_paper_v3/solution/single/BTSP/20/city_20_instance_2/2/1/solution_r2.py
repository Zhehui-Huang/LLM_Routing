import math
import itertools

# Coordinates of the cities in the form city_index: (x, y)
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Find a tour that minimizes the maximum distance between consecutive cities
def solve_tsp():
    # Start the tour at the depot city 0
    N = len(cities)
    tour = None
    min_max_dist = float('inf')
    total_distance_best = 0

    # Iterate over all permutations of city indices (excluding the depot city)
    for perm in itertools.permutations(range(1, N)):
        current_tour = [0] + list(perm) + [0]
        max_dist = 0
        total_distance = 0
        
        # Compute the distances for the current tour
        for i in range(1, len(current_tour)):
            dist = distance(current_tour[i-1], current_tour[i])
            max_dist = max(max_dist, dist)
            total_distance += dist

        # Compare against the best found so far
        if max_dist < min_max_dist:
            min_max_dist = max_dist
            tour = current_tour
            total_distance_best = total_distance

    return tour, total_distance_best, min_max_dist

# Calculate the tour that minimizes the maximum consecutive distance
tour, total_travel_cost, max_distance_between_cities = solve_tsp()

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_between_cities)