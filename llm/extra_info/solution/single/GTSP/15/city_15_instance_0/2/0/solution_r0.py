import math
from itertools import product

# Coordinates for each city
cities = {
    0: (9, 93),
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

# Groups of cities
city_groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all possible tours that start and end at the depot and visit one city from each group
def generate_tours():
    for permuted_cities in product(*city_groups):
        yield [0] + list(permuted_cities) + [0]

# Calculate the cost of a given tour
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Find the shortest tour
shortest_tour, min_cost = None, float('inf')

for tour in generate_tours():
    cost = calculate_tour_cost(tour)
    if cost < min_cost:
        shortest_tour = tour
        min_cost = cost

# Output result
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {min_cost}")