import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_solution():
    # Cities coordinates
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
    ]

    # Solution paths
    robot_0_tour = [0, 6, 7, 5, 9, 2, 10, 4, 3, 8, 0]
    robot_1_tour = [1, 16, 20, 14, 17, 13, 18, 19, 12, 15, 11, 1]

    # Validate they return to their start/end at depot
    if not (robot_0_tour[0] == robot_0_tour[-1] == 0 and robot_1_tour[0] == robot_1_tour[-1] == 1):
        return "FAIL"

    # Calculate total distances
    def calculate_total_distance(tour):
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        return round(total_cost, 2)
        
    robot_0_cost = calculate_total_distance(robot_0_tour)
    robot_1_cost = calculate_total_distance(robot_1_tour)

    # Validate provided costs and overall total costs
    provided_robot_0_cost = 142.33
    provided_robot_1_cost = 133.34
    provided_overall_cost = 275.67

    if (round(robot_0_cost, 2) != provided_robot_0_cost or 
        round(robot_1_cost, 2) != provided_robot_1_cost or
        round(robot_0_cost + robot_1_cost, 2) != provided_overall_cost):
        return "FAIL"

    # Validate all cities are covered exactly once by exactly one robot
    all_cities_visited = set(robot_0_tour[1:-1] + robot_1_tour[1:-1])
    if sorted(all_cities_visited) != list(range(2, 21)):
        return "FAIL"

    return "CORRECT"

# Perform the test
print(validate_solution())