import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_tsp_vrp_solution():
    # Provided city coordinates with indexes
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
        15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
    }
    
    robot_0_tour = [0, 18, 16, 17, 11, 4, 8, 7, 6, 0]
    robot_1_tour = [1, 13, 12, 15, 14, 10, 5, 2, 9, 3, 1]
    expected_total_cost = 426.9045844714489

    # Verify that all cities are covered exactly once except depots
    all_cities_visited = set(robot_0_tour + robot_1_tour)
    if len(all_cities_visited) != 19 or set(range(19)) != all_cities_visited:
        return "FAIL: Not all cities are visited exactly once."

    # Compute travel costs for each robot
    def compute_travel_cost(tour):
        total_cost = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            total_cost += euclidean_distance(*cities[city1], *cities[city2])
        return total_cost

    robot_0_cost = compute_travel_cost(robot_0_tour)
    robot_1_cost = compute_travel_cost(robot_1_tour)
    total_cost = robot_0_cost + robot_1_cost

    # Round the computed and expected cost to avoid floating point precision issues
    if round(total_cost, 3) != round(expected_total_cost, 3):
        return "FAIL: Travel costs do not match expected values."

    return "CORRECT"

# Run test function
print(test_tsp_vrp_solution())