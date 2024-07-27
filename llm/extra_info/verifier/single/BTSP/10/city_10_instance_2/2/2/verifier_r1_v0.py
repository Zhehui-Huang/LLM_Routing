import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cities):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city must be visited exactly once
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL"

    # Calculate total distance and maximum distance
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        total_distance += dist
        max_distance = max(max_distance, dist)

    # Results given in the solution
    given_total_distance = 418.32
    given_max_distance = 69.43

    # Requirement 6: Output must include the total travel cost of the tour
    if not math.isclose(total_distance, given_total_distance, abs_tol=0.01):
        return "FAIL"

    # Requirement 7: Output must include the maximum distance between consecutive cities in the tour
    if not math.isclose(max_distance, given_max_distance, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [
    (90, 3),  # City 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Provided solution
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]

# Verify the solution
result = verify_solution(tour, cities)
print(result)