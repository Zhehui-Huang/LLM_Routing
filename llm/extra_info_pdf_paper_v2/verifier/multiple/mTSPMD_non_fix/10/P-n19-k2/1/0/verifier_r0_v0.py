import math

# Provided city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Robot tours
robot_0_tour = [0, 18, 6, 1, 10, 3, 17, 16, 8, 9, 15, 13, 5, 7, 2, 4, 11, 14, 12]
robot_0_cost = 181.49265243386333

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create a function to validate the solution
def validate_solution():
    # Check Requirement 1: Each robot visits all cities exactly once
    all_cities = set(range(len(cities)))
    visited_cities_robot_0 = set(robot_0_tour)

    if visited_cities_robot_0 != all_cities:
        return "FAIL"
    
    # Check Requirement 2: Each robot must start at Depot city 0
    if robot_0_tour[0] != 0:
        return "FAIL"

    # Check Requirement 4 and Requirement 6:
    calculated_cost_robot_0 = 0
    for i in range(len(robot_0_tour) - 1):
        calculated_cost_robot_0 += euclidean
        _distance(robot_0_tour[i], robot_0_tour[i + 1])
    
    if not math.isclose(calculated_cost_robot_0, robot_0_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Check total cost consolidation
    total_cost_calculated = calculated_cost_robot_0
    if not math.isclose(total_cost_calculated, robot_0_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Execute the validation function and print the result
result = validate_solution()
print(result)