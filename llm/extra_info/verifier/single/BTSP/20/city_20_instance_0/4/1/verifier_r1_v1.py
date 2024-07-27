import math

# Coordinates of the cities
cities = [
    (8, 11),  # City 0 - Depot
    (40, 6),  # City 1
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
    (5, 59),  # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Solution provided
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 349.1974047195548
max_distance = 32.38826948140329

def compute_euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, total_travel_cost, max_distance):
    """Verify the tour based on the requirements."""
    # Requirement 1 & 5: Tour must start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city must be visited exactly once, excluding the final return.
    if len(set(tour[:-1])) != 20:
        return "FAIL"

    # Compute actual total travel cost and max distance
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        dist = compute_euclidean distance(cities[tour[i]], cities[tour[i + 1]])
        actual_total_cost += dist
        if dist > actual_max_distance:
            actual_max_distance = dist

    # Requirement 6: Total travel cost
    if not math.isclose(total_travel_cost, actual_total_cost, rel_tol=1e-9):
        return "FAIL"

    # Requirement 7: Maximum distance between consecutive cities
    if not math.isclose(max_distance, actual_max_distance, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Output the result of the tests
result = check_solution(tour, total_travel_cost, max_distance)
print(result)