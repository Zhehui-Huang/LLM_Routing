import math
from itertools import permutations

# Cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Brute force search to find the tour with minimal maximum leg distance
def minimize_max_distance_tour():
    min_max_dist = float('inf')
    best_tour = None
    # Permutes through all city combinations
    for perm in permutations(range(1, 10)):
        tour = [0] + list(perm) + [0]
        max_dist = 0
        total_cost = 0
        # Calculate the maximum distance and total cost
        for i in range(len(tour) - 1):
            dist = euclidean_distance(tour[i], tour[i + 1])
            total_cost += dist
            if dist > max_dist:
                max_dist = dist
        # Swap to a better tour if a lower max distance is found
        if max_dist < min_max_dist:
            min_max_dist = max_dist
            best_tour = tour
            best_total_cost = total_cost
    return best_tour, best_total_cost, min_max_dist

# Find the optimal tour and print the results
optimal_tour, total_cost, max_distance = minimize_max_cmdistance_tour()
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")