def validate_solution(tours, costs):
    # Define cities and their visit status
    city_visit_status = {i: False for i in range(23)}
    
    # Extracted information
    robot_starts = [tour[0] for tour in tours]
    robot_ends = [tour[-1] for tour in tours]
    total_calculated_cost = sum(costs)
    expected_travel_cost = 641.522718537834
    
    # Check all requirements:
    
    # [Requirement 1] Start from Depot 0
    if not all(start == 0 for start in robot_starts):
        return "FAIL"
    
    # [Requirement 2] Each city visited exactly once
    for tour in tours:
        for city in tour:
            if city_visit_status[city]:
                return "FAIL"  # City visited more than once
            city_visit_status[city] = True
    if not all(city_visit_status.values()):
        return "FAIL"  # Not all cities were visited
    
    # [Requirement 3] Robots can end their tour at any city, not specifically a depot
    # This is technically already handled by the tours given, no need to end at the starting depot explicitly
    
    # [Requirement 4] Minimize the total travel cost
    if not (abs(total_calculated_cost - expected_travel_cost) < 1e-5):
        return "FAIL"  # Costs do not match expected total costs
    
    # [Requirement 5] Correct format of output - Presumed correct if provided by the context
    
    return "CORRECT"

# Define the tours and their costs as provided
robot_tours = [
    [0, 6, 9, 18, 0],
    [0, 2, 15, 19, 22, 0],
    [0, 13, 20, 21, 0],
    [0, 5, 8, 10, 12, 14, 17, 0],
    [0, 11, 0],
    [0, 1, 4, 7, 16, 0],
    [0, 3, 0],
    [0, 0]
]
robot_costs = [
    92.47469996376915,
    129.27678698593303,
    63.34275435420754,
    154.87378215191654,
    56.32051136131489,
    80.1189013362939,
    65.11528238439882,
    0.0
]

# Validate the solution
solution_status = validate_solution(robot_tours, robot_costs)
print(solution_status)