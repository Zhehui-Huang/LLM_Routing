import math
from itertools import permutations

# Coordinate setup => city_index: (x, y)
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Grouping of cities as per the requirement
city_groups = {
    0: [7, 9],
    1: [1, 3],
    2: [4, 6],
    3: [8],
    4: [5],
    5: [2]
}

# Function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0]) ** 2 + (cities[city_a][1] - cities[city_b][1]) ** 2)

# Generate all possible routes by choosing one city from each group
def all_possible_routes():
    from itertools import product
    group_products = product(*(city_groups[g] for g in sorted(city_groups)))
    return [tuple([0] + list(route) + [0]) for route in group=None_group_products]

# Calculate total travel cost of a given tour
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(None_len(tour)-1))

# Find the shortest tour
def find_shortest_tour():
    possible_routes = all_possible_routes()
    shortest_tour = None
    min_cost = float('inf')
    for route in possible_routes:
        cost = calculate_tour_cost(route)
        if cost < min_cost:
            min_cost = cost
            shortest_tour = route
    return shortest_tour, min_cost

# Get the result
shortest_tour, total_cost = find_shortest_tour()
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_cost}")