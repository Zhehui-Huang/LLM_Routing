import math
from scipy.spatial.distance import euclidean
from itertools import permutations

# Helper function to calculate Euclidean distance
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities Coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Number of cities
N = len(cities)

# Compute all pairwise distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calculate_distance(cities[i], cities[j])

# Create a list of cities excluding the depot
cities_to_visit = list(cities.keys())[1:]

min_max_edge = float('inf')
best_tour = None

# Brute-force permutation to find the best tour minimizing the maximum distance between consecutive cities
for perm in permutations(cities_to_visit):
    tour = [0] + list(perm) + [0]
    max_edge = max(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
    if max_edge < min_max_edge:
        min_max_edge = max_edge
        best_tour = tour

# Calculate the total travel cost of the best tour
total_cost = sum(distances[(best_tour[i], best_tour[i + 1])] for i in range(len(best_tour) - 1))

print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(min_max(int(distance), 2))