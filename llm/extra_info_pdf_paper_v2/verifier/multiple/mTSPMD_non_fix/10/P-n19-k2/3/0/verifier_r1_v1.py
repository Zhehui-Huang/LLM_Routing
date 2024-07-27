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

# Tours given from the problem
robot_tours = {
    0: [0, 6, 5, 7, 2, 1, 4, 3, 8, 9],
    1: [1, 11, 14, 12, 17, 16, 10, 18, 13, 15]
}

# Calculate the travel costs from the tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour)-1):
        cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

# Unit tests to verify requirements
def test_robot_tours():
    all_visited = set()
    for robot_id, tour in robot_tours.items():
        # Requirement 1: Visit each city once per tour
        if len(tour) != len(set(tour)):
            return "FAIL"
        all_visited.update(tour)
    
    # Requirement 1: All cities must be visited exactly once collectively
    if all_visited != set(cities.keys()):
        return "FAIL"
    
    # Requirement 2 and 3: Each robot starts its tour from the designated depot
    for robot_id, tour in robot_tours.items():
        if tour[0] != robot_id:  # should start from its depot
            return "FAIL"
        if tour[-1] not in cities:  # should end at a valid city
            return "FAIL"
    
    # Calculate expected and actual costs
    expected_costs = [108.78362551868844, 126.4816647620796]
    actual_costs = [calculate_tour_cost(tour) for tour in robot_tours.values()]

    for actual, expected in zip(actual_costs, expected_costs):
        if not math.isclose(actual, expected, abs_tol=0.01):
            return "FAIL"

    # Total cost check
    total_expected_cost = 235.26529028076806
    actual_total_cost = sum(actual_costs)
    if not math.isclose(actual_total_cost, total_expected_total_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

result = test_robot_tours()
print(result)