import math
from itertools import product

# Coordinates of cities
cities = {
    0: (9, 93),  # depot city
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4,39)
}

# Groups of cities
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

# Calculate distance dictionary
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Find all combinations for visiting one city from each group
all_tours = product(groups[0], groups[1], groups[2])

# Calculate total travel cost for each tour and find the minimum cost tour
min_cost = float('inf')
best_tour = None

for tour in all_tours:
    # Starting and ending at depot (0)
    full_tour = [0] + list(tour) + [0]
    # Calculate the cost of the current tour
    cost = sum(distances[(full_tour[i], full_tour[i+1])] for i in range(len(full_tour) - 1))
    # Check if we found a new minimum cost tour
    if cost < min_cost:
        min_cost = cost
        best_tour = full_tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")