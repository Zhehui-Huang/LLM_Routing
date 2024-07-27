from itertools import permutations
from math import sqrt

# Define coordinates of cities
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

def compute_distance(city1, city2):
    """ Compute Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def bottleneck_tsp():
    city_count = len(cities)
    min_bottleneck_value = float('inf')
    optimal_tour = []

    # Loop over each possible permutation of cities (excluding the starting city 0)
    for perm in permutations(range(1, city_count)):
        current_tour = [0] + list(perm) + [0]
        max_edge_cost = max(compute_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
        total_cost = sum(compute_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))

        # Check if the current permutation yields a new minimum bottleneck value
        if max_edge_cost < min_bottleneck_value:
            min_bottleneck_value = max_edge_cost
            optimal_tour = current_tour
            optimal_total_cost = total_cost

    return optimal_tour, optimal_total_cost, min_bottleneck_value

# Execute the function and print results
tour, total_cost, max_distance = bottleneck_tsp()
formatted_tour = 'Tour: ' + str(tour)
formatted_total_cost = 'Total travel cost: ' + str(round(total_cost, 2))
formatted_max_distance = 'Maximum distance between consecutive cities: ' + str(round(max_distance, 2))

print(formatted_tour)
print(formatted_total_cost)
print(formatted_max_distance)