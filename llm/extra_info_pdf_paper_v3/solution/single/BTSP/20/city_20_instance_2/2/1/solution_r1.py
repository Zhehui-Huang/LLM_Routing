import math

# Define the cities and their coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Define a helper function to calculate the Euclidean distance between cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Define a function that finds a feasible tour minimizing the maximum edge length
def minimize_max_distance_tour():
    from itertools import permutations

    min_max_distance = float('inf')
    best_tour = None

    # Generate all permutations of the cities except the depot to find a feasible minimum max-distance tour
    for perm in permutations(cities.keys() - {0}):
        tour = [0] + list(perm) + [0]  # create a tour that starts and ends at the depot
        max_edge_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if max_edge_distance < min_max_distance:
            min_max_distance = max_edge_distance
            best_tour = tour

    # Calculate the total travel cost of the found tour
    total_travel_cost = sum(distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))

    return best_tour, total_travel_cost, min_max_distance

# Compute the tour, total travel cost, and maximum distance between consecutive cities
tour, total_travel_cost, max_distance_between_cities = minimize_max_distance_tour()

# Print the outputs
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_between_cities)