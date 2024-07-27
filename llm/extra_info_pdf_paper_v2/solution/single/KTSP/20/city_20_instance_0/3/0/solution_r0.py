import itertools
import math

# Given cities coordinates
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

# Euclidean distance calculation
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Search all combinations of 3 cities (plus the depot city 0)
comb = itertools.combinations(range(1, 20), 3)
best_tour = None
best_cost = float('inf')

for cities_set in comb:
    # All permutations of the selected cities starting from the depot city
    for perm in itertools.permutations(cities_set):
        tour = [0] + list(perm) + [0]
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if cost < best_cost:
            best_cost = cost
            best_tour = tour

# Providing the solution
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")