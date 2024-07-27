from math import sqrt
from itertools import combinations

# Cities coordinates; index is the city number
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
    19: (93, 15),
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generating all combinations of 3 non-depot cities
city_indices = list(cities.keys())
city_indices.remove(0)
combinations_of_cities = combinations(city_indices, 3)

min_cost = float('inf')
best_tour = []

# Evaluate each combination
for combo in combinations_of_cities:
    current_tour = [0] + list(combo) + [0]  # Start and end at the depot
    cost = sum(calculate_distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
    
    if cost < min_cost:
        min_cost = cost
        best_tour = current_tour

# Output the tour and the total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")