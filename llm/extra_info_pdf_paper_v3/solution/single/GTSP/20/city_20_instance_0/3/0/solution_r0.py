import math
from itertools import product

# Cities and their coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# City groups
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Function to compute Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Precompute distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Evaluate all possible tours
def evaluate_tours():
    min_tour_cost = float('inf')
    optimal_tour = None

    for tour in product(*groups):
        # Ensure unique cities in tour by checking if all are unique
        if len(set(tour)) == len(tour):
            # Building complete tour with depot start and return
            full_tour = [0] + list(tour) + [0]
            tour_cost = sum(distances[(full_tour[i], full_tour[i+1])] for i in range(len(full_tour) - 1))

            if tour_cost < min_tour_cost:
                min_tour_cost = tour_cost
                optimal_tour = full_tour
    
    return optimal_tour, min_tour_cost

# Find the optimal tour and its cost
optimal_tour, min_tour_cost = evaluate_tours()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", min_tour_cost)