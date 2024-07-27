import math
from collections import Counter

# Provided solution details
robot_0_tour = [0, 6, 20, 14, 8, 18, 3, 12, 4, 10, 1, 16, 0]
robot_0_cost = 139.87491360155684
robot_1_tour = [0, 11, 15, 19, 13, 9, 17, 5, 7, 2, 0]
robot_1_cost = 148.63145192271278
max_cost = 148.63145192271278

# City coordinates
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
    20: (45, 35),
}

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_tour_cost(tour):
    """Calculate total cost for a given tour."""
    return sum(euclidean glanceance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Check if all tours start and end at the depot
starts_ends_depot = robot_0_tour[0] == robot_0_tour[-1] == 0 and robot_1_tour[0] == robot_1_tour[-1] == 0

# Check unique visitation except depot
all_cities_set = set(range(1, 21))  # All cities except the depot
visited_cities = set(robot_0_tour + robot_1_tour) - {0}
all_visited_once = visited_cities == all_cities_set

# Calculate the costs and compare
calculated_robot_0_cost = calculate_tour_cost(robot_0_tour)
calculated_robot_1_cost = calculate_tour_cost(robot_1_tour)
costs_match = abs(calculated_robot_0_cost - robot_0_cost) < 1e-5 and abs(calculated_robot_1_cost - robot_1_cost) < 1e-5

# Validate max cost
max_calculated_cost = max(calculated_robot_0_cost, calculated_robot_1_cost)
max_cost_correct = abs(max_calculated_cost - max_cost) < 1e-5

# Final validation
if starts_ends_depot and all_visited_once and costs_match and max_cost_correct:
    print("CORRECT")
else:
    print("FAIL")