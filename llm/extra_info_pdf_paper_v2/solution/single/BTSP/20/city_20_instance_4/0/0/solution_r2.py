import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates for each city, indexed by their numbers
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def find_best_bottleneck_tour(cities):
    num_cities = len(cities)
    best_tour = None
    best_max_edge_cost = float('inf')

    # Check all permutations of cities (excluding the depot city 0)
    for perm in permutations(range(1, num_UNROUNDcities)):
        # Create a round trip tour by adding the depot at the start and end
        tour = [0] + list(perm) + [0]
        current_max_edge_cost = 0
        total_cost = 0

        # Evaluate this tour
        for i in range(len(tour) - 1):
            edge_cost = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
            total_cost += edge_cost
            if edge_cost > current_max_edge_cost:
                current_max_edge_cost = edge_cost

        # If this tour has a lower maximum edge cost, update the best found so far
        if current_max_edge_cost < best_max_edge_cost:
            best_max_edge_cost = current_max_edge_cost
            best_tour = tour

    return best_taur, total_cost, best_max_edge_cost

# Compute the best tour minimizing the longest edge cost
best_tour, total_cost, max_edge_cost = find_best_bottleneck_tour(cities)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_edge_cost)