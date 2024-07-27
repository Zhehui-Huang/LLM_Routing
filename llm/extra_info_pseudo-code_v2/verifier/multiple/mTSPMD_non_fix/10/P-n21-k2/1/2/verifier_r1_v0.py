import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(robot_0_tour, robot_0_cost, robot_1_tour, robot_1_cost, overall_cost):
    cities_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 
        18: (62, 63), 19: (63, 69), 20: (45, 35)
    }
    
    # Verify Cities Coverage and Starting Depots
    all_cities = set(range(21))
    visited_cities = set(robot_0_tour + robot_1_tour)
    if visited_cities != all_cities:
        return "FAIL"
    if robot_0_tour[0] != 0 or robot_1_tour[0] != 1:
        return "FAIL"
    
    # Check that there are no duplicates except for the depots
    if len(robot_0_tour) != len(set(robot_0_tour)) or len(robot_1_tour) != len(set(robot_1_tour)):
        return "FAIL"

    # Costs Calculation
    def get_tour_cost(tour):
        return sum(calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]]) 
                   for i in range(len(tour) - 1))

    calc_robot_0_cost = get_tour_cost(robot_0_tour)
    calc_robot_1_cost = get_tour_cost(robot_1_tour)
    
    if not (abs(calc_robot_0_cost - robot_0_cost) < 1e-5 and abs(calc_robot_1_cost - robot_1_cost) < 1e-5):
        return "FAIL"
    
    # Overall Cost
    if not abs((robot_0_cost + robot_1_cost) - overall_cost) < 1e-5:
        return "FAIL"

    return "CORRECT"

# Provided solution data
robot_0_tour = [0, 3, 4, 10, 16, 14, 5, 2, 8, 19, 0]
robot_0_cost = 198.29406454275986
robot_1_tour = [1, 18, 7, 20, 13, 11, 15, 12, 6, 17, 9, 1]
robot_1_cost = 214.9655386800923
overall_cost = 413.25960322285215

# Run the verification
result = verify_solution(robot_0_tour, robot_0_cost, robot_1_tour, robot_1_cost, overall_cost)
print(result)