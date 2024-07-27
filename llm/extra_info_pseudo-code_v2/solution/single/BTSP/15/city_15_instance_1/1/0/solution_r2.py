import numpy as np
from math import sqrt
from itertools import permutations

# Coordinates of the cities
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Function to calculate the Euclidean distance between two points
def distance(pt1, pt2):
    return sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

# Function to generate all tours starting and ending at the depot city (index 0)
def generate_tours():
    indices = range(1, len(cities))
    for perm in permutations(indices):
        yield [0] + list(perm) + [0]

# Function to calculate the total cost and maximum leg of a tour
def evaluate_tour(tour):
    total_cost = 0
    max_leg = 0
    for i in range(len(tour) - 1):
        leg_cost = distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += leg_cost
        if leg_cost > max_leg:
            max_leg = leg_cost
    return total_cost, max_leg

# Finding the optimum tour that minimizes the maximum leg distance
best_tour = None
best_max_leg = float('inf')
best_total_cost = None

for tour in generate_tours():
    total_cost, max_leg = evaluate_tour(tour)
    if max_leg < best_max_leg:
        best_max_leg = max_leg
        best_total_cost = total_cost
        best_tour = tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_leg:.2f}")