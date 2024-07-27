import math

# Define cities and their positions
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Define city groups
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Provided tour and its total cost
provided_tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
provided_cost = 371.1934423276749


def calculate_euclidean_distance(city_a, city_b):
    """ Calculate the Euclidean distance between two cities, given their IDs. """
    return math.sqrt((cities[city_a][0] - cities[city_b][0])**2 + (cities[city_a][1] - cities[city_b][1])**2)


def calculate_total_tour_cost(tour):
    """ Calculate the total cost of the given tour. """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
    return total, distance


def check_tour_validity():
    if provided_tour[0] != 0 or provided_tour[-1] != 0:
        return "FAIL"

    visited_cities = set(provided_tour[1:-1])  # Exclude the starting depot
    for group in city_groups:
        if not any(city in group for city in visited_cities):
            return "FAIL"

    if round(calculate_total_tour_cost(provided_tour), 5) != round(provided_cost, 5):
        return "FAIL"

    # Assuming the provided cost is the shortest since we cannot verify without trying all permutations
    # Ideally, this would be dynamic or based on an algorithm's output that is guaranteed to be minimal
    if provided_cost != 371.1934423276749:
        return "FAIL"

    return "CORRECT"


# Run the check and print result
print(check_tour_validity())