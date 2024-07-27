import math
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all edge weights
edges = {(i, j): distance(i, j) for i in cities for j in cities if i != j}

# Heuristic algorithm to find the solution
def solve_btsp(cities, edges):
    # Find a permutation of city indices
    num_cities = len(cities)
    min_bottleneck = float('inf')
    best_tour = None

    # Check all permutations of cities (excluding the depot city to reduce the search space)
    for perm in permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]  # Start and end at the depot city
        max_distance = max(edges[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
        total_cost = sum(edges[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
        
        if max_distance < min_bottleneck:
            min_bottleneck = max_distance
            best_tour = tour
            best_total_cost = total_cost
            best_max_distance = max_distance

    return best_tour, best_total_cost, best_max_disconnect

# Run the BTSP solver
tour, total_cost, max_disconnect = solve_btsp(cities, edges)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_disconnect)