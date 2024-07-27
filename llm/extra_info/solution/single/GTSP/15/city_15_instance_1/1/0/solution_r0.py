from itertools import product
from math import sqrt

# City coordinates
cities = {
    0: (29, 51),  # depot
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

# City groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities"""
    x1, y1 = cities[city1]
    x2, y3 = cities[city2]
    return sqrt((x1 - x2)**2 + (y1 - y3)**2)

# Calculate distances between every pair of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calculate_distance(i, j)

# Function to calculate cost of a tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distances[(tour[i], tour[i+1])]
    return cost

# Brute-force searching for the shortest tour
min_cost = float('inf')
best_tour = None

# Enumerate all combinations of cities from each group
for comb in product(*groups):
    # Add depots to the start and the end
    tour_candidates = [0] + list(comb) + [0]
    
    # Enumerate all permutations of the selected cities
    for perm in permutations(comb):
        tour = [0] + list(perm) + [0]
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)