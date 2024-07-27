import math
from itertools import permutations

# Definitions of cities with (x, y) coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible tours that start and end at the depot city (city 0)
all_permutations = permutations(cities.keys() - {0})
tours = [[0] + list(p) + [0] for p in all_permutations]

# Function to evaluate a tour: total distance and max distance between consecutive cities
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        d = distance(tour[i], tour[i + 1])
        total_cost += d
        if d > max_distance:
            max_distance = d
    return total_cost, max_distance

# Search for the best tour that minimizes the maximum distance between any two consecutive cities
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

for tour in tours:
    total_cost, max_distance = evaluate_tour(tour)
    if max_distance < best_max_distance:
        best_tour = tour
        best_max_distance = max_distance
        best_total_cost = total_cost
    elif max_distance == best_max_distance:
        if total_cost < best_total_cost:
            best_tour = tour
            best_total_cost = total_cost

# Output the best found tour, its total travel cost, and the max distance between any two consecutive cities
print("Tour:", best_tour)
print("Total travel cost:", best_total_cost)
print("Maximum distance between consecutive cities:", best_max_distance)