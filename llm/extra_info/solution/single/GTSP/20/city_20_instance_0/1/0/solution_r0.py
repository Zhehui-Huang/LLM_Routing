import math
from itertools import product

# City coordinates
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

# Calculate Euclidean distance between two points
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Compute all distances between cities
distances = {}
for i in cities.keys():
    for j in cities.keys():
        distances[(i, j)] = euclidean_dictance(cities[i], cities[j])

# Brute-force the shortest route that visits exactly one city from each group
min_distance = float('inf')
best_tour = []

# Create all combinations of visiting one city from each group
for choice in product(*groups):
    # Permutate all combinations starting and ending at the depot
    for perm in itertools.permutations(choice):
        # Calculate the tour: start at the depot, visit the cities in 'perm', and return to the depot
        tour = [0] + list(perm) + [0]
        # Calculate total travel distance for this tour
        total_distance = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
        
        # Check if we found a new shorter route
        if total_distance < min_distance:
            min_distance = total_distance
            best_tour = tour

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", min_distance)