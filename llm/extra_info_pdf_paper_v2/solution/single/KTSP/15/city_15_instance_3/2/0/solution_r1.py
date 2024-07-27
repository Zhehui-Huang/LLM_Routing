import numpy as np
import random

# Coordinates of the cities
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Generate distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Calculate total tour cost
def tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance_matrix[tour[i-1]][tour[i]]
    return cost

# Generate a random initial tour that includes exactly 10 cities and starts/ends at the depot city
def generate_initial_tour():
    tour = random.sample(range(1, n), 9)  # pick 9 cities randomly, excluding the depot city
    tour = [0] + tour + [0]
    return tour

# Local search optimization: swapping two cities in the tour
def optimize_tour(initial_tour):
    best_tour = initial_tour[:]
    best_cost = tour_cost(best_tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_tour) - 1):
            for j in range(i + 1, len(best_tour) - 1):
                if i != j:
                    new_tour = best_tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_cost = tour_cost(new_tour)
                    if new_cost < best_cost:
                        best_tour, best_cost = new_tour, new_cost
                        improved = True
    return best_tour, best_cost

# Perform multiple runs to find a good solution
best_global_tour, best_global_cost = None, float('inf')
num_attempts = 100

for _ in range(num_attempts):
    initial_tour = generate_initial_tour()
    optimized_tour, optimized_cost = optimize_tour(initial_tour)
    if optimized_cost < best_global_cost:
        best_global_tour, best_global_cost = optimized_tour, optimized_cost

print("Tour:", best_global_tour)
print("Total travel cost:", best_global_cost)