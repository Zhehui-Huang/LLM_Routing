import math

# Define the coordinates and demands of each city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot tours and their reported costs
robot_tours = [
    ([0, 18, 19, 16, 21, 0], 51.51),
    ([0, 9, 17, 0], 40.84),
    ([0, 12, 15, 1, 0], 37.22),
    ([0, 8, 13, 0], 39.17),
    ([0, 14, 22, 0], 36.37),
    ([0, 4, 11, 0], 35.37),
    ([0, 3, 10, 20, 0], 50.22),
    ([0, 5, 7, 0], 30.02)
]

# Calculate the Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Check if all tours start and end at the depot
def check_start_end_at_depot(robot_tours):
    return all(tour[0] == 0 and tour[-1] == 0 for tour, _ in robot_tours)

# Check that each city's demand is met exactly once
def check_demands_met(robot_tours):
    supplied = [0] * len(coordinates)
    for tour, _ in robot_tours:
        for city in tour:
            supplied[city] += 1
    supplied[0] = 0  # ignore depot visits beyond the expected
    return all(supplied[i] == 1 for i in range(1, len(demands)))

# Check if any robot exceeds its carrying capacity
def check_capacity_constraints(robot_tours):
    robot_capacity = 40
    for tour, _ in robot_tours:
        if sum(demands[city] for city in tour) > robot_capacity:
            return False
    return True

# Validate and calculate total travel cost
def check_total_travel_cost(robot_tours, expected_total_cost):
    total_calculated_cost = 0
    for tour, reported_cost in robot_tours:
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if not math.isclose(cost, reported_cost, abs_tol=0.1):
            return False
        total_calculated_cost += reported_cost
    return math.isclose(total_calculated_cost, expected_total_cost, abs_tol=0.1)

# Unit tests to check the provided tours
def run_checks(robot_tours, expected_total_cost):
    if not check_start_end_at_depot(robot_tours):
        return "FAIL: Starting or ending point check failed."
    
    if not check_demands_met(robot_tours):
        return "FAIL: Demand met check failed."
    
    if not check_capacity_constraints(robot_tours):
        return "FAIL: Capacity constraint failed."
    
    if not check_total_travel cost(robot_tours, expected_total_cost):
        return "FAIL: Total cost calculation mismatch."

    return "CORRECT"

# Run the checks with the given tours and their reported total cost
result = run_checks(robot_tour, 320.72)
print_result