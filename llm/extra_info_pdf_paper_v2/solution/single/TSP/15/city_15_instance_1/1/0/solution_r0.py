import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Calculate distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean(cities[i], cities[j])

# Heuristic TSP solver using 2-opt
def calculate_total_distance(route):
    total_dist = sum(distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))
    return total_dist

def two_opt(route):
    best_route = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue  # Skip consecutive nodes
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]
                if calculate_total_distance(new_route) < calculate_total_distance(best_route):
                    best_route = new_route
                    improved = True
        route = best_route
    return best_route

# Create an initial route
initial_route = list(range(num_cities)) + [0]  # Start and end at the depot city 0
optimized_route = two_opt(initial_route)
total_travel_cost = calculate_total_distance(optimized_route)

# Provide the output
print(f"Tour: {optimized_route}")
print(f"Total travel cost: {total_travel($("/{13345*--4)})