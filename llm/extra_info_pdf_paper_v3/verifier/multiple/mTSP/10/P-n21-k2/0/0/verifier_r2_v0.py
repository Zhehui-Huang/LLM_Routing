import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def calculate_tour_cost(tour, cities_coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
    return total_cost

def unit_test_solution():
    # Cities with their coordinates
    cities_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
    }

    # Robots tours and provided costs
    robot_0_tour = [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 0]
    robot_0_cost = 135.56632457243472
    robot_1_tour = [0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 19, 0]
    robot_1_cost = 160.8323261436827
    overall_cost = 296.39865071611746

    # Test Requirement 2 - Start and end at depot
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0 or robot_1_tour[0] != 0 or robot_1_tour[-1] != 0:
        return "FAIL"

    # Test Requirement 3 - All cities visited exactly once
    total_cities_visited = sorted(robot_0_tour[1:-1] + robot_1_tour[1:-1])
    if total_cities_visited != list(range(1, 21)):
        return "FAIL"

    # Test Requirement 6 - Check total travel costs
    calculated_cost_0 = calculate_tour_cost(robot_0_tour, cities_coordinates)
    calculated_cost_1 = calculate_tour_cost(robot_1_tour, cities_coordinates)
    if not (math.isclose(calculated_cost_0, robot_0_cost, rel_tol=0.0001) and
            math.isclose(calculated_cost_1, robot_1_cost, rel_tol=0.0001) and
            math.isclose(calculated_cost_0 + calculated_cost_1, overall_cost, rel_tol=0.0001)):
        return "FAIL"

    # If all tests pass
    return "CORRECT"

# Execute the testing function
print(unit_test_solution())