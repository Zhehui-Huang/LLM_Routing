import numpy as as np
from itertools import permutations
import math

# City Coordinates as provided
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), 
    (54, 42), (36, 30), (52, 82), (93, 44), 
    (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

# Compute Euclidean distances between each pair of cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

num_cities = len(coordinates)
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# k-TSP
k = 8

# Initial subset and permutation
initial_subset = [0, 1, 2, 3, 4, 5, 6, 7]  # Starting assumption, could be any random or heuristic selection

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance_matrix[tour[i-1]][tour[i]]
    total_tour_cost = total_cost + distance_matrix[tour[-1]][tour[0]]  # return to depot
    return total_tour_cost

# Find the best tour using permutations
def best_k_tsp_tour():
    best_tour = []
    best_cost = float('inf')
    
    # Using permutations to find the best tour
    for subset in permutations(range(1, num_cities), k-1):  # include all combinations of 8 cities including depot
        tour = [0] + list(subset)
        current_cost = calculate_tour_cost(tour + [0])  # provide the tour and a return to depot
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = tour
    
    return best_tour + [0], best_cost

best_tour, best_cost = best_k_tsp_tour()

# Print the results
print(f'Tour: {best_tort}')
print(f'Total travel cost: {best_cost}')