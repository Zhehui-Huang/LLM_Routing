import math

# Data as per the problem statement
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Solution provided (robot tours)
robot_tours = [
    [0, 10, 8, 6, 3, 4, 11, 0],
    [0, 17, 20, 18, 21, 19, 0],
    [0, 9, 7, 5, 2, 1, 0],
    [0, 14, 16, 13, 12, 15, 0]
]

reported_costs = [99.61, 115.49, 111.84, 84.94]
max_reported_cost = 115.49

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def test_solution():
    # Testing Requirement 1: All robots start and end at city 0
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Testing Requirement 2: All cities visited exactly once
    visited_cities = set()
    for tour in robot_tours:
        visited_cities.update(tour[1:-1])  # skip the depot (0) at the ends
    if sorted(list(visited_cities)) != list(range(1, 22)):  # cities 1 to 21 should be visited
        return "FAIL"
    
    # Calculate actual costs and compare to reported costs
    actual_costs = []
    for tour in robot_tours:
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_distance(tour[i], tour[i + 1])
        actual_costs.append(total_cost)
    
    # Testing Requirement 3: Minimize the maximum travel distance
    # Here we simply check if the reported maximum matches the calculated one
    max_cost = max(actual_costs)
    if not math.isclose(max_cost, max_reported_cost, rel_tol=1e-3):
        return "FAIL"

    # Testing Requirement 4 and Requirement 5: Costs are calculated correctly and reported correctly
    for reported_cost, actual_cost in zip(reported_costs, actual_costs):
        if not math.isclose(reported_cost, actual_cost, rel_tol=1e-3):
            return "FAIL"
    
    return "CORRECT"

# Running the test
test_result = test_solution()
print(test_result)