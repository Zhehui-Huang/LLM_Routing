import itertools
import math

# Definition of the cities coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all permutations of cities excluding the starting city 0
perms = itertools.permutations(range(1, len(cities)))

min_max_distance = float('inf')
best_tour = None

# Search through all permutations for the best tour
for perm in perms:
    # Compute the complete route starting and ending at the depot (city 0)
    route = [0] + list(perm) + [0]
    max_distance = 0
    total_distance = 0

    # Check each segment of the tour
    for i in range(len(route) - 1):
        dist = calculate_distance(route[i], route[i+1])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist

    # Update best tour if the current one has a smaller maximum distance
    if max_distance < min_max_point_distance:
        min_max_point_distance = max_distance
        best_tour = route

# Output the best tour and its characteristics
print(f'Tour: {best_tour}')
print(f'Total travel cost: {total_distance:.2f}')
print(f'Maximum distance between consecutive cities: {min_max_point_distance:.2f}')