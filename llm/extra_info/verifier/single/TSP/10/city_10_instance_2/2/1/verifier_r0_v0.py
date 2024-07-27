from math import sqrt

# Define the cities based on the given locations
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, reported_cost):
    """ Verify the proposed tour meets all requirements and calculate the total travel cost """
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city visited once
    visited = set(tour[1:-1])  # Exclude the depot city from the check
    if len(visited) != 9 or set(range(1, 10)) != visited:
        return "FAIL"

    # Requirement 3: Calculate the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i+1])

    # Check calculated cost with reported cost
    if abs(total_cost - reported_cost) > 0.001:  # Allowing for a small floating-point margin
        return "FAIL"

    return "CORRECT"

# Provided solution
solution_tour = [0, 3, 6, 4, 7, 2, 1, 9, 5, 8, 0]
reported_cost = 354.91010610434057

# Run test
test_result = verify_tour(solution_tour, reported_cost)
print(test_result)