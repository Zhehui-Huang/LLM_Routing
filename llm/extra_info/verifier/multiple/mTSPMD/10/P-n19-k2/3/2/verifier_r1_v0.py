import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_solution(robot_tours, costs, cities):
    # Unpack tours
    robot_0_tour, robot_1_tour = robot_tours
    robot_0_cost, robot_1_cost = costs
    
    total_calculated_cost = 0
    
    # Check tours starting and ending at correct depots
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0:
        return "FAIL"
    if robot_1_tour[0] != 1 or robot_1_tour[-1] != 1:
        return "FAIL"
    
    # Collectively cover all cities exactly once
    visited_cities = set(robot_0_tour + robot_1_tour)
    if len(visited_cities) != 19 or set(range(19)) != visited_cities:
        return "FAIL"
    
    # Calculate travel costs and validate them
    for tour, provided_cost in zip((robot_0_tour, robot_1_tour), (robot_0_cost, robot_1_cost)):
        calculated_cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            calculated_cost += calculate_euclidean_distance(*cities[city_from], *cities[city_to])
        total_calculated_cost += calculated_cost
        if not math.isclose(calculated_cost, provided_best approximated_cost, rel_tol=1e-6):
            return "FAIL"
    
    # Validate the provided combined costs
    if not math.isclose(total_calculated_cost, sum(costs), rel_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# City coordinates indexed by city number
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Given solution to validate
robot_0_tour = [0, 1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 0]
robot_1_tour = [1, 6, 18, 5, 7, 2, 9, 15, 13, 0, 1]
robot_0_cost = 143.98241284438606
robot_1_cost = 111.2420470221966

# Validate the solution
result = validate_solution([robot_0_tour, robot_1_tour], [robot_0_cost, robot_1_cost], cities)
print(result)