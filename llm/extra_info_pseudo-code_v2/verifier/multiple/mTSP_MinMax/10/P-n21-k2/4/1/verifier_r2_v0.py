import math

# Coordinates of cities including the depot city (city 0).
CITIES = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

ROBOT_TOURS = {
    0: [0, 1, 2, 3, 4, 5, 0],
    1: [0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    x1, y1 = CITIES[city1]
    x2, y2 = CITIES[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def test_solution(tours, expected_costs):
    """ Perform tests on the solution. """
    computed_costs = []
    visited_cities = set()
    
    for tour in tours.values():
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(tour[i], tour[i + 1])
            visited_cities.add(tour[i])
        visited_cities.add(tour[-1])
        computed_costs.append(cost)
    
    if not all(city in visited_cities for city in range(1, 21)):
        return "FAIL: Not all cities are visited."
    
    if 0 in visited_cities and visited_cities.count(0) != 2 * len(tours):
        return "FAIL: Depot city visits are incorrect."
    
    if any(abs(cost - expected) > 1e-3 for cost, expected in zip(computed_costs, expected_costs)):
        return "FAIL: Computed costs do not match expected costs."

    if max(computed_costs) != max(expected_costs):
        return "FAIL: Maximum travel cost does not match the expected maximum."

    return "CORRECT"

# Expected costs as given in the problem statement
EXPECTED_COSTS = [121.54566285797682, 348.1448530084161]

# Test the solution
test_result = test_solution(ROBOT_TOURS, EXPECTED_COSTS)
print(test_result)