import numpy as np
import math
from itertools import permutations

# City Coordinates as provided
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40),
    (54, 42), (36, 30), (52, 82), (93, 44),
    (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Compute Euclidean distances between each pair of cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

num_cities = len(coordinates)
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# k-TSP
k = 8

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance_matrix[tour[i-1]][tour[i]]
    total_cost += distance_matrix[tour[-1]][tour[0]]  # returning to the depot
    return total_cost

# Find the best tour using permutations
def best_k_tsp_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Include the depot city and find permutations of k-1 other cities
    for subset in permutations(range(1, num_cities), k-1):
        current_subset = [0] + list(subset) + [0]  # Start and end at the depot
        current_cost = calculate_tour_cost(current_subset)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_subset
        
    return best_tour, best_cost

best_tour, best_cost = best_k_tsp_tour()

# Outputs the best tour starting and ending at the depot and the total travel cost of this tour
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")