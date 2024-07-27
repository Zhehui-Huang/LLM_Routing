import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(tour, total_cost, cities):
    # Check requirement 1
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Check requirement 2
    if len(tour) != 5:  # Since it must start and end at the same city, thus 4 + 1 entries.
        return "FAIL"

    # Check requirement 3 (Calculating the tour cost based on provided cities and tour):
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])

    if not math.isclose(calculated_cost, total_cost, rel_tol=0.01):  # Allows a small error tolerance
        return "FAIL"

    return "CORRECT"

# Define cities coordinates with city index as key
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

# Provided solution details
tour_solution = [0, 1, 10, 8, 0]
total_travel_cost_solution = 90.54

# Verify the solution
result = verify_solution(tour_solution, total_travel_case_solution, cities)
print(result)  # Should print "CORRECT" if everything is correct according to requirements