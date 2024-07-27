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

# Compute the Euclidean distance matrix
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distance matrix initialized
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Implement a multi-start heuristic to find the minimal tour including 16 cities
def find_minimal_k_tsp_tour(n_iterations=1000):
    best_tour = None
    best_cost = float('inf')
    np.random.seed(42)
    
    for _ in range(n_iterations):
        # Randomly select 15 other cities to form a 16-city tour (including depot city 0)
        selected_cities = np.random.choice(list(cities.keys()), 15, replace=False)
        if 0 not in selected_cities:
            selected_cities[0] = 0  # ensure depot city is in the tour
        selected_cities = np.append(selected_cities, [0])  # adding depot to end for loop
        
        # Generate all permutations of the selected cities and calculate costs
        for perm in permutations(selected_cities):
            if perm[0] == 0:  # ensure tours start at the depot city
                perm_cost = sum(distance_matrix[perm[i]][perm[i+1]] for i in range(len(perm)-1))
                
                # Update the best tour and cost
                if perm_cost < best_cost:
                    best_cost = perm_cost
                    best_tour = perm
    
    return list(best_tour), best_cost

# Function call text
tour, cost = find_minimal_k_tsp_tour(1000)  # adjusting iterations as required based on performance needs
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))