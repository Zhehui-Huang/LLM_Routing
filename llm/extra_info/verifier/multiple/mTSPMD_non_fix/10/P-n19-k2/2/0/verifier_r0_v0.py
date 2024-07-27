import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69),
    18: (45, 35)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Proposed solution
robot_0_tour = [0, 18, 13, 5, 6, 0]
robot_1_tour = [1, 2, 7, 15, 9, 8, 16, 17, 3, 12, 14, 11, 4, 10, 1]
robot_0_cost = 64.4088502512122
robot_1_cost = 133.928942180743
overall_cost_provided = 198.33779243195522

# Check whether solution meets the requirements
def verify_solution():
    # Requirement 2: Each city visited exactly once
    unique_cities = set(robot_0_tour + robot_1_tour)
    if len(unique_cities) != 19:
        return "FAIL"
    
    # Requirement 5: Minimizing cumulative distance (already reflected in the tours' predefined costs)
    computed_robot_0_cost = sum(calculate_distance(robot_0_tour[i], robot_0_tour[i+1]) for i in range(len(robot_0_tour)-1))
    computed_robot_1_cost = sum(calculate_distance(robot_1_tour[i], robot_1_tour[i+1]) for i in range(len(robot_1_tour)-1))
    computed_overall_cost = computed_robot_0_cost + computed_robot_1_cost

    # Allowing a small margin for float comparison
    if not (math.isclose(robot_0_cost, computed_robot_0_cost, rel_tol=1e-9) and
            math.isclose(robot_1_cost, computed_robot_1_cost, rel_tol=1e-9) and
            math.isclose(overall_cost_provided, computed_overall_cost, rel_tol=1e-9)):
        return "FAIL"
    
    return "CORRECT"

# Running the verification function
result = verify_solution()
print(result)