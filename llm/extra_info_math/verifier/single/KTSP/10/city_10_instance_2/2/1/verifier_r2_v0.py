import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_solution(tour, cost):
    coordinates = {
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

    # [Requirement 1] The robot must start and end at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] The tour must consist of exactly 6 cities, including the depot city.
    if len(tour) != 7 or len(set(tour)) != 7:  # 6 unique cities + depot city (twice)
        return "FAIL"

    # [Requirement 3] Minimize the total Euclidean distance traveled by the robot.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])

    # Allow very minor floating point discrepancies in cost calculations
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Given solution data
tour = [0, 8, 5, 2, 1, 9, 0]
total_travel_cost = 183.85354044487238

# Verify the solution
result = validate_solution(tour, total_travel_cost)
print(result)