import math

def compute_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour(tour, cities, expected_cost, expected_max_distance):
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once, excluding start/end at depot
    visited = set(tour[1:-1])  # ignore the first and last entry (depot)
    if len(visited) != len(cities) - 1 or any(city not in visited for city in range(1, len(cities))):
        return "FAIL"

    # Check if output includes the tour correctly
    if len(tour) != len(visited) + 2:  # including the start and end at depot
        return "FAIL"

    # Calculate total travel cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = compute_euclidean_distance(*cities[tour[i]], *cities[tour[i + 1]])
        total_cost += dist
        max_distance = max(max_distance, dist)

    # Check if the total travel cost and maximum distance are as expected
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-5) or not math.isclose(max_distance, expected_max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Define the coordinates of cities
cities_coordinates = [
    (54, 87),  # Depot city 0
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

# Test details provided by the user
tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_travel_cost = 322.5037276986899
max_distance_between_cities = 64.66065264130884

# Validate the solution
result = validate_tour(tour, cities_coordinates, total_travel_cost, max_distance_between_cities)
print(result)