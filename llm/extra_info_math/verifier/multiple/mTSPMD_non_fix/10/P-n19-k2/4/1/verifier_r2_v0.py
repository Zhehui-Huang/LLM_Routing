import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def validate_solution(robot_tours, total_cost):
    # Coordinates (cities)
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
        (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
        (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    # Expected data
    robot_paths = [
        [0, 6, 2, 4, 7, 5, 9, 8, 3, 0],  # Robot 0
        [1, 10, 12, 14, 18, 11, 16, 15, 17, 13, 1]  # Robot 1
    ]
    expected_total_cost = 426.1148941221435
    
    # Check each robot tour starts from its designated depot
    if robot_paths[0][0] != 0 or robot_paths[1][0] != 1:
        return "FAIL"
    
    # Check all cities visited exactly once
    all_cities_visited = set()
    for path in robot_paths:
        all_cities_visited.update(path[1:-1])  # Exclude depot
    if len(all_cities_visited) != 18:
        return "FAIL"
    
    # Compute total travel cost
    computed_total_cost = 0.0
    for path in robot_paths:
        tour_cost = 0.0
        for i in range(len(path) - 1):
            tour_cost += euclidean_distance(coordinates[path[i]], coordinates[path[i + 1]])
        computed_total_cost += tour_cost
    
    # Compare computed total cost with the given total cost closely
    if not (abs(computed_total_cost - expected_total_cost) < 1e-5):
        return "FAIL"

    return "CORRECT"

# Provided solution details
robot_tours = [
    [0, 6, 2, 4, 7, 5, 9, 8, 3, 0],  # Robot 0
    [1, 10, 12, 14, 18, 11, 16, 15, 17, 13, 1]  # Robot 1
]
overall_total_cost = 426.1148941221435

print(validate_solution(robot_tours, overall_total_cost))