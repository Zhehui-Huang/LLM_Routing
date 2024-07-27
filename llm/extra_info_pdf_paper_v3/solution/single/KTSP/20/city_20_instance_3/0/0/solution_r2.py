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

# Calculate distance matrix
def calculate_distance(c1, c2):
    return np.hypot(c1[0] - c2[0], c1[1] - c2[1])

# Create distance matrix
dist_matrix = np.zeros((20, 20))
for i in range(20):
    for j in range(20):
        dist_matrix[i][j] = calculate_distance(cities[i], cities[j])

def find_minimum_tour():
    all_cities = list(range(20))
    best_tour = None
    best_cost = float('inf')
    
    for subset in itertools.combinations(all_cities[1:], 12):  # Choose 12 cities excluding the depot city
        current_cities = [0] + list(subset) + [0]   # Start and end at the depot
        
        # Try all permutations of the chosen cities
        for perm in itertools.permutations(current_cities[1:-1]):
            route = [0] + list(perm) + [0]
            cost = sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
            
            if cost < best_cost:
                best_cost = cost
                best_tour = route
                
    return best_tour, best_cost

# Calculate minimum tour and its cost
tour, cost = find_minimum_tour()

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")