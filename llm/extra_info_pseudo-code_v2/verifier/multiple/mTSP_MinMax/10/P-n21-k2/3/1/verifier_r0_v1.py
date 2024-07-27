import math

# Cities coordinates with city index
city_coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
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
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution(tours, expected_costs, max_cost):
    visited_cities = [city for tour in tours for city in tour if city != 0]
    
    if len(set(visited_cities)) != 20 or len(visited_cities) != 20:
        return "FAIL - Not all cities are visited exactly once"

    computed_costs = []
    for tour in tours:
        cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        computed_costs.append(cost)

    # Check costs are accurately reported within a small threshold
    if any(abs(computed_costs[i] - expected_costs[i]) >= 1e-2 for i in range(len(expected_costs))):
        return "FAIL - Cost mismatch"

    # Check if the maximum cost is correctly determined within a small threshold
    if abs(max(computed_costs) - max_cost) >= 1e-2:
        return "FAIL - Max cost mismatch"

    # Check tours start and end at depot (0)
    if any(tour[0] != 0 or tour[-1] != 0 for tour in tours):
        return "FAIL - Tours do not start and end at depot"

    return "CORRECT"

# Provided tours and costs
robot_tours = [
    [0, 4, 11, 15, 12, 3, 19, 18, 2, 16, 0],
    [0, 6, 20, 7, 5, 14, 17, 9, 13, 8, 10, 1, 0]
]
robot_costs = [113.76761794786297, 113.47599976519697]
max_travel_cost = 113.76761794786297

# Call the revised test function
result = test_solution(robot_tours, robot_costs, max_travel_cost)
print(result)