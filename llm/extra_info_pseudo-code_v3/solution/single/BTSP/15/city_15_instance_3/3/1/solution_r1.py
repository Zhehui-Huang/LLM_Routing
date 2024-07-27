import math
from itertools import permutations

# Coordinates of the cities
cities = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create matrix of distances for quick access
n = len(cities)
distances = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Start from the depot, check all permutations of other cities
best_path = None
min_bottleneck = float('inf')
for perm in permutations(range(1, n)):  # Permutate all cities except the depot
    path = [0] + list(perm) + [0]
    current_max_edge = max(distances[path[i]][path[i + 1]] for i in range(len(path) - 1))
    if current_max_edge < min_bottleneck:
        min_bottleneck = current_max_edge
        best_path = path

# Calculate the total cost of the optimal path found
total_cost = sum(distances[best_path[i]][best_path[i + 1]] for i in range(len(best_path) - 1))

# Output the results
print(f"Tour: {best_path}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {min_bottleneck}")