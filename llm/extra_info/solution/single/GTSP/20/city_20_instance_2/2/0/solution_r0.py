import itertools
import math

# City coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# City groups
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate total distance for the tour
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += distance(tour[i-1], tour[i])
    return total_distance

# Generate all permutations of selecting one city from each group
candidates = itertools.product(*groups)

# Find the solution with the minimum distance
def find_min_tour():
    min_distance = float('inf')
    shortest_tour = []
    for candidate in candidates:
        tour = [0] + list(candidate) + [0]  # start and end at the depot
        tour_distance = calculate_total_distance(tour)
        if tour_distance < min_distance:
            min_distance = tour_distance
            shortest_tour = tour
    return shortest_tour, min_distance

# Get the best tour and its cost
best_tour, best_cost = find_min_tour()

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)