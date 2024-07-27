import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# City coordinates map
city_coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Robot tours from the provided solution
robot_0_tour = [0, 6, 2, 7, 5, 9, 8, 3, 1, 4, 0]
robot_1_tour = [0, 18, 13, 15, 16, 17, 12, 14, 11, 10, 0]

def calculate_tour_cost(tour, city_coordinates):
    total_cost = 0.0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += calculate_euclidean_distance(
            city_coordinates[city1][0], city_coordinates[city1][1],
            city_coordinates[city2][0], city_coordinates[city2][1]
        )
    return total_cost

def tests():
    # Calculate costs from the solution
    actual_cost_robot_0 = calculate_tour_cost(robot_0_tour, city_coordinates)
    actual_cost_robot_1 = calculate_tour_cost(robot_1_tour, city_coordinates)

    # Expected costs
    expected_cost_robot_0 = 121.84817612829175
    expected_cost_robot_1 = 149.76726379384303
    
    # Setup the conditions
    costs_correct = (
        math.isclose(actual_cost_robot_0, expected_cost_robot_0, abs_tol=0.01) and
        math.isclose(actual_cost_robot_1, expected_cost_robot_1, abs_tol=0.01)
    )
    
    all_cities_covered_once = len(set(robot_0_tour + robot_1_tour) - {0}) == 18
    
    starts_ends_depot = robot_0_tour[0] == 0 and robot_0_tour[-1] == 0 and robot_1_tour[0] == 0 and robot_1_tour[-1] == 0
    
    # Verify conditions
    if costs_correct and all_cities_covered_once and starts_ends_depot:
        return "CORRECT"
    else:
        return "FAIL"

# Output the test result
output = tests()
print(output)