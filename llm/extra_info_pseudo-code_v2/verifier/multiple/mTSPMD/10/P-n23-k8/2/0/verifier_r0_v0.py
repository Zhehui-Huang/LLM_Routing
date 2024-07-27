import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution():
    # Coordinates of each city
    city_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35), 21: (32, 39), 22: (56, 37)
    }
    
    # Provided solution details - Robot tour and travel costs
    robot_tour = [5, 14, 17, 9, 22, 7, 2, 13, 8, 18, 19, 3, 12, 15, 4, 11, 10, 1, 16, 21, 0, 6, 20, 5]
    reported_cost = 192.0845769149381
    # Check unique cities
    city_count = len(set(robot_tour))
        
    # Visiting all cities exactly once check
    if city_count != 23:
        return "FAIL"
    
    # Starting and ending at initial depot
    if robot_tour[0] != robot_tour[-1]:
        return "FAIL"
    
    # Calculate travel cost based on Euclidean distance
    computed_cost = 0
    for i in range(len(robot_tour) - 1):
        city1 = robot_tour[i]
        city2 = robot_tour[i + 1]
        computed_cost += calculate_euclidean_distance(*(city_coordinates[city1] + city_coordinates[city2]))
    
    # Cost should be within a small tolerance of reported cost due to floating point arithmetic errors
    if not math.isclose(computed_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks passed
    return "CORRECT"

# Execution of the created verification function
verification_result = verify_solution()
print(verification_result)