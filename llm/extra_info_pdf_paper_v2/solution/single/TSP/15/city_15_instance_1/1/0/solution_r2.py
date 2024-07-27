import numpy as np
from math import sqrt

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Distance matrix initialization
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

# Fill distance matrix
for i in range(num_cities):
    for j in range(num_cities):
        dist = sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)
        distance_matrix[i][j] = dist

# 2-opt Algorithm
def two_opt(route):
    best_route = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_route) - 1):
            for j in range(i+1, len(best_route)):
                new_route = best_route[:]
                new_route[i:j] = best_route[j-1:i-1:-1]
                if calculate_total_distance(new_route) < calculate_total_distance(best_route):
                    best_route = new_route
                    improved = True
    return best_route

def calculate_total_distance(route):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

# Create a list of city indices, starting and ending at the depot
initial_route = list(range(num_cities)) + [0]
optimized_route = two_opt(initial_route)
total_distance = calculate_total_distance(optimized_route)

# Output
print(f"Tour: {optimized_route}")
print(f"Total travel cost: {total_distance}")