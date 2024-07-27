import numpy as np
import random
from itertools import permutations

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68), 
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54), 
    18: (64, 72), 19: (14, 89)
}

# Distance calculation using Euclidean formula
def euclidean_distance(city1, city2):
    c1 = cities[city1]
    c2 = cities[city2]
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generating all subsets of cities of size k including the depot city 0
def generate_subsets(k):
    city_indices = list(cities.keys())
    city_indices.remove(0)
    subsets = [subset for subset in permutations(city_indices, k-1)]
    return [tuple([0] + list(subset) + [0]) for subset in subsets]

# Cost calculation for a tour
def tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# General Variable Neighborhood Search (GVNS)
def general_vns(k, max_iter=1000):
    subsets = generate_subsets(k)
    best_tour = None
    best_cost = float('inf')
    
    for iteration in range(max_iter):
        # Random initial subset
        current_tour = random.choice(subsets)
        current_cost = tour_cost(current_tour)
        
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour
        
        # Apply local search in the neighborhood
        # Here, considers a simple next neighbor swap within the subset
        improved = True
        while improved:
            improved = False
            for i in range(1, len(current_tour) - 2):
                for j in range(i+1, len(current_tour) - 1):
                    new_tour = list(current_tour)
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_cost = tour_cost(new_tour)
                    if new_cost < current_cost:
                        current_tour = tuple(new_tour)
                        current_cost = new_cost
                        improved = True
        
        # Update the best found solution if improved
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour
    
    return best_tour, best_cost

# Set k as 16 and find the best tour
k_tsp_tour, k_tsp_cost = general_vns(16)
print("Tour:", k_tsp_tour)
print("Total travel cost:", k_tsp_cost)