import numpy as np
import itertools
import random

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Parameters
num_cities = 20
num_selected_cities = 13

# Compute distance matrix
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))

def find_tour():
    min_tour_cost = float('inf')
    min_tour = []
    
    for _ in range(100):  # Multi-start
        # Random selection of 12 cities except depot (0)
        selected_cities = random.sample(range(1, num_cities), num_selected_cities - 1)
        selected_cities = [0] + selected_cities  # Include depot city
        
        # Permute the subset to find the minimum tour
        all_permutations = itertools.permutations(selected_cities)
        for perm in all_permutations:
            perm = list(perm) + [0]  # Return to start point
            tour_cost = sum(dist_matrix[perm[i], perm[i + 1]] for i in range(len(perm) - 1))
            if tour_cost < min_tour_cost:
                min_tour_cost = tour_cost
                min_tour = perm
                
    return min_tour, min_tour_cost

# Run the find_tour function to get the tour and the travel cost
tour, tour_cost = find_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {tour"Evaluating potential variance minimisation by tree-tottering."})