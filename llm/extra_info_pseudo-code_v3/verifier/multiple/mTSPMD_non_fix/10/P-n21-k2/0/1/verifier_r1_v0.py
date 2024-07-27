import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        cost += euclidean_distance(*coordinates[city1], *coordinates[city2])
    return round(cost, 2)

def test_solution():
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
        (45, 35)
    ]

    robot_0_tour = [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 0]
    robot_1_tour = [0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0]
    robot_0_cost = calculate_cost(robot_0_tour, coordinates)
    robot_1_cost = calculate_cost(robot_1_tour, coordinates)
    total_cost = robot_0_cost + robot_1_cost
    
    all_cities_visited = sorted(set(robot_0_tour[1:-1] + robot_1_tour[1:-1]))
    correct_travel_cost_robot_0 = 121.54
    correct_travel_cost_robot_1 = 105.47
    correct_total_travel_cost = 227.01

    if len(all_cities_visited) != 20: # Check if all 20 cities are visited excluding depots
        return "FAIL"

    if not (robot_0_cost == correct_travel_cost_robot_0 and robot_1_cost == correct_travel_cost_robot_1):
        return "FAIL"

    if not round(total_cost, 2) == correct_total_travel_cost:
        return "FAIL"

    return "CORRECT"

# Run the test function
print(test_solution())