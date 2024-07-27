import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Data initialization
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

# Tours given from the problem description
robot_tours = {
    0: [0, 6, 5, 7, 2, 1, 4, 3, 8, 9],
    1: [1, 11, 14, 12, 17, 16, 10, 18, 13, 15]
}

# Calculate the travel costs from the tours given
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour)-1):
        cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

# Test cases
def test_robot_tours():
    all_visited = set()
    for robot_id, tour in robot_tours.items():
        # Requirement 1: Visit each city once
        if len(tour) != len(set(tour)):
            return "FAIL"
        all_visited.update(tour)
    
    # Requirement 1: All cities must be visited
    if all_visited != set(cities.keys()):
        return "FAIL"
    
    # Requirement 2 and 3
    for robot_id, tour in robot_tours.items():
        # Starting at depot
        if tour[0] != robot_id:
            return "FAIL"
        # Ending at any city
        if tour[-1] not in cities:
            return "FAIL"
    
    # Requirement 6 (implicitly met by tours given)
    # Requirement 7 (implicitly met by correct total costs provided)

    # Compute costs
    expected_cost_robot_0 = 108.78362551868844
    expected_cost_robot_1 = 126.4816647620796
    actual_cost_robot_0 = calculate_tour_cost(robot_tours[0])
    actual_cost_robot_1 = calculate_tour_cost(robot_tours[1])

    if not math.isclose(actual_cost_robot_0, expected_cost_robot_0, abs_tol=0.01) or not math.isclose(actual_cost_robot_1, expected_cost_robot_1, abs_tol=0.01):
        return "FAIL"

    # Total costs
    total_expected_cost = 235.26529028076806
    actual_total_cost = actual_cost_robot_0 + actual_cost_robot_1
    if not math.isclose(actual_total_package, total_expected_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

result = test_robot_tours()
print(result)