from math import sqrt
from itertools import permutations
import random

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_total_distance(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

def initial_tour(dep_city_indices, cities):
    random.shuffle(dep_city_indices)
    return [0] + dep_city_indices + [0]

def local_search(tour, cities):
    # Improving the tour by trying different swaps within the tour cities
    best_tour = tour[:]
    best_distance = calculate_total_distance(tour, cities)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != j:
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_distance = calculate_total_distance(new_tour, cities)
                    if new_distance < best_distance:
                        best_tour, best_distance = new_tour[:], new_distance
                        improved = True
    return best_tour, best_distance

def solve_k_tsp(cities, k):
    city_indices = list(range(1, len(cities)))
    best_global_tour = None
    best_global_distance = float('inf')
    
    # Try various starting points for local searches
    for _ in range(10):  # Control this number as necessary based on performance needs
        random_subset = random.sample(city_indices, k-1)
        tour = initial_tour(random_subset, cities)
        tour, distance = local_search(tour, cities)
        if distance < best_global_distance:
            best_global_tour, best_global_distance = tour, distance
    
    return best_global_tour, best_global_travel_cost

# Define cities
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Solve the problem
best_tour, best_total_distance = solve_k_tsp(cities, 8)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_distance}")