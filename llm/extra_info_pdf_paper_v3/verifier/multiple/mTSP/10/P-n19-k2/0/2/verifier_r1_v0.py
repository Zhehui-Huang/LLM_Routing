import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

def check_provided_tours():
    # Coordinates of the cities
    coordinates = {
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
    
    # Robot 0 and Robot 1 tours
    robot_0_tour = [0, 6, 18, 15, 7, 8, 16, 12, 11, 10, 0]
    robot_1_tour = [0, 1, 4, 14, 3, 17, 9, 13, 5, 2, 0]
    
    # Calculating costs
    calculated_robot_0_cost = calculate_tour_cost(robot_0_tour, coordinates)
    calculated_robot_1_cost = calculate_tour_cost(robot_1_tour, coordinates)
    
    # Total costs validation
    total_calculated_cost = calculated_robot_0_cost + calculated_robot_1_cost
    
    # Expected costs
    expected_robot_0_cost = 146.56445621046797
    expected_robot_1_cost = 143.37198532416284
    expected_total_cost = 289.93644153463083

    # Check cost calculations
    if not math.isclose(calculated_robot_0_cost, expected_robot_0_cost, rel_tol=1e-9) or \
       not math.isclose(calculated_robot_1_cost, expected_robot_1_cost, rel_tol=1e-9) or \
       not math.isclose(total_calculated_cost, expected_total_cost, rel_tol=1e-9):
        return "FAIL"

    # Check if all cities are visited exactly once and tours are correct
    visited_cities = set(robot_0_tour[1:-1] + robot_1_tour[1:-1])
    if len(visited_cities) != 18 or visited_cities != set(range(1, 19)):
        return "FAIL"
    
    # Check if tours start and end at depot
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0 or robot_1_tour[0] != 0 or robot_1_tour[-1] != 0:
        return "FAIL"
    
    return "CORRECT"

# Running the test
result = check_provided_tours()
print(result)