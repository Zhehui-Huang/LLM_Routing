import math
from itertools import permutations

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible tours, skipping the depot city 0 in permutations
min_tour = None
min_cost = float('inf')

all_cities = list(cities.keys())
other_cities = all_cities[1:]  # Exclude the depot city from the tour permutations

for perm in permutations(other_cities):
    tour = [0] + list(perm) + [0]
    cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    if cost < min_cost:
        min_cost = cost
        min_tour = tour

# Output results
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost:.2f}")