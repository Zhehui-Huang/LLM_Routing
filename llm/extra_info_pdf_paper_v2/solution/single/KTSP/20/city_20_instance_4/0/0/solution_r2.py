import numpy as np
import random
from itertools import permutations

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68), 
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54), 
    18: (64, 72), 19: (14, 89)
}

# Distance calculation using Euclidean formula
def euclidean_distance(city1, city2):
    c1 = cities[city1]
    c2 = cities[city2]
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculating total cost for a given tour
def tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Find the best route through a given subset of cities, starting and ending at the depot
def find_best_tour(subset):
    best_subtour = None
    best_cost = float('inf')
    for perm in permutations(subset):
        tour = (0,) + perm + (0,)
        cost = tour_cost(tour)
        if cost < best_cost:
            best_cost = cost
            best_subtour = tour
    return best_subtour, best_cost

# Main function to solve the problem
def solve_k_tsp():
    city_indices = list(cities.keys())
    city_indices.remove(0)  # remove the depot from the subset choices
    best_global_tour = None
    best_global_cost = float('inf')
    # Generate all subsets of 15 cities (1 is the depot)
    for subset in combinations(city_indices, 15):
        tour, cost = find_best_tour(subset)
        if cost < best_global_cost:
            best_global_cost = cost
            best_global_tour = tour
    return best_global_tour, best_global_cost

# Solve and output the solution
best_tour, best_cost = solve_k_tsp()
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))