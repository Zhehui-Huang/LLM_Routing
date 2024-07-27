import numpy as np
import math
from itertools import permutations

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76),
}

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Number of cities
num_cities = len(cities)

# Distance matrix
dist_matrix = [[calculate_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Generate initial feasible solution (simple heuristic e.g., nearest neighbor or random)
def initial_tour():
    # Start at the depot city 0
    start = 0
    unvisited = list(range(1, num_cities))
    tour = [start]
    while unvisited:
        current = tour[-1]
        # Find nearest unvisited city
        next_city = min(unvisited, key=lambda x: dist_matrix[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)  # Return to the start
    return tour

# Calculate total travel cost of the tour
def total_cost(tour):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Improving the tour by swapping two edges (2-opt)
def improve_tour(tour):
    improved = True
    while improved:
        improved = False
        best_cost = total_cost(tour)
        for i in range(1, len(tour) - 3):
            for j in range(i + 2, len(tour) - 1):
                if j - i == 1: continue
                new_tour = tour[:]
                new_tour[i:j] = tour[j-1:i-1:-1]
                new_cost = total_cost(new_tour)
                if new_cost < best_cost:
                    tour = new_tour
                    best_cost = new_cost
                    improved = True
        if improved:
            tour = new_tour
    return tour

# Get an initial solution
tour = initial_tour()

# Improve the tour using the 2-opt heuristic based on Lin-Kernighan idea
optimized_tour = improve_tour(tour)
optimized_cost = total_cost(optimized_tour)

print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {optimized_cost}")