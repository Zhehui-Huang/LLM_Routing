import math
from itertools import permutations

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

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate all distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Attempt to find an optimal route
def find_optimal_tour():
    min_max_distance = float('inf')
    best_tour = None
    best_total_cost = None
    
    # We generate all permutations of cities (excluding the depot 0 which is start and end)
    for perm in permutations(range(1, 20)):
        tour = [0] + list(perm) + [0]
        max_distance = 0
        total_cost = 0
        for i in range(len(tour) - 1):
            d = distances[(tour[i], tour[i + 1])]
            total_cost += d
            if d > max_distance:
                max_distance = d
        # Update best tour found
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
            best_total_cost = total_cost
    
    return best_tour, best_total_cost, min_max_distance

# Finding an optimal tour
tour, total_cost, max_distance = find_optimal_tour()

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")