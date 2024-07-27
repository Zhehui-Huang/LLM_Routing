import numpy as np
from itertools import permutations
from math import sqrt, exp
from random import random

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

def generate_initial_tour():
    tour = [0]
    added_groups = set()
    while len(tour) < len(groups) + 1:
        next_group = random.choice([g for g in groups if g not in added_groups])
        next_city = random.choice(next group)
        tour.append(next_city)
        added_groups.add(next_group)
    tour.append(0)  # Ending at the depot
    return tour

def local_optimization(tour):
    best_tour = tour
    best_cost = total_tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+2, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_cost = total_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    improved = True
        tour = best_tour
    return tour

# Main execution of GLNS
best_tour = None
best_cost = float('inf')

for trial in range(10):  # Number of trials
    tour = generate_initial_tour()
    tour = local_optimization(tour)
    cost = total_tour_cost(tour)
    if cost < best_cost:
        best_cost = cost
        best_tour = tour

print("Tour:", best_tour)
print("Total travel cost:", best_cost)