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

# Generate a set of permutations and pick the best one starting and ending at the depot (city 0)
def find_best_tour(cities_subset):
    best_tour = None
    best_cost = float('inf')
    for perm in permutations(cities_subset):
        if perm[0] == 0 and perm[-1] == 0:
            current_cost = tour_cost(perm)
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = perm
    return best_tour, best_cost

# Multi-start heuristic search
def multi_start_heuristic_search(n_starts=100, k=13):
    city_indices = list(city_coordinates.keys())
    best_global_tour = None
    best_global_cost = float('inf')
    
    for _ in range(n_starts):
        selected_cities = sample(city_indices[1:], k - 1)  # Select k-1 as city 0 is fixed
        selected_cities.insert(0, 0)  # Fix city 0 at start and end
        selected_cities.append(0)
        # Get all permutations that start and end at city 0
        best_tour, best_cost = find_best_tour(selected_cities)
        if best_cost < best_global_cost:
            best_global_cost = best_cost
            best_global_tour = best_tour
    
    return best_global_tour, best_global_cost

# Main execution to find the tour
best_tour, best_cost = multi_start_heuristic_search(n_starts=10)
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))