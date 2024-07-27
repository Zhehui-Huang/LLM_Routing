import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_solution(cities, robot_tours):
    # Ensure all cities are visited exactly once and the tour starts/ends at the assigned depots
    visited_cities = set()
    for tour in robot_tours:
        # Check if the tour starts and ends at the robot's designated depot
        if tour[0] != tour[-1]:
            return "FAIL"
        visited_cities.update(tour)

    if visited_cities != set(range(len(cities))):
        return "FAIL"

    # Compute and validate travel costs
    robot_0_tour = [0, 6, 2, 7, 5, 9, 8, 3, 4, 0]
    expected_robot_0_cost = 112.0719227360316
    robot_1_tour = [1, 10, 12, 14, 11, 16, 17, 15, 13, 18, 1]
    expected_robot_1_cost = 151.74982440173858
    overall_cost = expected_robot_0_cost + expected_robot_1_cost

    robot_0_actual_cost = sum(euclidean_distance(cities[robot_0_tour[i]], cities[robot_0_tour[i + 1]]) for i in range(len(robot_0_tour) - 1))
    robot_1_actual_cost = sum(euclidean_distance(cities[robot_1_tour[i]], cities[robot_1_tour[i + 1]]) for i in range(len(robot_1_tour) - 1))
    
    if not (math.isclose(robot_0_actual_cost, expected_robot_0_cost, rel_tol=1e-9) and
            math.isclose(robot_1_actual_cost, expected_robot_1_cost, rel_tol=1e-9) and
            math.isclose(robot_0_actual_cost + robot_1_actual_check, overall_cost, rel_tol=1e-9)):
        return "FAIL"

    return "CORRECT"

# City coordinates, including depots
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
          (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

robot_tours = [
    [0, 6, 2, 7, 5, 9, 8, 3, 4, 0], # Robot 0 Tour with associated depot city 0
    [1, 10, 12, 14, 11, 16, 17, 15, 13, 18, 1] # Robot 1 Tour with associated depot city 1
]

# Call the verification function and print the result
result = verify_solution(cities, robot_tours)
print(result)