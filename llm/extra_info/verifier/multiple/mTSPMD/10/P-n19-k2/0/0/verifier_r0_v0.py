import math

# Helper function to calculate Euclidean distance between two cities
def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Provided cities data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69),
    18: (45, 35)
}

# Provided tour data
robot_0_tour = [0, 5, 6, 13, 18, 0]
robot_1_tour = [1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 1]
reported_distance_robot_0 = 88.23
reported_distance_robot_1 = 297.88
reported_total_distance = 386.11

# Functions to calculate the total travel cost for a given tour
def calculate_total_travel_cost(tour):
    total_cost = sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    return round(total_cost, 2)

# Unit Tests
def test_tours():
    all_cities_covered = set(robot_0_tour + robot_1_tour) == set(range(19))
    if not all_cities_covered:
        return "FAIL: Cities not covered properly"
    
    returns_to_depot = robot_0_tour[-1] == robot_0_tour[0] and robot_1_tour[-1] == robot_1_tour[0]
    if not returns_to_depot:
        return "FAIL: Robots do not return to their starting depots"

    cost_0 = calculate_total_travel_cost(robot_0_tour)
    cost_1 = calculate_total_travel_cost(robot_1_tour)
    total_cost = round(cost_0 + cost_1, 2)
    
    cost_check = (cost_0 == reported_distance_robot_0) and (cost_1 == reported_distance_robot_1) and (total_cost == reported_total_distance)
    if not cost_check:
        return "FAIL: Incorrect cost calculation"

    return "CORRECT"

# Running the test
print(test_tours())