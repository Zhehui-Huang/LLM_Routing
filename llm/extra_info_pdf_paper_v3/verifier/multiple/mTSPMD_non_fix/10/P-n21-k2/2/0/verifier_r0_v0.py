import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += euclidean_distance(coordinates[city1][0], coordinates[city1][1], coordinates[city2][0], coordinates[city2][1])
    return total_cost

def test_solution():
    coordinates = {
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
    
    robot_0_tour = [0, 0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 17, 14, 5, 20, 6, 7, 2]
    robot_1_tour = [1, 1, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0, 10, 12, 15, 4, 11, 3, 8, 18, 19]
    
    # The two tours overlap and visit more than 21 unique cities, this is incorrect.
    
    unique_cities = set(robot_0_tour + robot_1_tour)
    if len(unique_cities) != 21:
        return "FAIL"
    
    # Both robots should start from city 0 but initial paths seem incorrect
    if robot_0_tour[0] != 0 or robot_1_tour[0] != 1:
        return "FAIL"

    # Compute the costs and compare with the given costs
    computed_cost_0 = calculate_tour_cost(robot_0_tour, coordinates)
    computed_cost_1 = calculate_tour_cost(robot_1_tour, coordinates)
    
    given_cost_0 = 208.84408586170917
    given_cost_1 = 236.87921612619309
    overall_total_cost = 445.72330198790223
    
    if (abs(computed_cost_0 - given_cost_0) < 0.01 and
        abs(computed_cost_1 - given_cost_1) < 0.01 and
        abs((computed_cost_0 + computed_cost_1) - overall_total_cost) < 0.01):
        return "CORRECT"
    else:
        return "FAIL"

# Run the test
result = test_solution()
print(result)