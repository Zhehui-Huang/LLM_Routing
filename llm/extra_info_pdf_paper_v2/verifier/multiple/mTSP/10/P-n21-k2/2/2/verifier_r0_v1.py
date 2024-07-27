import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def calculate_tour_cost(tour, city_coords):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(city_coords[tour[i]], cityCoords[tour[i + 1]])
    return round(cost, 2)

def verify_solution(robot_0_tour, robot_1_tour, city_coords):
    all_cities = set(range(1, 21))  # City indices excluding the depot
    visited_cities = set(robot_0_tour[1:-1] + robot_1_tour[1:-1])

    # Requirement 6 Check
    if visited_cities != all_cities:
        return "FAIL"

    # Requirement 2 Check
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0 or robot_1_tour[0] != 0 or robot_1_tour[-1] != 0:
        return "FAIL"

    # Calculate costs
    robot_0_cost = calculate_tour_cost(robot_0_tour, city_coords)
    robot_1_cost = calculate_tour_cost(robot_1_tour, city_coords)
    total_cost = robot_0_cost + robot_1_cost

    # Expected costs
    expected_robot_0_cost = 212.22
    expected_robot_1_cost = 184.31
    expected_total_cost = 396.53

    # Requirement 3 & 7 Check
    if robot_0_cost != expected_robot_0_cost or robot_1_cost != expected_robot_1_cost or total_cost != expected_total_cost:
        return "FAIL"

    return "CORRECT"

# City coordinates as provided
cityCoords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
              (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
              (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Tours provided
robot_0_tour = [0, 1, 3, 4, 8, 10, 11, 12, 15, 18, 19, 0]
robot_1_tour = [0, 2, 5, 6, 7, 9, 13, 14, 16, 17, 20, 0]

# Verify and print the result
result = verify_solution(robot_0_tour, robot_1_tour, cityCoords)
print(result)