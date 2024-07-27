import math

# Given city coordinates
city_coordinates = [
    (54, 87),  # Depot City 0
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

# Solution from CBC MILP Solver
tour = [0, 2, 12, 3, 5, 10, 9, 7, 13, 4, 11, 1, 14, 8, 6, 0]
total_travel_cost = 343.12265870232255
max_distance_consecutive_cities = 39.05124837953327

def euclidean_distance(city_a, city_b):
    x1, y1 = city_coordinates[city_a]
    x2, y2 = city_coordinates[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost, max_distance):
    # Check starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour must start and end at depot."

    # Check each city is visited exactly once
    cities_visited = set(tour[1:-1])
    if len(cities_visited) != 14 or any(city not in cities_visited for city in range(1, 15)):
        return "FAIL: Each city must be visited exactly once."

    # Check total travel cost and max distance
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(tour[i], tour[i + 1])
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Compare calculated values with provided values
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL: Total travel cost does not match."
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-9):
        return "FAIL: Maximum distance between consecutive cities does not match."

    return "CORRECT"

# Perform the verification
verification_result = verify_solution(tour, total_travel_cost, max_distance_consecutive_cities)
print(verification_result)