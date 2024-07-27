import itertools
import math

# Define city coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Define city groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Calculate distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all possible routes by picking one city from each group
all_routes = itertools.product(*groups)

# Evaluate each possible route and find the one with the minimum total travel cost
min_cost = float('inf')
best_route = None

for route in all_routes:
    # Start and end at the depot cityg
    full_route = [0] + list(route) + [0]
    total_cost = sum(distance(full_route[i], full_route[i+1]) for i in range(len(full_route) - 1))
    
    if total_cost < min_cost:
        min_cost = total_cost
        best_route = full_route

# Output the best route and its corresponding cost
print("Tour:", best_route)
print("Total travel cost:", round(min_cost, 2))