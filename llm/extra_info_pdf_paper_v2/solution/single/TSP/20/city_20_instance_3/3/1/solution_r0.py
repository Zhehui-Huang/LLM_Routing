import numpy as np
import math

# Ddefine the cities and their coordinates
cities = {
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

# Compute Euclidean distance
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Build cost matrix
def build_cost_matrix(cities):
    n = len(cities)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            cost_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return cost_matrix

# The Lin-Kernighan heuristic (Simplified simulation)
def lin_kernighan_tsp(cities):
    n = len(cities)
    current_tour = list(range(n))
    current_tour.append(0)  # complete the tour by returning to the starting city
    best_tour = current_tour
    best_cost = compute_tour_cost(best_tour, cost_matrix)
    
    improved = True
    while improved:
        improved = False
        for i in range(1, n - 2):
            for j in range(i + 2, n):
                if j - i == 1: continue  # skipping consecutive cities
                new_tour = current_tour[:i + 1] + current_tour[i + 1:j + 1][::-1] + current_tour[j + 1:]
                new_cost = compute_tour_cost(new_tour, cost_matrix)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour, new_cost
                    improved = True
        current_tour = best_tour
    return best_tour, best_cost

# Utility function to calculate tour cost
def compute_tour_cost(tour, matrix):
    return sum(matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

cost_matrix = build_cost_matrix(cities)
tour, total_cost = lin_kernighan_tsp(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)