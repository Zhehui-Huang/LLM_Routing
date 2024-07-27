import math
from itertools import permutations

# City coordinates (City index is determined by order in the list)
coordinates = [
    (8, 11),  # City 0 (Depot)
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two cities given their coordinates."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Compute distances between all pairs of cities
n = len(coordinates)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

def total_tour_cost(tour):
    """Calculate the total travel cost of a tour."""
    cost = 0
    for k in range(len(tour) - 1):
        cost += distances[tour[k]][tour[k + 1]]
    return cost

# Generate all 3-city combinations from cities 1 to 19
from itertools import combinations

best_tour = None
min_cost = float('inf')

# Check each combination by linking with the depot city 0
for cities in combinations(range(1, n), 3):
    # Consider paths starting and ending at depot (0)
    current_tour = [0] + list(cities) + [0]
    # Since we need all permutations of the selected cities to check the minimal path
    for perm in permutations(cities):
        perm_tour = [0] + list(perm) + [0]
        cost = total_tour_cost(perm_tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = perm_tour

print("Tour:", best_tour)
print("Total travel cost:", min_cost)