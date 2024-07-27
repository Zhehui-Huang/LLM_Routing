import itertools
from math import sqrt, inf

# Coordinates of each city including the depot city
locations = [
    (9, 93),  # Depot city 0
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
    # Calculate max distance for any tour permutation including the start/depot
    min_max_distance = inf
    optimal_tour = None

    for perm in itertools.permutations(initial_path[1:]):  # Leave the depot city fixed
        current_path = [initial_path[0]] + list(perm) + [initial_path[0]]
        current_max_distance = max(calc_distance(current_path[i], current_path[i+1]) for i in range(len(current_path) - 1))
        if current_max_distance < min_max_distance:
            min_max_distance = current_max_distance
            optimal_tour = current_path

    return optimal_tour, min_max_distance

# Initiate list of cities for permutation
initial_path = list(range(len(locations)))

# Find optimal tour with minimized longest single trip between cities
optimal_tour, max_distance = all_pairs_max_path(initial_path)

# Calculate total travel cost of the optimal tour
total_travel_cost = sum(calc_distance(optimal_tour[i], optimal_tour[i + 1]) for i in range(len(optimal_tour) - 1))

# Output according to the required format
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")