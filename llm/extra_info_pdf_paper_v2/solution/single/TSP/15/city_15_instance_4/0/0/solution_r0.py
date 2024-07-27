import numpy as np
import math
from itertools import permutations

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Matrix of distances
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(i, j)

# Initial naive solution (nearest neighbor algorithm starting from the depot city)
def initial_solution(depot):
    unvisited = set(cities.keys()) - {depot}
    tour = [depot]
    current = depot
    while unvisited:
        nearest = min(unvisited, key=lambda city: distance_matrix[current][city])
        tour.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    tour.append(depot)  # return to the depot
    return tour

# Calculate the cost of a tour
def calculate_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Implementing a simple 2-opt Algorithm for improvement
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # consecutive edges, no gain
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if calculate_cost(new_tour) < calculate_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Initialization and optimization
initial_tour = initial_solution(0)
optimized_tour = two_opt(initial_tour)
total_cost = calculate_cost(optimized_tour)

print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)