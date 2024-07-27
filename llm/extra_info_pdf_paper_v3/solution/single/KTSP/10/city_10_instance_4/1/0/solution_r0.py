import numpy as np
from itertools import permutations
import random

# Define city locations
city_locations = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city_locations[city1]
    x2, y2 = city_locations[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible city subsets of size 7 (excluding depot city)
def generate_city_subsets():
    all_city_indices = list(city_locations.keys())[1:] # Exclude depot city index 0
    return [subset for subset in permutations(all_city_indices, 7) if 0 in subset]

# Evaluate the tour
def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i+1])
    return total_distance

# Generate initial subsets and find optimal route
def find_optimal_route():
    best_tour = None
    best_distance = float('inf')
    
    for _ in range(100):  # Multi-start aspect, can change based on computational budget
        subset = random.sample(range(1, 10), 7)  # Random subset of 7 cities, excluding the depot
        subset.insert(0, 0)  # Insert depot city at start
        subset.append(0)  # Append depot city at end
        
        subsets_permutations = list(permutations(subset))
        
        for perm in subsets_permutations:
            perm = list(perm)
            if perm[0] == 0 and perm[-1] == 0:
                tour_distance = evaluate_tour(perm)
                if tour_distance < best_distance:
                    best_distance = tour_distance
                    best_tour = perm
    
    return best_tour, best_distance

# Run the heuristic to find the best tour
best_tour, best_distance = find_optimal_route()

print("Tour:", best_tour)
print("Total travel cost:", round(best_distance, 2))