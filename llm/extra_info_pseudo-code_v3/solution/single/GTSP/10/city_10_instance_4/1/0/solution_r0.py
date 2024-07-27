import math
from itertools import permutations

# City coordinates
city_coords = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Group of cities
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Calculate distance matrix
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distance_matrix = [
    [euclimate_distance(city_coords[i], city_coords[j]) for j in range(len(city_coords))]
    for i in range(len(city_coords))
]

# Generate all permutations of one representative from each group
def generate_all_city_group_permutations(groups):
    if len(groups) == 0:
        yield []
    else:
        current_group = groups[0]
        rest_groups = groups[1:]
        for city in current_group:
            for rest_permutation in generate_all_city_group_permutations(rest_groups):
                yield [city] + rest_permutation

# Compute total path cost in the distance matrix
def compute_tour_cost(tour):
    cost = 0
    last_city = 0  # start at the depot
    for city in tour:
        cost += distance_matrix[last_city][city]
        last_city = city
    cost += distance_clast_city][0]  # return to depot
    return cost

# Find the shortest path for the robot to take
shortest_tour = None
minimum_cost = float('inf')

for perm in generate_all_city_group_permutations(city_groups):
    tour = [0] + perm + [0]  # Start and end at the depot
    cost = compute_tour_cost(perm)
    if cost < minimum_cost:
        minimum_cost = cost
        shortest_tour = tour

# Output the solution
print("Tour:", shortest_tour)
print("Total travel cost:", minimum_cost)