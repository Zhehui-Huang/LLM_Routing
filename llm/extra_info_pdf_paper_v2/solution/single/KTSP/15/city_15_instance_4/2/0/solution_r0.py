import numpy as np
from itertools import combinations, permutations
from sys import float_info

# City coordinates
cities = {0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 5: (54, 46), 
          6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74), 
          12: (53, 80), 13: (21, 21), 14: (12, 39)}

# Function to calculate Euclidean distance
def calc_dist(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize variables
total_cities = 15
tour_length = 12
best_tour = []
best_cost = float_info.max

# Generate combinations of 11 cities to visit (excluding the depot which must be visited)
combs = combinations([i for i in range(1, total_cities)], tour_length - 1)

# Explore each combination
for comb in combs:
    current_comb = [0] + list(comb) + [0]  # Include the depot city as start and end

    # Generate permutations of the inner cities
    perms = permutations(current_comb[1:-1])
    
    for perm in perms:
        tour = [0] + list(perm) + [0]
        current_cost = 0
        
        # Calculate total cost for this permutation
        for i in range(len(tour)-1):
            current_cost += calc_dist(cities[tour[i]], cities[tour[i+1]])
        
        # Check if this is the best tour so far
        if current_cost < best_cost:
            best_tour = tour
            best_cost = current_cost

# Output the best tour found and its cost
print("Tour:", best_tour)
print("Total travel cost:", best_cost)