import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution():
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

    # Provided solution
    tour = [0, 2, 6, 5, 3, 13, 7, 4, 9, 11, 12, 14, 1, 10, 8, 0]
    reported_cost = 339.25546983499316
    
    # Requirement 1: There are 15 cities including the depot.
    if len(cities) != 15:
        return "FAIL"
    
    # Requirement 2: The depot city is city 0 with correct coordinates (9, 93).
    if cities[0] != (9, 93):
        return "FAIL"
    
    # Requirement 3: The tour starts and ends at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 4: The robot visits each city exactly once, excluding the depot city twice.
    if sorted(tour) != sorted([0] + list(range(1, 15)) + [0]):
        return "FAIL"

    # Requirement 5: Compute the travel cost and check against the reported cost.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Execute the verification function
print(verify_solution())