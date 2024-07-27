import numpy as np
from itertools import permutations

# City coordinates
cities = {0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 5: (54, 46), 
          6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74), 
          12: (53, 80), 13: (21, 21), 14: (12, 39)}

# Function to calculate Euclidean distance
def calc_dist(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to evaluate the total distance of a tour
def evaluate_tour(tour):
    return sum(calc_dist(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# Pick a subset of cites including the depot (0) and any other 11 cities
subset_cities = [0] + sorted(cities.keys())[1:12]
shortest_tour, min_cost = None, float('inf')

# Permutation of only the inner cities (not including the depot)
for perm in permutations(subset_cities[1:]):
    tour = [0] + list(perm) + [0]
    cost = evaluate_tour(tour)
    if cost < min_cost:
        min_cost = cost
        shortest_tour = tour

# Output the best tour and its cost
print("Tour:", shortest_tour)
print("Total travel cost:", min_cost)