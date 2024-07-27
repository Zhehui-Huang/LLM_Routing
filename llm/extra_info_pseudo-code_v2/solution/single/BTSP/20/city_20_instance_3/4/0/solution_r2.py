import math
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to solve the Bottleneck Travelling Salesman Problem (BTSP)
def solve_btsp(cities):
    num_cities = len(cities)
    best_tour = None
    best_total_cost = float('inf')
    best_max_distance = float('inf')

    # Iterate over all permutations of cities (excluding the depot)
    for perm in permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]  # Create tour starting and ending at the depot
        # Calculate distances for the tour
        distances = [euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)]
        max_distance = max(distances)
        total_cost = sum(distances)
        
        # Check if this tour has a better max distance
        if max_distance < best_max_distance:
            best_max_distance = max_distance
            best_tour = tour
            best_total_cost = total_cost

    return best_tour, best_total_cost, best_max_distance

# Invoke the BTSP solver function
tour, total_cost, max_distance = solve_btsp(cities)

# Print results correctly
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)