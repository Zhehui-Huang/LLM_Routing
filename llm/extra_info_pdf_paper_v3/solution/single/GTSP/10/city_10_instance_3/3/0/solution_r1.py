import itertools
import math

# City coordinates
cities = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# City groups
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += euclidean_distance(cities[route[i]], cities[route[i+1]])
    return total_distance

# Find the shortest tour
best_distance = float('inf')
best_route = []

for combination in itertools.product(*groups):
    full_route = [0] + list(combination) + [0]
    total_distance = calculate_total_distance(full_route)
    if total_distance < best_distance:
        best_distance = total_distance
        best_route = full_route

# Output the best tour and total travel cost
print(f"Tour: {best_route}")
print(f"Total travel cost: {best_distance:.2f}")