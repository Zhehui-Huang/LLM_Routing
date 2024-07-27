import math
from itertools import product

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

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distances between all pairs of cities and store in dictionary
distances = {}
for i in cities:
    for j in cities:
        if i <= j:  # Store once as distances are symmetrical
            distances[(i, j)] = euclidean_contribution(cities[i], cities[j])
        else:
            distances[(i, j)] = distances[(j, i)]

def compute_cost(tour):
    # Computes the total cost of the given tour that starts and ends at the depot city
    cost = distances[(0, tour[0])]
    for i in range(len(tour) - 1):
        cost += distances[(tour[i], tour[i+1])]
    cost += distances[(tour[-1], 0)]
    return cost

# Generate all product combinations of cities (1 from each group)
all_combinations = list(product(*groups))
minimal_cost = float('inf')
best_tour = []

# Evaluate each combination for the shortest circular tour
for combination in all_combinations:
    potential_tour = list(combination)
    potential_cost = compute_cost(potential_tour)
    if potential_cost < minimal_cost:
        minimal_cost = potential_cost
        best_tour = potential_tour

# Output the best tour, adding depot city at the start and the end
final_tour = [0] + best_tour + [0]

print(f"Tour: {final_tour}")
print(f"Total travel cost: {minimal_cost:.2f}")