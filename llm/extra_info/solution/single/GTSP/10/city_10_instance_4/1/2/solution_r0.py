import math
from itertools import permutations

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Groups of cities
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Precompute distances between all city pairs
distances = {}
for c1 in cities:
    for c2 in cities:
        if c1 != c2:
            distances[(c1, c2)] = distance(c1, c2)

# Generate all permutations of one city from each group
group_permutations = permutations([g[0] for g in groups])  # Taking first city from each group

# Calculate cost of tour
def calculate_tour_cost(tour):
    total_cost = distances[(0, tour[0])] + distances[(tour[-1], 0)]  # from depot to first and last to depot
    for i in range(len(tour) - 1):
        total_cost += distances[(tour[i], tour[i + 1])]
    return total_cost

# Find shortest tour over all permutations
min_cost = float('inf')
best_tour = None

for perm in group_permutations:
    perm = tuple([0] + list(perm) + [0])  # Insert depot at the start and end
    cost = calculate_tour_cost(perm)
    if cost < min_cost:
        min_cost = cost
        best_tour = perm

# Output the result
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {min_tour_cost}")