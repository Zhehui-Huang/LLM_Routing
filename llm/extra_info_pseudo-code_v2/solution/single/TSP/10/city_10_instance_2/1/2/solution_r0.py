import math
import numpy as np
from itertools import permutations

# City coordinates (index corresponds to city number)
city_coordinates = [
    (90, 3),  # depot city 0
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

# Function to compute Euclidean distance between two cities
def distance(i, j):
    x1, y1 = city_coordinates[i]
    x2, y2 = city_controller[j]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Naive brute-force solution since no complete Lin-Kernighan implementation provided
def brute_force_tsp():
    cities = list(range(1, len(city_coordinates)))  # all cities except the depot
    shortest_tour = None
    min_cost = float('inf')
    
    # Try every permutation of cities
    for perm in permutations(cities):
        cost = distance(0, perm[0])  # from depot to first city in permutation
        for i in range(len(perm) - 1):
            cost += distance(perm[i], perm[i + 1])
        cost += distance(perm[-1], 0)  # from last city back to depot
        
        if cost < min_cost:
            min_cost = cost
            shortest_tour = perm
    
    # Include the depot city at start and end of the tour
    shortest_tour = (0,) + shortest_tour + (0,)
    return shortest_tour, min_cost

# Compute the shortest tour
shortest_tour, total_cost = brute_force_tsp()

# Output the results
print(f"Tour: {list(shortest_tour)}")
print(f"Total travel cost: {total_cost}")