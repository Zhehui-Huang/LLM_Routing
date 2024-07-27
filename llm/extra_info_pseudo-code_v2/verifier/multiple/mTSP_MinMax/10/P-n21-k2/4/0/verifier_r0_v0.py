import numpy as np

# Given cities and their coordinates
cities = {
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

# Solution provided
robot_tours = {
    0: [0, int(np.int64(16)), 0],
    1: [0, int(np.int64(6)), 0]
}
robot_costs = {
    0: 20.0,
    1: 24.08318915758459
}
max_cost = 24.08318915758459

def calculate_distance(c1, c2):
    """Euclidean distance between two cities based on their coordinates."""
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution():
    # Verify all cities except depot are visited exactly once
    all_visited_cities = set()
    for tour in robot_tours.values():
        for city in tour:
            if city != 0:
                if city in all_visited_cities:
                    return "FAIL"
                all_visited_cities.add(city)
    
    if len(all_visited_cities) != 20:  # 21 cities including depot, so 20 except depot
        return "FAIL"
    
    # Verify start and end at depot, calculate costs and check with given costs
    for robot, tour in robot_tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        calculated_cost = 0
        for i in range(len(tour)-1):
            calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        
        if not np.isclose(calculated_cost, robot_costs[robot]):
            return "FAIL"
    
    # Check maximum cost
    calculated_max_cost = max(robot_costs.values())
    if not np.isclose(calculated_max_cost, max_cost):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Run the verification
print(verify_solution())