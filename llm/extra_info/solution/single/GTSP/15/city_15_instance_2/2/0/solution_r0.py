import itertools
from math import sqrt

# City coordinates
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

# Group of cities
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to calculate total route distance
def calculate_total_distance(route):
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += distance(route[i], route[i + 1])
    return total_dist

# Generate all permutations of one city from each group
all_possible_tours = itertools.product(*groups)

# Evaluate the shortest possible route
shortest_tour = None
min_distance = float('inf')

for potential_tour in all_possible_tours:
    complete_tour = [0] + list(potential_tour) + [0]
    tour_distance = calculate_total_distance(complete_tour)
    if tour_distance < min_distance:
        min_distance = tour_distance
        shortest_tour = complete_tour

# Output the best tour and its distance
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {min_distance:.2f}")