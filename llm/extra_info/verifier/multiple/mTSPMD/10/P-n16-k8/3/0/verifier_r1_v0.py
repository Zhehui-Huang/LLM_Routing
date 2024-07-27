import math

# Cities coordinates as given
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Robot tour solutions and their reported costs
robot_solutions = [
    ([0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0], 173.0132333806203),
    ([1, 10, 12, 15, 4, 11, 3, 8, 13, 9, 7, 5, 14, 6, 2, 0, 1], 183.6071858764857),
    ([2, 7, 5, 14, 9, 13, 8, 3, 12, 15, 4, 11, 10, 1, 6, 0, 2], 168.68730261645365),
    ([3, 8, 13, 9, 7, 5, 14, 6, 2, 10, 1, 4, 11, 15, 12, 0, 3], 198.96976250793807),
    ([4, 11, 15, 12, 3, 8, 13, 9, 7, 5, 14, 6, 2, 10, 1, 0, 4], 170.1855619140049),
    ([5, 7, 2, 13, 9, 14, 6, 0, 1, 10, 12, 15, 4, 11, 3, 8, 5], 194.02846713211324),
    ([6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0, 6], 173.0132333806203),
    ([7, 5, 14, 9, 13, 2, 6, 0, 1, 10, 12, 15, 4, 11, 3, 8, 7], 175.56454652700504)
]

# Check if each robot starts and ends at its depot
def check_start_end_depot(robot_solutions):
    for i, (tour, _) in enumerate(robot_solutions):
        if tour[0] != i or tour[-1] != i:
            return False
    return True

# Check if each city is visited exactly once
def check_visit_once(robot_solutions, total_cities=16):
    visit_count = [0]*total_cities
    for tour, _ in robot_solutions:
        for city in tour:
            visit_count[city] += 1
    return all(count == 1 for count in visit_count[0:])

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Verify reported costs using Euclidean distance
def verify_costs(robot_solutions, cities_coordinates):
    total_cost = 0
    for tour, reported_cost in robot_solutions:
        cost = 0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
        if not math.isclose(cost, reported_cost, rel_tol=1e-3):
            return False
        total_cost += cost
    return total_cost

# Testing the solution provided
def test_solution(robot_solutions, cities_coordinates):
    if not check_start_end_depot(robot_solutions):
        return "FAIL"
    if not check_visit_once(robot_solutions):
        return "FAIL"
    calculated_total_cost = verify_costs(robot_solutions, cities_coordinates)
    if calculated_total_cost is False:
        return "FAIL"
    return "CORRECT"

# Output the test result
print(test_solution(robot_solutions, cities_coordinates))