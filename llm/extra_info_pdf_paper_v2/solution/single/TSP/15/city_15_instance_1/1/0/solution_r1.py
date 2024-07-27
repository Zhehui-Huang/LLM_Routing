import numpy as np
from math import sqrt

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Distance calculation
def euclidean_distance(c1, c2):
    return sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Calculate all distances
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(i, j)

# 2-opt Algorithm
def two_opt(route):
    best_route = route.copy()
    best_cost = calculate_total_distance(best_route)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_route) - 2):
            for j in range(i + 1, len(best_route) - 1):
                if j - i == 1:
                    continue
                new_route = best_route[:]
                new_route[i:j+1] = best_route[i:j+1][::-1]
                new_cost = calculate_total_distance(new_route)
                if new_cost < best_cost:
                    best_route = new_route
                    best_cost = new_cost
                    improved = True
    return best_route, best_cost

def calculate_total_distance(route):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

# Initial route
initial_route = list(range(1, num_cities)) + [0]  # Start from 1 to exclude the depot and end at the depot
optimized_route, total_travel_cost = two_opt(initial_route)

# Outputting results
optimized_route = [0] + optimized_btn.route[::-1]  # Add depot at the start and reverse back as it's appended in the end initially
print(f"Tour: {optimized_route}")
print(f"Total travel cost: {total_travel_cost}")