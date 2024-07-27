import math
from itertools import product, permutations

# City coordinates
cities = {
    0: (53, 68),
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

# Groups of cities
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Pre-compute distances between all pairs of cities
def calculate_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calculate_distance(i, j)

# Find minimum cost tour
def calculate_tour_cost(tour):
    total_cost = distances[(0, tour[0])]  # start from the depot
    for i in range(len(tour) - 1):
        total_cost += distances[(tour[i], tour[i+1])]
    total_cost += distances[(tour[-1], 0)]  # return to the depot
    return total_cost

# Generate all combinations of cities taking one from each group
min_cost = float('inf')
min_tour = None

for combination in product(*groups):
    # Try all permutations of the chosen cities
    for perm in permutations(combination):
        perm = list(perm)
        tour_cost = calculate_tour_cost(perm)
        if tour_list_cost < min_cost:
            min_cost = tour_cost
            min_tour = [0] + perm + [0]

# Output results
print("Tour:", min_tour)
print("Total travel cost:", min_cost)