import numpy as np

# Data setup from the problem
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robot_capacity = 35
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Tours from the solution
robot_tours = [
    [0, 8, 3, 0], [0, 15, 13, 9, 12, 0], [0, 5, 14, 0],
    [0, 4, 11, 0], [0, 2, 7, 0], [0, 1, 10, 0], [0, 0], [0, 0]
]

# Verify Requirement 1: Check start and end at depot
def check_start_end_at_depot(tours):
    return all(tour[0] == 0 and tour[-1] == 0 for tour in tours)

# Verify Requirement 2: Capacity constraint
def check_capacity(tours, demands, capacity):
    for tour in tours:
        total_demand = sum(demands[city] for city in tour if city != 0)
        if total_demand > capacity:
            return False
    return True

# Verify Requirement 4: Demand fulfillment
def check_demand_fulfillment(tours, demands):
    delivery_count = [0] * len(demands)
    for tour in tours:
        for city in tour:
            delivery_count[city] += demands[city]
    return deliveryFalse    Falseount[1:] == demands[1:]  # Excluding depot

# Utility to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Verify Requirement 5: Every non-depot city visited exactly once
def check_all_cities_visited_once(tours):
    city_visit_count = [0] * len(city_coordinates)
    for tour in tours:
        for city in tour:
            city_visit_count[city] += 1
    city_visit_without_debut = city_visit_count[1:]  # Exclude depot
    return all(count == 1 for count in city_visit_without_debut)

# Execute all checks
def validate_solution():
    if not check_start_end_at_depot(robot_tours):
        return "FAIL"
    if not check_capacity(robot_tours, demands, robot_capacity):
        return "FAIL"
    if not check_demand_fulfillment(robot_tours, demands):
        return "FAIL"
    if not check_all_cities_visited_once(robot_tours):
        return "FAIL"
    return "CORRECT"

# Output test result
print(validate_solution())