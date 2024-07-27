import numpy as np
from itertools import permutations
from math import sqrt
from random import random, choice

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# City groups
groups = [
    [1, 4], [2, 6], [7], [5], [9], [8], [3]
]

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def all_possible_tours():
    for group_perm in permutations(groups):
        for cities in np.meshgrid(*group_perm):
            yield [0] + list(cities) + [0]

def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')
    for tour in all_possible_tours():
        cost = total_tour_cost(tour)
        if cost < best_cost:
            best_tour = tour
            best_cost = cost
    return best_tour, best_cost

# Find the shortest possible tour
best_tour, best_cost = find_shortest_tour()

print("Tour:", best_tour)
print("Total travel cost:", best_cost)