import random
import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Groups of cities
city_groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generate all possible tours
def generate_all_tours(depot, groups):
    for possible_combo in product(*groups):
        yield [depot] + list(possible_combo) + [depot]

# Find the shortest tour
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = None
    for tour in generate_all_tours(0, city_groups):
        # Calculate the cost of the current tour
        current_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = tour
            
    return best_tour, min_cost

# Finding the shortest tour
best_tour, total_cost = find_shortest_tour()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")