import math
import random
from itertools import permutations

# Coordinates dictionary
cities = {
    0: (90, 3), 
    1: (11, 17), 
    2: (7, 27), 
    3: (95, 81), 
    4: (41, 54), 
    5: (31, 35), 
    6: (23, 95), 
    7: (20, 56),
    8: (49, 29), 
    9: (13, 17)
}

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities given their indices """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_cost(tour):
    """ Calculate the total travel cost of the given tour """
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def refine_tour(best_tour):
    """ Attempt to refine the tour by trying all permutations of nodes inside the tour """
    min_cost = total_tour_cost(best_tour)
    for perm in permutations(best_tour[1:-1]):
        new_tour = [best_tour[0]] + list(perm) + [best_tour[0]]
        new_cost = total_tour_cost(new_tour)
        if new_cost < min_cost:
            min_cost = new_cost
            best_tour = new_tour
    return best_tour, min_cost

# Given we need to visit 6 cities including the depot
k = 6
other_cities_indices = list(range(1, 10))
random.shuffle(other_cities_indices)
selected_cities = [0] + other_cities_indices[:k-2] + [0] # Select random k-1 cities plus the depot

min_cost = float('inf')
best_tour = None

# Try initial solutions and refine
for _ in range(1000):  # Number of iterations for pseudo-random restarts
    random.shuffle(other_cities_indices)
    selected_cities = [0] + other_cities_indices[:k-2] + [0]
    optimized_tour, optimized_cost = refine_tour(selected_cities)
    if optimized_cost < min_cost:
        min_cost = optimized_cost
        best_tour = optimized_tour

print("Tour:", best_tour)
print("Total travel cost:", min_cost)