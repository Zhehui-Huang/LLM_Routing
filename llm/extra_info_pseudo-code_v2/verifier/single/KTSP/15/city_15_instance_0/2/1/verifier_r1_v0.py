import math

# Provided cities coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Solution provided
tour = [0, 8, 10, 11, 0]
reported_cost = 110.00961484483386

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution(tour, reported_cost):
    # Checking Requirement 1 and 5
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Checking Requirement 2
    if len(set(tour)) != 4 or len(tour) != 5:
        return "FAIL"

    # Calculate actual total travel cost
    actual_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    # Checking Requirement 6
    if not math.isclose(actual_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Solution is correct based on the given test scenario
    return "CORRECT"

# Test the solution
result = test_solution(tour, reported_cost)
print(result)