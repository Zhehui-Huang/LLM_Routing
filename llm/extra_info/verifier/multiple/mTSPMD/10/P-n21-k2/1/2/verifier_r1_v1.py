import math

# Define city coordinates
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

# Tours provided
robot_0_tour = [0, 16, 6, 7, 2, 10, 12, 15, 4, 11, 3, 8, 0]
robot_1_tour = [1, 20, 5, 14, 17, 9, 13, 18, 19, 1]

# Calculate travel cost using Euclidean distance
def calculate_travel_cost(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        total_distance += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total_distance

# Calculate and assert the travel costs
robot_0_cost_calculated = calculate_travel_cost(robot_0_tour, cities)
robot_1_cost_calculated = calculate_travel_cost(robot_1_tour, cities)

# Verify travel costs
def verify_costs():
    if not (math.isclose(robot_0_cost_calculated, 143.96) and math.isclose(robot_1_cost_calculated, 110.20)):
        return "FAIL"
    return "PASS"

# Check for starting and ending at assigned depots
def check_depots():
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0 or robot_1_tour[0] != 1 or robot_1_tour[-1] != 1:
        return "FAIL"
    return "PASS"

# Check each city is visited exactly once
def check_all_cities_visited():
    all_cities = set(range(21))
    visited_cities = set(robot_0_tour[:-1] + robot_1_tour[:-1])
    if visited_cities != all_cities:
        return "FAIL"
    return "PASS"

# Check the solution
def check_solution():
    if verify_costs() == "FAIL" or check_depots() == "FAIL" or check_all_cities_visited() == "FAIL":
        return "FAIL"
    else:
        return "CORRECT"

# Output the result
print(check_solution())