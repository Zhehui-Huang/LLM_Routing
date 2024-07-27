import math
from itertools import product

# Defined cities and their coordinates
cities = {
    0: (9, 93),  # Depot
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# City groups
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Calculate distance between two cities using Euclidean formula
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate a dictionary of distances between all city pairs
distances = {}
for city_a in cities:
    for city_b in cities:
        if city_a != city_b:
            distances[(city_a, city_b)] = calculate_distance(city_a, city_b)

# Brute force over all combinations in each group
min_cost = float('inf')
best_tour = []

# Iterate over all product combinations of 1 city from each group
for combination in product(groups[0], groups[1], groups[2]):
    # Always beginning at depot and ending at depot
    citizen_indices = [0] + list(combination) + [0]
    total_cost = sum(distances[(citizen_indices[i], citizen_indices[i+1])] for i in range(len(citizen_indices) - 1))
    
    if total_cost < min_cost:
        min_cost = total_cost
        best_tour = citizen_indices

# Printing the output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")