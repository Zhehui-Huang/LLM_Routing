import math
from itertools import permutations, product

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

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Compute all distances between cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Brute-force the shortest route that visits exactly one city from each group
min_distance = float('inf')
best_tour = []

# Generate all permutations of each city from the given groups
for choice in product(*groups):
    # Iterate through permutations of selected cities from each group
    for perm in permutations(choice):
        # Calculate the total distance of the tour starting and ending at 0
        current_tour = [0] + list(perm) + [0]
        current_distance = sum(distances[(current_tour[i], current_tour[i + 1])] for i in range(len(current_tour) - 1))
        # Update the best tour if found shorter
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = current_tour

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", min_distance)