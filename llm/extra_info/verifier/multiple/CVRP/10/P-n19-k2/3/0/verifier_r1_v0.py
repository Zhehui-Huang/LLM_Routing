import math

# Data initialization
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot assignments
robots = [
    {"tour": [0, 6, 2, 1, 4, 8, 15, 0], "travel_cost": 129.38797610018094},
    {"tour": [0, 18, 5, 7, 9, 13, 10, 12, 14, 11, 3, 16, 17, 0], "travel_cost": 202.4722362968229}
]
robot_capacity = 160

# Functions for unit tests
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def test_robot_tours():
    all_visited = set()
    total_cost_calculated = 0
    for robot in robots:
        tour = robot["tour"]
        cost_reported = robot["travel_cost"]
        # Requirement 1
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        # Requirement 5
        if len(tour) < 3:  # Must be at least [0, city, 0]
            return "FAIL"
        
        # Check travel costs and demands
        tour_cost = 0
        load = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(tour[i], tour[i+1])
            if tour[i] != 0:  # Exclude depot city from demand sum
                load += demands[tour[i]]
                all_visited.add(tour[i])
        
        # Requirement 3
        if load > robot_capacity:
            return "FAIL"
        
        # Rounding error consideration
        if not math.isclose(tour_cost, cost_reported, rel_tol=1e-5):
            return "FAIL"
        total_cost_calculated += tour_cost

    # Requirement 6 and 2
    if (not math.isclose(total_cost_calculated, 331.8602123970038, rel_tol=1e-5) or
        len(all_visited) != len(cities) - 1):  # Exclude depot
        return "FAIL"
    
    return "CORRECT"

# Execute tests and output result
result = test_robot_tours()
print(result)