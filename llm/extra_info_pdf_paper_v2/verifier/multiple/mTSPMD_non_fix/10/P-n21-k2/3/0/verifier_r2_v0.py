import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0.0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    return round(total_cost, 2)

def validate_solution():
    # Provided solution
    robot_0_tour = [0, 16, 2, 4, 11, 15, 18, 9, 17, 7, 0]
    robot_1_tour = [1, 10, 12, 3, 19, 8, 13, 6, 20, 5, 14, 1]
    robot_0_cost = 150.7
    robot_1_cost = 133.86
    total_cost = 284.55
    
    # City coordinates
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
        (45, 35)
    ]
    
    # Check if each city is visited exactly once
    all_cities_visited = set(robot_0_tour[1:-1] + robot_1_tour[1:-1])
    if len(all_cities_visited) != 20:  # 20 cities apart from the starting depots
        return "FAIL"
    
    # Validate tours start and end at their depots
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0:
        return "FAIL"
    if robot_1_tour[0] != 1 or robot_1_tour[-1] != 1:
        return "FAIL"
    
    # Verify travel costs
    calculated_robot_0_cost = calculate_total_travel_cost(robot_0_tour, coordinates)
    calculated_robot_1_cost = calculate_total_travel_cost(robot_1_tour, coordinates)
    calculated_total_cost = round(calculated_robot_0_cost + calculated_robot_1_cost, 2)
    
    if not (math.isclose(robot_0_cost, calculated_robot_0_cost, rel_tol=1e-02) and
            math.isclose(robot_1_cost, calculated_robot_1_cost, rel_tol=1e-02) and
            math.isclose(total_cost, calculated_total_cost, rel_tol=1e-02)):
        return "FAIL"

    return "CORRECT"

# Run validation
result = validate_solution()
print(result)