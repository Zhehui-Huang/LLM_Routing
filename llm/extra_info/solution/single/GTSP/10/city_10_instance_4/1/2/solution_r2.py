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

# Precompute distances between all pairs of cities
distances = {}
for c1 in cities:
    for c2 in cities:
        if c1 != c2:
            distances[(c1, c2)] = distance(c1, c2)

# Function to calculate the cost of a given tour
def calculate_tour_cost(tour):
    total_cost = distances[(0, tour[0])] + distances[(tour[-1], 0)]  # from depot to first and last to depot
    for i in range(1, len(tour)):
        total_cost += distances[(tour[i-1], tour[i])]
    return total_cost

# Generate all combinations of choosing one city from each group and evaluate them
min_cost = float('inf')
best_tour = []

all_combinations = [0] + [None]*len(groups) + [0]  # Tour template, starting and ending at the depot

# Iterating over permutations of one city from each group
for perm in permutations([min(group) for group in groups]):  # Choose the minimum indexed city in each group
    tour_candidate = [0] + list(perm) + [0]
    tour_cost = calculate_tour_cost(tour_candidate)
    if tour_cost < min_cost:
        min_cost = tour_cost
        best_tour = tour_candidate

# Output the final results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)