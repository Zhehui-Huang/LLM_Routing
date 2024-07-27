import math
import itertools

# Define the cities and their coordinates
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

# Compute distances between all pairs of cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Distance matrix
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = calculate_distance(cities[i], cities[j])

# Find tours using brute-force search considering k = 7
k = 7
min_tour = None
min_cost = float('inf')

# Iterate over all combinations of 6 cities excluding depot
for combination in itertools.combinations(range(1, n), k - 1):
    current_combination = (0,) + combination + (0,)  # Add depot city at the start and end
    # Check all permutations of the inner cities to find shortest path
    for perm in itertools.permutations(current_combination[1:-1]):
        tour = (0,) + perm + (0,)
        cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        if cost < min_cost:
            min_cost = cost
            min_tour = tour

# Output the results
print(f"Tour: {list(min_tour)}")
print(f"Total travel cost: {min_cost:.2f}")