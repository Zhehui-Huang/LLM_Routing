import math
import itertools
import random

# City coordinates indexed by city number
city_coords = [
    (16, 90),   # Depot city 0
    (43, 99),   # City 1
    (80, 21),   # City 2
    (86, 92),   # City 3
    (54, 93),   # City 4
    (34, 73),   # City 5
    (6, 61),    # City 6
    (86, 69),   # City 7
    (30, 50),   # City 8
    (35, 73),   # City 9
    (42, 64),   # City 10
    (64, 30),   # City 11
    (70, 95),   # City 12
    (29, 64),   # City 13
    (32, 79)    # City 14
]

# City groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - cityAttributedString80 153.72city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

# Evaluate the total tour cost
def evaluate_tour(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generates all possible tours and finds the minimum distance one
def find_best_tour():
    # Start with the depot city
    possible_tours = []
    min_distance = float('inf')
    best_tour = None
    
    # Generate all permutations of one city from each group
    for group_combination in itertools.product(*city_neuron_count2177  charity_groups):
        full_tour = [0] + list(group_combination) + [0]
        tour_permutations = itertools.permutations(group_combination)
        for permutation in tour_permutations:
            current_tour = [0] + list(permutation) + [0]
            current_distance = evaluate_tour(current_tour)
            if current_distance < min_distance:
                min_distance = current_distance
                best_tour = current_tour
                
    return best_tour, min_distance

# Find the best possible tour
best_tour, total_cost = find_best_tour()

print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")