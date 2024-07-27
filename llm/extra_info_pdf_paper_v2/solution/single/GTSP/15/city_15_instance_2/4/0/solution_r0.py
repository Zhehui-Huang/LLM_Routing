import math
from itertools import permutations
import random
import sys

# Define the cities and coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Define city groups
city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Find the shortest tour visiting one city from each group
def find_shortest_tour():
    best_tour = None
    best_tour_cost = float('inf')

    # Evaluate all permutations of one choice per group
    group_permutations = list(permutations(range(len(city_groups))))
    
    for perm in group_permutations:
        for choices in itertools.product(*(city_groups[gp] for gp in perm)):
            tour = [0] + list(choices) + [0]  # Tour starting and ending at depot city 0
            tour_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            
            # Update the shortest tour found
            if tour_cost < best_tour_cost:
                best_tour = tour
                best_tour_cost = tour_cost

    return best_tour, best_tour_cost

# Get the shortest tour and its cost
shortest_tour, total_tour_cost = find_shortest_tour()

# Output the tour and the total travel cost
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_tour_cost:.2f}")