import math
from collections import defaultdict

# Robot tours from the given solution
robot_tours = [
    [0, 21, 16, 1, 10, 13, 0],
    [0, 6, 20, 19, 0],
    [0, 2, 22, 0],
    [0, 4, 11, 9, 0],
    [0, 7, 5, 12, 0],
    [0, 15, 3, 0],
    [0, 14, 18, 0],
    [0, 17, 0]
]

# Demand list (index corresponds to city number)
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Coordinates (index corresponds to city number)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Capacity of each robot
robot_capacity = 40

def check_start_end_at_depot(tours):
    return all(tour[0] == 0 and tour[-1] == 0 for tour in tours)

def check_visit_once(tours, num_cities):
    city_visit_count = [0] * num_cities
    for tour in tours:
        for city in tour[1:-1]:  # exclude depot existence at start/end
            city_visit_count[city] += 1
    return all(count == 1 for count in city_visit_count[1:])  # exclude depot

def check_capacity_constraints(tours, demands):
    for tour in tours:
        total_demand = sum(demands[city] for city in tour[1:-1])  # exclude depot
        if total_demand > robot_capacity:
            return False
    return True

def check_unique_operation(tours):
    used = set()
    for tour in tours:
        for i in range(len(tour)-1):
            if (tour[i], tour[i+1]) in used:
                return False
            used.add((tour[i], tour[i+1]))
    return True

def check_requirement():
    num_cities = len(coordinates)
    
    if not check_start_end_at_depot(robot_tours):
        return "FAIL"
    
    if not check_visit_once(robot_tours, num_cities):
        return "FAIL"
    
    if not check_capacity_constraints(robot_tours, demands):
        return "FAIL"
    
    if not check_unique_operation(robot_tours):
        return "FAIL"

    return "CORRECT"

# Run the unit test function
result = check_requirement()
print(result)