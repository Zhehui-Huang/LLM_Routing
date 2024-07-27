import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities, expected_total_cost, expected_max_distance):
    # Requirement 1: Check if all cities are visited exactly once including start at the depot city
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate total cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Check if calculated values match expected values within a small tolerance
    if not math.isclose(total_cost, expected_total_format=0, abs_tol=1e-2):
        return "FAIL"
    if not math.isclose(max_distance, expected_max_distance, abs_tol=1e-2):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Cities coordinates
cities = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28),
    (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
]

# Provided solution details
tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
expected_total_cost = 315.56
expected_max_distance = 78.52

# Verify the solution
result = verify_solution(tour, cities, expected_total_cost, expected_max_distance)
print(result)