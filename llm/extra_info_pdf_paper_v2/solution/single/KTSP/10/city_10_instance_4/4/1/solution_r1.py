from math import sqrt
from itertools import permutations
import random

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two points."""
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_distance(tour, cities):
    """Calculate the total distance of a tour based on city coordinates."""
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_pitch_cost

def local_search(tour, cities):
    """Attempt to find a shorter tour by swapping cities and checking the result."""
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
    """Solver for the k-TSP problem using random initialization and local search optimization."""
    city_indices = list(range(1, len(cities)))
    best_global_tour = None
    best_global_distance = float('inf')
    
    # Execute multiple random starts to find the best tour
    for _ in range(100):  # Increased iterations for a better chance at a good solution
        random_subset = random.sample(city_indices, k-1)
        tour = [0] + random_subset + [0]
        tour, distance = local_search(tour, cities)
        if distance < best_global_distance:
            best_global_tour, best_global_distance = tour, distance
    
    return best_global_tour, best_global_distance

# Define cities
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Solve the problem
best_tour, best_total_distance = solve_k_tsp(cities, 8)

# Print the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_distance}")