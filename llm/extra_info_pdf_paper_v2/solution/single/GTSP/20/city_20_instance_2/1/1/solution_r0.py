import math
import random
from itertools import permutations

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_distance(tour, city_coords):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    return total_distance

# Coordinates of cities including the depot
city_coords = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Grouping of cities
groups = {
    0: [7, 10, 11, 12],
    1: [3, 8, 13, 16],
    2: [2, 4, 15, 18],
    3: [1, 9, 14, 19],
    4: [5, 6, 17]
}

# Implementation of a simple simulation to find a reasonable tour
def find_best_tour(groups, city_coords):
    best_tour = None
    best_cost = float('inf')
    
    # Generate permutations of picking one city from each group
    all_combinations = []
    for selection in permutations(groups):
        # Create all combinations for each permutation of group selections
        for choices in permutations([random.choice(groups[grp]) for grp in selection]):
            # Considering the depot at the start and end
            current_tour = [0, *choices, 0]  
            current_cost = total_tour_distance(current_tour, city_coords)
            if current_cost < best_cost:
                best_tour = current_tour
                best_cost = current_cost
    
    return best_tour, best_cost

# Running the simulation function to find the best tour
best_tour, best_cost = find_best_tour(groups, city_coords)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)