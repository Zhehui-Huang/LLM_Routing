import math
from itertools import permutations

# Define the city coordinates as given
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Selecting a subset of k cities, starting with depot city 0 included
k = 10
selected_cities = [0]  # Including the depot city

# Heuristic: Select cities closest to current city, until we have k cities
while len(selected_cities) < k:
    last_city = selected_cities[-1]
    remaining_cities = [c for c in cities if c not in selected_cities]
    next_city = min(remaining_cities, key=lambda x: distance(last_city, x))
    selected_cities.append(next_city)

# Generate permutations of the selected cities to find the shortest route
min_tour = None
min_cost = float('inf')

for perm in permutations(selected_cities[1:]):  # Exclude depot city 0 for permutation
    tour = [0] + list(perm) + [0]  # Start and end at the depot
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if total_cost < min_cost:
        min_tour = tour
        min_cost = total_cost

# Output the best tour and its cost
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost:.2f}")