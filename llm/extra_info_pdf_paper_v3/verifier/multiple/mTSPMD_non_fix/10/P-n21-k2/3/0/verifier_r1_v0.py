import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Coordinates of each city indexed by city number
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Tours provided in the solution
robot_0_tour = [0, 5, 9, 17, 13, 18, 4, 15, 12, 10]
robot_1_tour = [1, 8, 14, 7, 20, 6, 16, 2, 3, 19, 11]

# Calculate the travel cost of a tour
def calculate_tour_cost(tour):
    cost = 0.0
    for i in range(1, len(tour)):
        cost += euclidean_distance(cities_coordinates[tour[i-1]], cities_coordinates[tour[i]])
    return cost

# Validating the provided solution
def validate_solution():
    # Check if all cities except depot cities (0 and 1) are visited exactly once
    visited = robot_0_tour + robot_1_tour
    unique_visited = set(visited)
    if len(unique_visited) != 21 or sorted(unique_visited) != list(range(21)):
        return "FAIL"
    
    # Check if robots start from designated depots
    if robot_0_tour[0] != 0 or robot_1_tour[0] != 1:
        return "FAIL"
    
    # Calculated costs from solution
    robot_0_calculated_cost = 133.02713542077208
    robot_1_calculated_cost = 164.25490167141817
    
    # Validate costs
    if (not math.isclose(calculate_tour_cost(robot_0_tour), robot_0_calculated_cost, rel_tol=1e-5) or
        not math.isclose(calculate_tour_cost(robot_1_tour), robot_1_calculated_cost, rel_tol=1e-5)):
        return "FAIL"
    
    # If all checks are correct
    return "CORRECT"

# Run the validation
result = validate_solution()
print(result)