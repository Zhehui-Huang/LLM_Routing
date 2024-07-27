import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def validate_solution(tour, total_cost, max_distance):
    # City coordinates
    cities = [
        (53, 68),  # Depot city 0
        (75, 11),  # City 1
        (91, 95),  # City 2
        (22, 80),  # City 3
        (18, 63),  # City 4
        (54, 91),  # City 5
        (70, 14),  # City 6
        (97, 44),  # City 7
        (17, 69),  # City 8
        (95, 89)   # City 9
    ]

    # Requirement 1: Robot must start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Robot must visit each city exactly once
    if len(set(tour)) != len(cities) or sorted(set(tour)) != sorted(range(len(cities))):
        return "FAIL"

    # Calculate tour costs for requirements 5 and 6
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(1, len(tour)):
        distance = euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Requirement 5: Check if the reported total travel cost is accurate
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    # Requirement 6: Check if the reported maximum distance between any two consecutive cities is accurate
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Given solution details
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost = 291.41
max_distance_between_cities = 56.61

# Execute the validation
result = validate_solution(tour, total_travel_cost, max_distance_between_cities)
print(result)