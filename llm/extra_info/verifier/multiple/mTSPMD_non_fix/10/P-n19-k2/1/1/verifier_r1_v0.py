import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_tour_cost(tour, coordinates):
    total_cost = 0.0
    for i in range(1, len(tour)):
        x1, y1 = coordinates[tour[i - 1]]
        x2, y2 = coordinates[tour[i]]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    return total_cost

def test_solution():
    # Given coordinates and depot assignment
    coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
                   (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
                   (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
    # Provided solution
    robot_0_tour = [0, 6, 18, 5, 13, 15, 9, 2, 7, 8, 16, 17, 3, 12, 14, 4, 11, 10]
    robot_1_tour = [1]
    robot_0_cost = 160.72
    robot_1_cost = 0.00
    overall_cost = 160.72

    # Test Requirement 1: Robots start from depot city 0
    if robot_0_tour[0] != 0 or robot_1_tour[0] != 1:
        return "FAIL"

    # Test Requirement 3: Each city is visited exactly once
    unique_cities_visited = set(robot_0_tour[1:] + robot_1_tour[1:])
    if len(unique_cities_visited) != 18 or sorted(unique_cities_visited) != list(range(2, 19)):
        return "FAIL"

    # Test Requirement 4, 6: Check tours start from assigned depot
    if robot_0_tour[0] != 0 or robot_1_tour[0] != 1:
        return "FAIL"

    # Test Requirement 7: Check costs are correct
    calculated_robot_0_cost = calculate_tour_cost(robot_0_tour + [robot_0_tour[-1]], coordinates)
    calculated_robot_1_cost = calculate_tour_cost(robot_1_tour + [robot_1_tour[-1]], coordinates)
    calculated_overall_cost = calculated_robot_0_cost + calculated_robot_1_cost

    if not (math.isclose(calculated_robot_0_cost, robot_0_cost, abs_tol=0.1) and 
            math.isclose(calculated_robot_1_cost, robot_1_cost, abs_tol=0.1) and
            math.isclose(calculated_overall_cost, overall_cost, abs_tol=0.1)):
        return "FAIL"

    # If all tests pass
    return "CORRECT"

# Run the test function
result = test_solution()
print(result)