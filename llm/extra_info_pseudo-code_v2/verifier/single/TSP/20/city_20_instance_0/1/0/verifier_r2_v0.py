import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def check_solution(tour, total_cost, coordinates):
    # Check Requirement 1: The robot must start and end the tour at the depot city, which is city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: The robot must visit each city exactly once, excluding the depot.
    visited_cities = set(tour)
    expected_cities = set(range(20))  # Cities 0 through 19
    if visited_cities != expected_cities:
        return "FAIL"

    # Check Requirement 3: Calculate the travel cost as the Euclidean distance between cities.
    computed_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        computed_cost += calculate_euclidean_distance(coordinates[city_a][0], coordinates[city_a][1],
                                                      coordinates[city_b][0], coordinates[city_b][1])

    if not math.isclose(computed_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Define the city coordinates as given in the description
coordinates = [
    (8, 11),   # City 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Given solution
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_cost = 349.1974047195548

# Check and print the veracity of the solution
result = check_solution(tour, total_config, coordinates)
print(result)