import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return total_cost

def test_solution():
    # City Coordinates
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64),
        (31, 62), (52, 33), (42, 41), (52, 41),
        (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 27), (37, 69), (61, 33),
        (62, 63), (63, 69), (45, 35)
    ]

    # Expected tours and costs
    robot_0_tour = [0, 6, 2, 7, 5, 9, 8, 3, 4, 1, 0]
    robot_1_tour = [0, 10, 11, 14, 12, 17, 16, 15, 13, 18, 0]
    robot_0_cost_expected = 115.60
    robot_1_cost_expected = 149.77
    
    # Calculate travel costs
    robot_0_cost_calculated = calculate_total_travel_cost(robot_0_tour, coordinates)
    robot_1_cost_calculated = calculate_total_travel_cost(robot_1_tour, coordinates)
    
    # Check if all cities are visited exactly once excluding the depot city
    visited_cities = set(robot_0_tour[1:-1] + robot_1_tour[1:-1])
    all_cities = set(range(1, 19))

    # Results check
    is_correct = (
        visited_cities == all_cities and
        len(robot_0_tour) == len(set(robot_0_tour)) and
        len(robot_1_tour) == len(set(robot_1_tour)) and
        robot_0_tour[0] == robot_0_tour[-1] == 0 and
        robot_1_tour[0] == robot_1_tour[-1] == 0 and
        np.isclose(robot_0_cost_calculated, robot_0_cost_expected, rtol=1e-2) and
        np.isclose(robot_1_cost_calculated, robot_1_cost_expected, rtol=1e-2) and
        np.isclose(robot_0_cost_calculated + robot_1_cost_calculated, 265.37, rtol=1e-2)
    )

    print("CORRECT" if is_correct else "FAIL")

test_solution()