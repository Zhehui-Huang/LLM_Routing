import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_tour(city_positions, tour, total_cost, max_distance):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city visited exactly once
    if sorted(tour) != sorted([0] + list(range(1, len(city_positions)))):
        return "FAIL"

    # Requirement 4: Output as list of city indices
    if not isinstance(tour, list) or not all(isinstance(x, int) for x in tour):
        return "FAIL"

    # Calculate total travel cost and maximum distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(city_positions[tour[i]], city_positions[tour[i + 1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Requirement 5: Check total travel cost
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    # Requirement 6: Check maximum distance
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# City coordinates
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

# Proposed solution to test
tour = [6, 3, 0, 4, 1, 5, 7, 9, 8, 2, 6]
total_trip_cost = 324.6418061704166
max_trip_distance = 61.68468205316454

# Validate the solution
result = validate_tour(cities, tour, total_trip_cost, max_trip_distance)
print(result)