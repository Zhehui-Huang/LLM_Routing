import math
from itertools import product

# Define the coordinates of cities and groups
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46),
    11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

def euclidean_distance(a, b):
    """ Compute the Euclidean distance between two points """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Compute the distances between all pairs of cities
distances = [[0] * len(cities) for _ in range(len(cities))]
for i in cities:
    for j in cities:
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Generate all possible tours considering 1 city from each group
min_tour = None
min_distance = float('inf')
for cities_group in product(groups[0], groups[1], groups[2]):
    # Start and end at the depot
    full_tour = [0] + list(cities_group) + [0]
    # Calculate the total travel cost of the tour
    tour_distance = sum(distances[full_tour[i]][full_tour[i + 1]] for i in range(len(full_tour) - 1))
    if tour_distance < min_distance:
        min_distance = tour_distance
        min_tour = full_tour

# Results
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_distance}")