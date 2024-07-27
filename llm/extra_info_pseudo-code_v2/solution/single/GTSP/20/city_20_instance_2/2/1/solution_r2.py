import math
from itertools import product

# Define city coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Define groups of cities
groups = [
    [7, 10, 11, 12],  # Group 0
    [3, 8, 13, 16],   # Group 1
    [2, 4, 15, 18],   # Group 2
    [1, 9, 14, 19],   # Group 3
    [5, 6, 17]        # Group 4
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate the cost of a given tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Generate all possible tours
all_possible_tours = product(*groups)

best_cost = float('inf')
best_tour = None

# Searching for the shortest tour
for possible_tour in all_possible_tours:
    tour = [0] + list(possible_tour) + [0]
    tour_cost = calculate_total_cost(tour)
    if tour_cost < best_cost:
        best_cost = tour_cost
        best_tour = tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)