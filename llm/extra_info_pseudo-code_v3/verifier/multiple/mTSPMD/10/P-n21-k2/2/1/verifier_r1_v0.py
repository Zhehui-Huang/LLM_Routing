import math

def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
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
    
    robot_0_tour = [0, 5, 7, 0]
    robot_1_tour = [1, 2, 1]
    given_robot_0_total_cost = 53.10950830677563
    given_robot_1_total_cost = 24.73863375370596
    given_overall_total_cost = 77.84814206048159
    
    # Check each robot starts and ends at their respective depots
    if not (robot_0_tour[0] == robot_0_tour[-1] == 0 and robot_1_tour[0] == robot_1_tour[-1] == 1):
        return "FAIL"
    
    # Check each city is visited exactly once by any robot
    all_visited_cities = robot_0_tour[1:-1] + robot_1_tour[1:-1]
    all_cities = list(range(2, 21))
    if sorted(all_visited_cities) != sorted(all_cities):
        return "FAIL"
    
    # Check if travel cost is calculated correctly
    def calculate_total_cost(tour):
        total_cost = 0.0
        for i in range(len(tour) - 1):
            total_cost += compute_distance(cities[tour[i]], cities[tour[i+1]])
        return total_cost
    
    calc_robot_0_cost = calculate_total_cost(robot_0_tour)
    calc_robot_1_cost = calculate_total_cost(robot_1_tour)
    
    if not (abs(calc_robot_0_cost - given_robot_0_total_cost) < 1e-5 and
            abs(calc_robot_1_cost - given_robot_1_total_cost) < 1e-5):
        return "FAIL"
    
    # Check Objective
    calc_total_cost = calc_robot_0_cost + calc_robot_1_cost
    if abs(calc_total - given_total_cost) < 1e-5:
        return "FAIL"
    
    return "CORRECT"

print(test_solution())