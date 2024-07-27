import math
from itertools import permutations

# City coordinates
cities = {
    0: (84, 67),  # depot city
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

# City groups
city_groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_tour_cost(tour):
    """ Calculate total cost of the given tour """
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean interpolation_distance(tour[i], tour[i + 1])
    return cost

def find_shortest_tour():
    """ Find the shortest possible tour visiting exactly one city from each group """
    shortest_tour = None
    min_cost = float('inf')

    # Generate all permutations of city groups
    all_group_permutations = permutations(city_groups)

    for group_perm in all_group_permutations:
        # For each permutation of groups, explore permutations within groups
        for city_selection in itertools.product(*group_perm):
            # Always start and end at the depot city
            current_tour = [0] + list(city_result) + [0]
            current_cost = calculate_tour_cost(current_tour)
            
            if current_cost < min_cost:
                min_cost = current_cost
                shortest_tour = current_tour

    return shortest_tour, min_cost

# Find the shortest tour
optimal_tour, optimal_cost = find_shortest_tour()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")