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
    # Calculate max distance for any tour permutation
    n = len(initial_path)
    min_max_distance = inf
    optimal_tour = []

    for perm in itertools.permutations(initial_path[1:]):  # Leave the first city fixed for considering tours
        tour = [initial_path[0]] + list(perm) + [initial_path[0]]
        max_distance = max(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            optimal_tour = tour

    return optimal_tour, min_max_distance

# Generate a simple initial path (Greedy choice)
def greedy_initial_path(start):
    unvisited = set(range(1, len(locations)))
    current = start
    tour = [current]

    while unvisited:
        next_city = min(unchecked_city for unchecked_city in unvisited)
        unvisited.remove(next_city)
        tour.append(next_city)

    tour.append(start)  # Complete the tour back to the depot

    return tour

initial_tour = greedy_initial_path(0)
optimal_tour, bottleneck_distance = all_pairs_max_path(initial_tour)

total_travel_cost = sum(calc_distance(optimal_tour[i], optimal_tour[i+1]) for i in range(len(optimal_tour)-1))

# Prepare output according to the required format
output = {
    "Tour": optimal_tour,
    "Total travel cost": total_travel_cost,
    "Maximum distance between consecutive cities": bottleneck_distance
}

output