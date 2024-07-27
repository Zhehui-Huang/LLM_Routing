import math
from itertools import permutations
from random import sample

# Define the cities coordinates
city_coordinates = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Compute the total cost of visiting cities in the given order
def tour_cost(city_tour):
    total_cost = 0
    for i in range(len(city_tour) - 1):
        total_cost += euclidean_distance(city_tour[i], city_tour[i + 1])
    return total_cost

# Execute the heuristic search
def heuristic_search(k=13):
    city_indices = list(city_coordinates.keys())
    all_city_indices = list(city_coordinates.keys())
    best_overall_cost = float('inf')
    best_overall_tour = None

    for _ in range(1000):  # Number of random starts
        # Select k-1 random cities excluding the depot, then add the depot at start and end
        cities_subset = sample([ci for ci in all_city_indices if ci != 0], k-1)
        cities_subset = [0] + cities_subset + [0]

        # Generate permutations, keeping the first and last elements fixed (depot city)
        best_tour = None
        best_cost = float('inf')
        for perm in permutations(cities_subset):
            if perm[0] == 0 and perm[-1] == 0:
                current_cost = tour_cost(list(perm))
                if current_cost < best_cost:
                    best_cost = current_cost
                    best_tour = list(perm)

        # Retain the best found tour across all iterations
        if best_cost < best_overall_cost:
            best_overall_cost = best_cost
            best_overall_tour = best_tour

    return best_overall_tour, best_overall_cost

# Find the optimal tour and its cost
optimal_tour, optimal_cost = heuristic_search()
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_cost, 2))