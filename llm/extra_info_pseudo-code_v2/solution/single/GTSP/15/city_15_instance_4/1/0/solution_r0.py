import random
import math
from itertools import permutations

# City coordinates indexed by their IDs
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Groups of cities
groups = {
    0: [3, 8], 1: [4, 13], 2: [1, 2], 3: [6, 14], 4: [5, 9], 5: [7, 12], 6: [10, 11]
}

def calculate_distance(c1, c2):
    "Calculate Euclidean distance between two cities given their IDs."
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def all_possible_tours(groups):
    "Generate all possible tours through one city from each group."
    for group_choice in permutations([min(group) for group in groups.values()]):
        yield [0] + list(group_choice) + [0]

def calculate_tour_cost(tour):
    "Calculate the total cost of a given tour."
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Brute-force the shortest tour by evaluating all possible tours
best_tour = None
min_cost = float('inf')

for tour in all_possible_tours(groups):
    cost = calculate_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best tour found and its total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")