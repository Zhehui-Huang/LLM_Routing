import math
from itertools import product

# Coordinates of cities
cities = {
    0: (53, 68),  # Depot
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# City groups
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

def calc_distance(c1, c2):
    """Calculate Euclidean distance between two cities"""
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate distances between every pair of cities
distances = {}
for c1, loc1 in cities.items():
    for c2, loc2 in cities.items():
        if c1 not in distances:
            distances[c1] = {}
        distances[c1][c2] = calc_distance(loc1, loc2)

# Find combinations of cities to visit, one from each group
all_combinations = list(product(*groups))

# Generate tours and compute travel costs
def compute_tour_cost(tour):
    total_cost = distances[0][tour[0]]  # start from depot to first city
    for i in range(len(tour) - 1):
        total_cost += distances[tour[i]][tour[i + 1]]
    total_cost += distances[tour[-1]][0]  # return to depot
    return total_cost

# Evaluate all combinations and find the one with the minimum travel cost.
best_tour = None
min_cost = float('inf')

for comb in all_combinations:
    comb = [0] + list(comb) + [0]  # start and end at the depot
    tour_cost = compute_tour_cost(comb)
    if tour_cost < min_cost:
        min_cost = tour_cost
        best_tour = comb

print("Tour:", best_tour)
print("Total travel cost:", min_cost)