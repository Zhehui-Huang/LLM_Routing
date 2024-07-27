import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(robot_tours, city_coords):
    # Cities and their coordinates
    robot_0_tour = robot_tours[0]
    robot_1_tour = robot_tours[1]
    
    # All cities indices
    all_cities = set(range(len(city_coords)))
    
    # Gather all visited cities
    visited_cities = set(robot_0_tour + robot_1_tour)
    
    # Check if every city is visited exactly once
    if visited_cities != all_cities:
        return "FAIL"
    
    # Check if each robot starts and ends at its depot
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0:
        return "FAIL"
    if robot_1_tour[0] != 1 or robot_1_tour[-1] != 1:
        return "FAIL"
    
    # Calculate travel cost and verify against provided
    total_calculated_cost = 0

    # Calculate cost for robot 0
    for i in range(len(robot_0_tour) - 1):
        total_calculated_cost += euclidean_distance(city_coords[robot_0_tour[i]], city_coords[robot_0_tour[i+1]])

    # Calculate cost for robot 1
    for i in range(len(robot_1_tour) - 1):
        total_calculated_cost += euclidean_distance(city_coords[robot_1_tour[i]], city_coords[robot_1_tour[i+1]])

    expected_cost = 297.1650480979624  # from the given solution
    if not math.isclose(total_calculated_cost, expected_cost, abs_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of cities
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Provided tours
robot_0_tour = [0, 6, 5, 14, 13, 11, 12, 19, 8, 20, 0]
robot_1_tour = [1, 4, 15, 10, 2, 7, 17, 9, 16, 3, 18, 1]

# Verify the solution
solution_status = verify_solution([robot_0_tour, robot_1_tour], city_coords)
print(solution_status)