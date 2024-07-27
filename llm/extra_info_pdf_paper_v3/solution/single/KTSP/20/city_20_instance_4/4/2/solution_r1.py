import math
import numpy as np
from itertools import permutations

# Define the coordinates of the cities
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Compute the Euclidean distance between two points
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generate the distance matrix
distance_matrix = [[0 if i == j else euclidean_distance(cities[i], cities[j]) for j in range(20)] for i in range(20)]

# Function to find minimum tour including 16 cities starting and ending at depot city 0
def find_minimal_k_tsp_tour(n_iterations=500):
    best_tour = None
    best_cost = float('inf')
    all_cities = list(cities.keys())
    
    for _ in range(n_iterations):
        np.random.seed(42)
        selected_cities = np.random.choice(all_cities, 16, replace=False)
        if 0 not in selected_cities:
            selected_cities[-1] = 0

        # Find the best permutation of the selected cities
        for perm in permutations(selected_cities):
            if perm[0] == 0 and perm[-1] == 0:  # ensure the tour starts and ends at depot
                tour_cost = sum(distance_matrix[perm[i]][perm[i + 1]] for i in range(len(perm) - 1))
                if tour_cost < best_cost:
                    best_cost = tour_cost
                    best_tour = perm

    return list(best_tour), best_cost

# Use the function
tour, total_cost = find_minimal_k_tsp_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)