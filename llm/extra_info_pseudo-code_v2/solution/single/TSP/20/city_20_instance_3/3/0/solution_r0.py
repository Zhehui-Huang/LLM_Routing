import math
import random
from itertools import permutations

# Coordinates of cities including the depot (index 0)
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
          (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
          (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create distance matrix
def create_distance_matrix(cities):
    num_cities = len(cities)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = distance(cities[i], cities[j])
    return distances

# Heuristic: Simplified implementation of Lin-Kernighan
def lin_kernighan(cities):
    n = len(cities)
    distance_matrix = create_distance_matrix(cities)
    best_tour = list(range(n)) + [0]  # Initial tour: simple circle route and back to the start
    best_cost = sum(distance_matrix[best_tour[i]][best_tour[i + 1]] for i in range(len(best_tour) - 1))
    
    improvement = True  # Flag to detect if improvement happened in inner loop
    while improvement:
        improvement = False
        for start in range(1, n):  # Start from 1 to skip the depot for starting point
            for i in range(1, n):
                for j in range(i + 2, n + 1):  # ensuring i and j do not overlap
                    new_tour = best_tour[:i] + best_tour[i:j][::-1] + best_tour[j:]
                    new_cost = sum(distance_matrix[new_tour[k]][new_tour[k + 1]] for k in range(len(new_tour) - 1))
                    if new_cost < best_cost:
                        best_tour = new_tour
                        best_cost = new_cost
                        improvement = True
                        break  # Break to restart checking after improvement
                if improvement:
                    break
            if improvement:
                break
    
    return best_turbough, bes_subcost

# Solve the problem using Lin-Kernighan
tour, cost = lin_kernighan(cities)

print("Tour:", tour)
print("Total travel cost:", cost)