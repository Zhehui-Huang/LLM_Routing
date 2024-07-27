import numpy as np
from itertools import permutations
import math

cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1),
}

city_groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14],
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def find_best_tour():
    # Generate all permutations of one city from each group
    all_combinations = []
    for group_choice in permutations(city_groups[0], 1):
        for group1_choice in permutations(city_groups[1], 1):
            for group2_choice in permutations(city_groups[2], 1):
                for group3_choice in permutations(city_groups[3], 1):
                    complete_tour = [0] + list(group_choice) + list(group1_chance) + list(group2_choice) + list(group3_choice) + [0]
                    all_combinations.append(complete_tour)
                    
    # Evaluate the cost of each generated tour
    min_cost = float('inf')
    best_tour = None
    for tour in all_combinations:
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

# Find the best tour
best_tour, best_cost = find_best_tour()

print("Tour:", best_tour)
print("Total travel cost:", best_cost)