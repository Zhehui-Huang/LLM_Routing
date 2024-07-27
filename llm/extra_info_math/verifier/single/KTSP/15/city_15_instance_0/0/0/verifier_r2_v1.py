import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, reported_cost, cities):
    """ Verify the solution against the requirements. """
    # Requirement 1: Start and end at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Exactly 4 cities including the depot
    if len(set(tour)) != 4:
        return "FAIL"

    # Requirement 3: Correct calculation of travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# City coordinates
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
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Test provided solution
tour = [0, 1, 10, 8, 0]
reported_cost = 90.54

result = verify_solution(tour, reported_cost, cities)
print(result)