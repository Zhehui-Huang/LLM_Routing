import math

# Given solution data
robot_0_tour = [0, 16, 5, 0]
robot_1_tour = [0, 2, 6, 18, 7, 13, 15, 9, 8, 17, 3, 12, 14, 11, 4, 10, 1, 0]
robot_0_cost = 94.11769035339026
robot_1_cost = 180.93336654488584
maximum_cost = 180.93336654488584

# City coordinates data
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Functions to calculate Euclidean distance
def calculate_distance(city_a, city_b):
    x1, y1 = city_coordinates[city_a]
    x2, y2 = city_coordinates[city_b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to verify the solution
def verify_solution():
    # Check all cities are visited exactly once excluding depot
    visited_cities = set(robot_0_tour[1:-1] + robot_0_tour[1:-1])
    if len(visited_cities) != 18:
        print("FAIL - Not all cities visited or some city visited more than once.")
        return "FAIL"
    
    # Check if both robots start and end at depot
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0 or robot_1_tour[0] != 0 or robot_1_tour[-1] != 0:
        print("FAIL - Robots do not start and end at the depot.")
        return "FAIL"
    
    # Check if travel cost matches the one calculated via distances
    def verify_tour_cost(tour):
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(tour[i], tour[i+1])
        return cost
    
    calculated_robot_0_cost = verify_tour_cost(robot_0_tour)
    calculated_robot_1_cost = verify_tour_cost(robot_1_tour)
    if not math.isclose(calculated_robot_0_cost, robot_0_cost) or not math.isclose(calculated_robot_1_cost, robot_1_cost):
        print("FAIL - Cost calculation mismatch.")
        return "FAIL"
    
    calculated_maximum_cost = max(calculated_robot_1_cost, calculated_robot_0_cost)
    if not math.isclose(calculated_maximum_cost, maximum_cost):
        print("FAIL - Maximum cost calculation mismatch.")
        return "FAIL"
    
    # All tests passed
    print("CORRECT")
    return "CORRECT"

# Execute the verification
verify_solution()