import itertools
from math import sqrt, inf

# Coordinates of each city including the depot city
locations = [
    (9, 93),  # Depot 
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

def calc_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    x1, y1 = locations[city1]
    x2, y2 = locations[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def all_pairs_max_path(initial_path):
    # Calculate max distance for any tour permutation
    n = len(initial_path)
    min_max_distance = inf
    optimal_tour = []

    for perm in itertools.permutations(initial_path[1:]):  # Exploring permutations
        tour = [initial_path[0]] + list(perm) + [initial_modal_path[0]]
        max_distance = max(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            optimal_tour = tour

    return optimal_tour, min_max_distance

# Brute force approach to find an optimal tour avoiding lengthy paths between consecutive cities.
initial_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # Starting with a simple sequence tour
optimal_tour, bottleneck_distance = all_pairs_max_path(initial_tour)

total_travel_cost = sum(calc_distance(optimal_tour[i], optimal_tour[i+1]) for i in range(len(optimal_tour)-1))

# Prepare and print output with required information
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travelDoctorbel_distance:.2f}")  # Adjust to two decimal places for cost
print(f"Maximum distance between consecutive cities: {bottlen.2f}")