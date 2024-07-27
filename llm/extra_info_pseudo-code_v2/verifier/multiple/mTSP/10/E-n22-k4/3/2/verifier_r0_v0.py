import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

cities = {
    0: (145, 215), 1: (151, 264),  2: (159, 261),  3: (130, 254),  4: (128, 252), 
    5: (163, 247),  6: (146, 246),  7: (161, 242),  8: (142, 239),  9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

# Provided solution data
robots_data = {
    0: {"tour": [0, 4, 3, 2, 1, 5, 0], "cost": 139.44761634147744},
    1: {"tour": [0, 9, 6, 7, 8, 10, 0], "cost": 108.623496012051},
    2: {"tour": [0, 14, 15, 12, 11, 13, 0], "cost": 101.47821998346262},
    3: {"tour": [0, 18, 17, 20, 21, 19, 16, 0], "cost": 116.52547826679636}
}

def test_solution(robots_data, cities):
    total_cities_visited = set()
    expected_total_distance = 0.0

    for robot in robots_data.values():
        tour = robot["tour"]
        expected_cost = robot["cost"]
        calculated_cost = 0.0

        # Check if each tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check if the tour is valid and calculate the cost
        for i in range(len(tour) - 1):
            start_city = tour[i]
            end_city = tour[i + 1]
            total_cities_visited.add(start_city)
            distance = calculate_distance(cities[start_city], cities[end_city])
            calculated_cost += distance
        
        # Compare the calculated cost and expected cost
        if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-5):
            return "FAIL"

        expected_total_distance += expected_cost

    # Check if all cities are visited exactly once, excluding the depot
    if len(total_cities_visited) != 22 or 0 not in total_cities_visited:
        return "FAIL"

    # Check the cumulative cost
    total_reported_cost = sum(robot["cost"] for robot in robots_data.values())
    if not math.isclose(total_reported_cost, expected_total_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Execute the test
test_result = test_solution(robots_data, cities)
print(test_result)