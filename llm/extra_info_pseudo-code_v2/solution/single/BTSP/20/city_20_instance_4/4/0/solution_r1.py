import math
from itertools import permutations

# Define the cities' coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9),
    17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Brute-force algorithm to find the approximate BTSP tour minimizing the maximum inter-city distance
def find_bottleneck_tsp_tour(cities):
    num_cities = len(cities)
    all_permutations = permutations(range(1, num_cities))  # Generate permutations for cities 1 to 19
    min_bottleneck_value = float('inf')
    best_tour = None

    # Evaluate each permutation of cities
    for perm in all_permutations:
        current_route = [0] + list(perm) + [0]
        max_dist = max(distance(current_route[i], current_route[i+1]) for i in range(len(current_route) - 1))
        
        if max_dist < min_bottleneck_value:
            min_bottleneck_value = max_dist
            best_tour = current_route

    return best_tour, min_bottleneck_value

# Running the BTSP solver to find the best tour and its bottleneck
tour, bottleneck_value = find_bottleneck_tsp_tour(cities)

# Calculate the total travel cost of the tour
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output the tour, total travel cost and the maximum distance
print("Tour:", tour)
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {bottleneck_value:.2f}")