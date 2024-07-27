import math
from itertools import product

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

# City groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible city combinations to visit (one from each group)
city_combinations = product(*groups)

# Function to calculate the total route cost
def calculate_route_cost(route):
    total_cost = 0
    current_city = route[0]
    for next_city in route[1:]:
        total_cost += euclidean_distance(current_city, next_city)
        current_city = next_city
    return total_cost

# Finding the best (minimum cost) route
min_cost = float('inf')
best_route = None

for combination in city_combinations:
    route = [0] + list(combination) + [0]
    cost = calculate_route_cost(route)
    if cost < min_cost:
        min_cost = cost
        best_route = route

# Output results
print(f"Tour: {best_route}")
print(f"Total travel cost: {round(min_cost, 2)}")