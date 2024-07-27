import itertools
import math
import random

# Coordinates of cities indexed from 0 to 14, where index 0 is the depot
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Groups: List of cities grouped
groups = [
    [8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]
]

def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Generate all permutations of cities, one from each group
all_group_permutations = list(itertools.product(*groups))

def calculate_total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

def find_best_tour():
    minimal_cost = float('inf')
    best_tour = None
    
    # Include the depot in the tour
    for perm in all_group_permutations:
        # Try starting from the depot, going to one city from each group, and coming back to the depot
        candidate_tour = [0] + list(perm) + [0]
        cost = calculate_total_tour_cost(candidate_tour)
        
        if cost < minimal_cost:
            minimal_cost = cost
            best_tour = candidate_tour
            
    return best_tour, minimal_cost
  
best_tour, best_cost = find_best_tour()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)