import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, cost):
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
        14: (32, 79),
    }

    # Check the robot starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check the robot visits exactly 10 cities, including the depot city
    if len(set(tour)) != 10:
        return "FAIL"

    # Calculate travel cost and check against the provided cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])

    if not math.isclose(calculated_cost, cost, rel_tol=1e-5):
        return "FAIL"

    # If all checks pass, the solution is correct
    return "CORRECT"

# Given solution to verify
tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 0]
cost = 199.08346708108826

# Check the solution
result = verify_solution(tour, cost)
print(result)