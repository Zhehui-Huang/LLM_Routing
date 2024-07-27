import math

# Test data set including the coordinates of cities
cities_coordinates = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, reported_cost):
    # Check requirement 1 and 4: Tour must start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check requirement 2: Exactly 10 cities, including the depot
    if len(tour) != 11:  # 10 cities + 1 return to the depot
        return "FAIL"

    # Check requirement 3 and 5: Minimize and report travel cost correctly
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(tour[i], tour[i + 1])

    if abs(calculated_cost - reported_cost) > 1e-2:  # allowing minor floating-point discrepancies
        return "FAIL"

    return "CORRECT"

# Provided solution to test
tour = [0, 10, 8, 11, 3, 4, 1, 13, 14, 9, 0]
reported_cost = 290.18

# Perform the test
test_result = verify_solution(tour, reported_cost)
print(test_result)