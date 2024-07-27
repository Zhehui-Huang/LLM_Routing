import numpy as np
from math import sqrt

# Data initialization
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Solution provided
robots_tours = [
    [0, 2, 0, 13, 0],
    [0, 3, 0],
    [0, 8, 6, 15, 12, 22, 17, 0],
    [0, 20, 4, 5, 0],
    [0, 7, 0],
    [0, 1, 10, 16, 0],
    [0, 19, 21, 0]
]
robots_costs = [100.28847119750142, 65.11528238439882, 160.76819705379563, 105.1170212934997,
                44.04543109109048, 42.6682117120349, 89.30714247072336]
overall_cost_reported = 607.3097572030445

# Methods
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tours_and_costs():
    visited = set()
    overall_calculated_cost = 0
    for robot, tour in enumerate(robots_tours):
        start_city = tour[0]
        end_city = tour[-1]
        
        # Check if tours start and end at the same city (depot)
        if start_city != end_city:
            return "FAIL"
        
        # Check all cities are visited exactly once
        for city in tour:
            if city in visited and city != start_city:
                return "FAIL"
            visited.add(city)

        # Check costs
        tour_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour)-1))
        if not np.isclose(tour_cost, robots_costs[robot]):
            return "FAIL"
        
        overall_calculated_cost += tour_cost

    # Validate total count of cities visited
    if len(visited) != len(cities):
        return "FAIL"

    # Check if the reported overall cost is close to calculated overall cost
    if not np.isclose(overall_calculated_cost, overall_cost_reported):
        return "FAIL"

    return "CORRECT"

# Execute tests
result = verify_tours_and_costs()
print(result)