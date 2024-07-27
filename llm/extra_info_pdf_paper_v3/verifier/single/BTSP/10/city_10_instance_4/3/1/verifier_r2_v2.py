import math

# Provided data
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
tour = [0, 4, 3, 1, 5, 7, 9, 8, 2, 6, 0]
reported_total_cost = 337.17
reported_max_distance = 61.68

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_solution(tour, reported_total_cost, reported_max_distance):
    # Check Requirement 1: Starts and ends at 0, visits all cities exactly once
    if tour[0] != 0 or tour[-1] != 0 or sorted(tour[1:-1]) != sorted(list(cities.keys())[1:]):
        return "FAIL"

    # Calculate total travel cost and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(tour[i], tour[i + 1])
        calculated_total_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)

    # Check Requirement 2 & 3
    if not (math.isclose(calculated_total_cost, reported_total_cost, rel_tol=1e-2) and
            math.isclose(calculated_max_distance, reported_max_distance, rel_tol=1e-2)):
        return "FAIL"

    return "CORRECT"

# Run the test
result = check_solution(tour, reported_total_cost, reported_max_distance)
print(result)