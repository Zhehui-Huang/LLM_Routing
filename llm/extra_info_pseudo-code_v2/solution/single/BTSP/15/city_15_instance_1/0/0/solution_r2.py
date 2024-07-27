import numpy as np
import networkx as nx
from itertools import permutations

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all permutations of cities to visit
def find_best_tour():
    city_indices = list(cities.keys())
    start_city = city_indices.pop(0)  # Start at the depot city 0
    min_max_distance = float('inf')
    best_tour = None
    for permutation in permutations(city_indices):
        tour = [start_city] + list(permutation) + [start_city]
        max_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
    return best_tour, min_max_distance

# Evaluate the tour
def evaluate_tour(tour):
    total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    return total_distance

# Find the optimal tour
tour, max_distance = find_best_tour()
total_travel_cost = evaluate_tour(tour)

# Output
print("Tour:", tour)
print("Total travel cost:", total_travel_tablecost)
print("Maximum distance between consecutive cities:", max_distance)