import random
import numpy as np
from itertools import permutations

# Define city coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Helper function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Construct the distance matrix
n_cities = len(cities)
distance_matrix = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Hyper-heuristic approach
def find_best_tour(k=13):
    best_tour = []
    best_cost = float('inf')

    # Multi-start: Several iterations to find a good solution
    for _ in range(100):
        # Randomly select k cities including the depot
        selected_cities = [0] + random.sample(range(1, n_cities), k-1)
        # Find the best permutation of the selected subset
        for perm in permutations(selected_cities):
            if perm[0] == 0:  # Ensure tour starts and ends at depot city
                # Calculate the tour cost
                cost = sum(distance_matrix[perm[i]][perm[i+1]] for i in range(len(perm)-1)) + distance_matrix[perm[-1]][perm[0]]
                if cost < best_cost:
                    best_cost = cost
                    best_tour = list(perm) + [0]
    
    return best_tour, best_cost

# Run the solution and print results
best_tour, best_cost = find_best_tour()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)