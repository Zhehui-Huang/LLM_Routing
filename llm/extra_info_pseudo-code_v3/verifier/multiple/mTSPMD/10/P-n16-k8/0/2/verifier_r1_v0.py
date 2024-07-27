import math
from collections import Counter

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities coordinates (including depots)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41), 
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Simulated solution output
output = {
    "robots": [
        {"tour": [0, 8, 9, 0], "cost": 67},
        {"tour": [1, 10, 11, 1], "cost": 56},
        {"tour": [2, 12, 13, 2], "cost": 47},
        {"tour": [3, 14, 15, 3], "cost": 78},
        {"tour": [4, 6, 5, 4], "cost": 62},
        {"tour": [5, 7, 14, 5], "cost": 45},
        {"tour": [6, 12, 10, 6], "cost": 53},
        {"tour": [7, 11, 15, 7], "cost": 72}
    ],
    "overall_cost": 480
}

def test_solution(output):
    # Requirement 1: Start and end at assigned depots
    for robot in output['robots']:
        depot = robot['tour'][0]
        if robot['tour'][-1] != depot:
            return "FAIL"

    # Requirement 2: Each city visited exactly once
    all_visited = [city for robot in output['robots'] for city in robot['tour'][1:-1]]
    if len(all_visited) != len(set(all_visited)):
        return "FAIL"
    
    # Additional check to ensure all cities are visited
    required_cities = set(range(16))
    visited_cities = set(all_visited) | set(robot['tour'][0] for robot in output['robots'])
    if visited_cities != required_cities:
        return "FAIL"

    # Requirement 5: Correct calculation of costs
    overall_calculated_cost = 0
    for robot in output['robots']:
        tour = robot['tour']
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        overall_calculated_cost += cost
        if not math.isclose(cost, robot['cost'], rel_tol=1e-2):
            return "FAIL"

    # Requirement 5: Overall cost
    if not math.isclose(overall_calculated_cost, output['overall_cost'], rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Run the test
test_result = test_solution(output)
print(test_result)