import math

def calculate_travel_cost(tour, coords):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coords[tour[i]]
        x2, y2 = coords[tour[i+1]]
        total_cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total_cost

def test_solution():
    # Coordinates of each city
    coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
              (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
              (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
              (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

    # Tours and costs provided in the solution
    robot_0_tour = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    robot_0_cost = 247.1624868549446
    robot_1_tour = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    robot_1_cost = 257.7720534080389
    overall_cost = 504.93454026298355

    # Check Requirement 1: Each robot must visit each city exactly once
    all_cities_visited = sorted(robot_0_tour + robot_1_tour)
    if all_cities_visited != list(range(21)):
        return "FAIL"

    # Check Requirement 2: Robots start from specified depot and end at any city
    # Robot 0 starts at 0
    if robot_0_tour[0] != 0:
        return "FAIL"
    # Robot 1 starts at 1
    if robot_1_tour[0] != 1:
        return "FAIL"

    # Check Requirement 3: Validate the travel costs
    # Calculate the cost based on the provided tours
    calculated_robot_0_cost = calculate_travel_cost(robot_0_tour, coords)
    calculated_robot_1_cost = calculate_travel_cost(robot_1_tour, coords)
    calculated_overall_cost = calculated_robot_0_cost + calculated_robot_1_cost

    # Compare calculated costs with provided costs, allow small margin for floating-point comparison
    if not math.isclose(calculated_robot_0_cost, robot_0_cost, rel_tol=1e-5) or \
        not math.isclose(calculated_robot_1_cost, robot_1_cost, rel_tol=1e-5) or \
        not math.isclose(calculated_overall_cost, overall_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Test the solution
test_result = test_solution()
print(test_result)