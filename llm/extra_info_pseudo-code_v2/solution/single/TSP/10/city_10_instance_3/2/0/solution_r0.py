import math
import numpy as np
from itertools import permutations

# --- Distance calculation function ---
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

# --- Cities coordinates ---
coordinates = [
    (84, 67),  # Depot City 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  end City 8
    (6, 76)    # City 9
]

# --- Initial tour ---
# A very naive initial tour just picks cities in numerical order
initial_tour = list(range(len(coordinates))) + [0]

# --- Distance matrix ---
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# --- Initial Tour Cost Function ---
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# --- Heuristic: Simple implementation of Lin-Kernighan-inspired adjustments ---
# For simplicity, we'll just try pairwise swaps to find a better tour

def improve_tour(tour, distance_matrix):
    best_tour = tour[:]
    best_cost = calculate_tour_cost(tour, distance_matrix)
    improved = True

    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i + 2, len(tour) - 1):
                # Swap the sections of the tour
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_cost = calculate_tour_cost(new_tour, distance_matrix)
                if new_cost < best_cost:
                    best_tour = new_tour[:]
                    best_tour = best_tour[:j] + best_tour[j + 1:]  # Remove duplicate depot
                    best_cost = new_cost
                    improved = True
        tour = best_tour[:]
    return best_tour, best_cost

# --- Applying the heuristic ---
best_tour, best_cost = improve_tour(initial_tour, distance_converter)

# --- Outputting the result ---
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")