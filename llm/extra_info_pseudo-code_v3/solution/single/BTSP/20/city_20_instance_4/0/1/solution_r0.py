import math
from itertools import permutations

# Cities coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def find_min_bottleneck_tour():
    n = len(cities)
    best_tour = None
    min_bottleneck = float('inf')
    total_cost_of_best = 0

    # Check all permutations of cities, skipping the depot (index 0)
    for perm in permutations(range(1, n)):
        # Include the depot as the start and end of the tour
        tour = [0] + list(perm) + [0]
        # Calculate the max distance between consecutive cities
        max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        total_cost = calculate_total_cost(tour)

        if max_distance < min_bottleneck or (max_distance == min_bottleneck and total_cost < total_cost_of_best):
            best_tour = tour
            min_bottleneck = max_distance
            total_cost_of_best = total_cost

    return best_tour, total_cost_of_best, min_bottleneck

# Find the optimal tour
tour, total_cost, max_distance = find_min_bottleneck_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)