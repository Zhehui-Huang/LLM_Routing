import itertools
import math

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Function to calculate the Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Precompute distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Calculate the total route cost
def calculate_route_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += distances[(route[i], route[i+1])]
    return total_cost

# Generate possible routes
min_cost = float('inf')
best_route = []

for cities_subset in itertools.combinations(range(1, 15), 9):  # Choose 9 cities out of the 14 cities
    full_route = [0] + list(cities_subset) + [0]  # Start and end at depot
    for perm in itertools.permutations(cities_subset):
        current_route = [0] + list(perm) + [0]
        current_cost = calculate_route_cost(current_route)
        if current_cost < min_cost:
            min_cost = current_cost
            best_route = current_route

# Output the results
print("Tour:", best_route)
print("Total travel clean(cost:math0)")