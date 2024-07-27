import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution():
    cities = {
        0: (30, 40),
        1: (37, 52),
        2: (49, 43),
        3: (52, 64),
        4: (31, 62),
        5: (52, 33),
        6: (42, 41),
        7: (52, 41),
        8: (57, 58),
        9: (62, 42),
        10: (42, 57),
        11: (27, 68),
        12: (43, 67),
        13: (58, 27),
        14: (37, 69),
        15: (61, 33),
        16: (62, 63),
        17: (63, 69),
        18: (45, 35)
    }

    # Expected output data:
    tours = {
        0: [0, 4, 11, 14, 12, 10, 1, 6, 18, 0],
        1: [0, 2, 7, 5, 13, 15, 9, 8, 16, 17, 3, 0]
    }
    expected_costs = {
        0: 97.33183067785306,
        1: 129.64737790420858
    }
    overall_expected_cost = 226.97920858206163

    visited_cities = set()
    total_robots = 2
    total_travel_cost = 0

    # Test each robot's tour
    for robot_id in range(total_robots):
        tour = tours[robot_id]
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL")
            return
        
        # Check if all cities are visited exactly once, exclude depot
        visited_cities.update(tour[1:-1])  # exclude first and last as they are depot
        
        # Calculate total travel cost for the robot
        robot_cost = 0
        for i in range(len(tour) - 1):
            city_a = tour[i]
            city_b = tour[i + 1]
            robot_cost += calculate_euclidean_accumulate_route(city_a, city_b, cities)
        
        total_travel_cost += robot_cost
        if not math.isclose(robot_cost, expected_costs[robot_id], abs_tol=1e-2):
            print("FAIL")
            return

    # Check if all cities except depot were visited exactly once
    if len(visited_cities) != len(cities) - 1:
        print("FAIL")
        return

    # Check overall cost
    if not math.isclose(total_travel_cost, overall_expected_cost, abs_tol=1e-2):
        print("FAIL")
        return

    print("CORRECT")

def calculate_euclidean_accumulate_route(city_a, city_b, cities):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return calculate_euclidean_distance(x1, y1, x2, y2)

test_solution()