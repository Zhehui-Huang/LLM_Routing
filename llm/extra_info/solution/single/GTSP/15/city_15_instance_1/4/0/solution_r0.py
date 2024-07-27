import math
from itertools import product

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Groups of cities
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Calculate all pairwise distances
distances = {
    (i, j): euclidean_distance(i, j) for i in cities for j in cities
}

# Find all possible tours
min_cost = float('inf')
best_tour = None

for tour in product(*groups):
    full_tour = [0] + list(tour) + [0]
    cost = sum(distances[full_tour[i], full_tour[i+1]] for i in range(len(full_tour) - 1))
    if cost < min_cost:
        min_cost = cost
        best_tour = full_tour

# Output the best tour and the total travel cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)