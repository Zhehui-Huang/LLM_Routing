import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tsp_vrp_solution():
    cities = {
        0: (30, 40),
        1: (37, 52),
        2: (49, 49),
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
        13: (58, 48),
        14: (58, 27),
        15: (37, 69),
        16: (38, 46),
        17: (61, 33),
        18: (62, 63),
        19: (63, 69),
        20: (45, 35)
    }
    
    # Provided solution
    robot_0_tour = [0, 1, 3, 4, 10, 11, 12, 15, 16, 19]
    robot_1_tour = [2, 5, 6, 7, 8, 9, 13, 14, 17, 18, 20]
    robot_0_cost = 164.23
    robot_1_cost = 171.26
    total_cost = 335.49

    # Requirement 1: Each robot must visit all cities exactly once
    all_cities_visited = sorted(robot_0_tour + robot_1_tour)
    expected_cities = list(range(21))
    if all_cities_visited != expected_cities:
        return "FAIL"
    
    # Requirement 2: Each tour must start at the robot's designated depot
    if robot_0_tour[0] != 0 or robot_1_tour[0] != 2:
        return "FAIL"

    # Requirement 5: Calculate travel costs as the Euclidean distance between two cities
    calculated_robot_0_cost = sum(calculate_distance(cities[robot_0_tour[i]], cities[robot_0_tour[i+1]])
                                  for i in range(len(robot_0_tour) - 1))
    calculated_robot_1_cost = sum(calculate_distance(cities[robot_1_tour[i]], cities[robot_1_tour[i+1]])
                                  for i in range(len(robot_1_tour) - 1))
    if not math.isclose(robot_0_cost, calculated_robot_0_cost, rel_tol=0.01) or \
       not math.isclose(robot_1_cost, calculated_robot_1_cost, rel_tol=0.01):
        return "FAIL"

    # Requirement 6: Check total cost
    if not math.isclose(total_cost, robot_0_cost + robot_1_cost, rel_tol=0.01):
        return "FAIL"

    return "CORRECT"
    
# Run the test
result = test_tsp_vrp_solution()
print(result)