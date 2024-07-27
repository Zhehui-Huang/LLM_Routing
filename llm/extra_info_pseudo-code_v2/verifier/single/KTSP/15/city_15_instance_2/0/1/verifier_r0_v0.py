import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost):
    # City coordinates with city index as key
    cities = {
        0: (54, 87),
        1: (21, 84),
        2: (69, 84),
        3: (53, 40),
        4: (54, 42),
        5: (36, 30),
        6: (52, 82),
        7: (93, 44),
        8: (21, 78),
        9: (68, 14),
        10: (51, 28),
        11: (44, 79),
        12: (56, 58),
        13: (72, 43),
        14: (6, 99)
    }
    
    # Check Requirement 1: Start and end at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Visit exactly 8 cities including the depot
    if len(tour) != 9:
        return "FAIL"

    # Check Requirement 3: Calculate the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    # Check Requirement 4: Format of the output
    # Format is ensured by the coder, automatically correct if above passes.

    return "CORRECT"

# Solution provided
tour_solution = [0, 6, 11, 12, 4, 3, 13, 2, 0]
total_cost_solution = 132.1185774560832

# Checking the solution
verification_result = verify_solution(tour_solution, total_cost_solution)
print(verification_result)