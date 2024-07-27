import numpy as np
import random
from itertools import permutations

# Coordinates of cities, with city 0 as the depot
coords = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# City groups
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Calculate Euclidean distance
def euclidean_dist(city1, city2):
    return np.sqrt((coords[city1][0] - coords[city2][0]) ** 2 + (coords[city1][1] - coords[city2][1]) ** 2)

# Calculate the total tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_dist(tour[i], tour[i + 1])
    return total_cost

# Helper function to generate all permutations and select the best one
def find_best_route(group_permutations):
    best_cost = float('inf')
    best_tour = None
    for perm in group_permutations:
        full_tour = [0] + list(perm) + [0]
        cost = calculate_tour_cost(full_tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = full_tour
    return best_tour, best_cost

# Main function to calculate the shortest tour visiting one city from each group
def solve_gtsp(groups):
    # Generate all permutations (Cartesian product of all groups - exhaustive search over small dataset)
    all_possible_tours = list(permutations([g[0] for g in groups]))
    for i, grp in enumerate(groups[1:], start=1):
        new_list = []
        for perm in all_possible_tours:
            new_list.extend([perm[:i] + (city,) + perm[i:] for city in grp])
        all_possible_tours = new_list

    # Find the best route among all permutations
    best_tour, best_cost = find_best_route(all_possible_tours)
    return best_tour, best_cost

# Solve GTSP
tour, total_cost = solve_gtsp(groups)
print("Tour:", tour)
print("Total travel cost:", total_cost)