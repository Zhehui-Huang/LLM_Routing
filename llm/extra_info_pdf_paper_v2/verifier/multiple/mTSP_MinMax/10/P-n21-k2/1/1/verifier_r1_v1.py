import math
from collections import Counter

# Given solution details
robot_0_tour = [0, 6, 20, 14, 8, 18, 3, 12, 4, 10, 1, 16, 0]
robot_0_cost = 139.87491360155684
robot_1_tour = [0, 11, 15, 19, 13, 9, 17, 5, 7, 2, 0]
robot_1_cost = 148.63145192271278
max_cost = 148.63145192271278

# City coordinates including the depot
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

# Function to compute the Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Function to calculate the cost of a tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Validation of the requirements

# Requirement 1: Tours start and end at the depot and include all cities exactly once (excluding the depot)
all_cities = set(range(1, 21))  # All cities except the depot
visited_cities = set(robot_0_tour[1:-1] + robot_1_tour[1:-1])
all_cities_visited_correct = (visited_cities == all_cities) and (robot_0_tour[0] == robot_0_tour[-1] == 0) and (robot_1_tour[0] == robot_1_tour[-1] == 0)

# Requirement 2: Minimize the maximum distance traveled by any robot
calculated_robot_0_cost = calculate_tour_cost(robot_0_tour)
calculated_robot_1_cost = calculate_tour_cost(robot_1_tour)
max_calculated_cost = max(calculated_robot_0_cost, calculated_robot_1_cost)
cost_accuracy = abs(robot_0_cost - calculated_robot_0_cost) < 1e-5 and abs(robot_1_cost - calculated_robot_1_cost) < 1e-5
max_cost_correct = abs(max_cost - max_calculated

# Output evaluation
if all_cities_visited_correct and cost_accuracy and max_cost_correct:
    print("CORRECT")
else:
    print("FAIL")