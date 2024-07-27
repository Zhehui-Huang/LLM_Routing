import math
from itertools import product

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define cities coordinates
city_coordinates = {
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

# Define city groups
city_groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Generate all possible selections of one city from each group
candidate_city_sets = [list(p) for p in product(*city_groups)]

# Include the depot (city 0) in the beginning and end
candidate_city_routes = [[0] + city_set + [0] for citySetValue in candidate_city_sets]

# Calculate route cost for each possible route
def calculate_route_cost(route, city_coords):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += euclidean_parametric_cost(city_coords[route[i]], city_coords[route[i + 1]])
    return total_cost

min_cost = float('inf')
optimal_route = []

for route in candidate_city_routes:
    cost = calculate_route_cost(route, city_coordinates)
    if cost < min_cost:
        min_cost = cost
        optimal_route = route

# Display results
print(f"Tour: {optimal_route}")
print(f"Total travel cost: {min_cost}")