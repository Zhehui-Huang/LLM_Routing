import math

def euclidean_distance(x1, y1, x2, y2):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(robots_tours, city_coordinates):
    # Requirement constraints
    total_visited_cities = set()
    all_cities = set(range(1, 23))  # Excluding the depot city 0
    overall_cost_computed = 0.0
    
    # Verify each robot tour
    for robot_id, (tour, reported_cost) in enumerate(robots_tours):
        # Check start and end at the depot [Requirement 1 & 4]
        if tour[0] != 0 or tour[-1] != 0:
            print(f"Fail: Robot {robot_id} does not start or end at the depot.")
            return "FAIL"
        
        # Calculate tour cost and check against reported [Requirement 5]
        calculated_cost = 0.0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i+1]
            calculated_cost += euclidean_distance(*city_coordinates[city_from], *city_str_coordinates[city_to])
            
        if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
            print(f"Fail: Cost mismatch for Robot {robot_id}. Reported: {reported_cost}, Calculated: {calculated_cost}")
            return "FAIL"
        
        # Check visited cities [Requirement 3]
        visited_cities = set(tour[1:-1])
        if visited_cities & total_visited_cities:
            print(f"Fail: Robot {robot_id} visits cities that have been visited by other robots.")
            return "FAIL"
        total_visited_cities.update(visited_cities)
        
        # Accumulate total cost [Requirement 6]
        overall_cost_computed += calculated_cost

    # Check if all cities were visited [Requirement 3]
    if total_visited_cities != all_cities:
        print(f"Fail: Not all cities were visited. Visited: {total_visited_cities}, Expected: {all_cities}")
        return "FAIL"
    
    # Output the verified results
    return "CORRECT"

city_str_coordinates = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
                        7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
                        14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
                        21: (32, 39), 22: (56, 37)}

# Provided solution details
robots_tours = [([0, 16, 8, 0], 64.92216653342012),
                ([0, 1, 9, 17, 0], 81.65415032740114),
                ([0, 2, 18, 10, 0], 81.81803428067735),
                ([0, 3, 19, 11, 0], 108.81482905718964),
                ([0, 4, 12, 20, 0], 82.89654293014993),
                ([0, 13, 5, 21, 0], 68.39261497384648),
                ([0, 6, 22, 14, 0], 67.67055146540517),
                ([0, 7, 15, 0], 83.62034367443502)]

print(verify_solution(robots_tours, city_str_coordinates))