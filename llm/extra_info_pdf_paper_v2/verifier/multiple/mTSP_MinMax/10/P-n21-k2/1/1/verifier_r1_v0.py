import math
from collections import Counter

# Provided solution
robot_0_tour = [0, 6, 20, 14, 8, 18, 3, 12, 4, 10, 1, 16, 0]
robot_0_cost = 139.87491360155684
robot_1_tour = [0, 11, 15, 19, 13, 9, 17, 5, 7, 2, 0]
robot_1_cost = 148.63145192271278
max_cost = 148.63145192271278

# Define the coordinates of each city including the depot
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

# Function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Function to calculate total tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

# Validate each requirement

# Requirement 1: Each non-depot city visited exactly once and tours end and start at depot
all_cities_visited = robot_0_tour[1:-1] + robot_1_tour[1:-1]
city_counts = Counter(all_cities_visited)
all_cities_visited_correct = all(robot_0_tour[0] == robot_0_tour[-1] == 0 and robot_1_tour[0] == robot_1_tour[-1] == 0)
all_cities_visited_once = all(count == 1 for city, count in city_counts.items()) and len(city_counts) == 20

# Requirement 2: Minimize the maximum distance traveled by any single robot
calculated_robot_0_cost = calculate_tour_cost(robot_0_tour)
calculated_robot_1_cost = calculate_tour_cost(robot_1_tour)
costs_correct = abs(calculated_robot_0_cost - robot_0_cost) < 1e-5 and abs(calculated_robot_1_cost - robot_1_cost) < 1e-5
max_cost_correct = abs(max(calculated_robot_0_cost, calculated_robot_1_cost) - max_cost) < 1e-5

# Complete validation
if all_cities_visited_correct and all_cities_visited_once and costs_correct and max_cost_correct:
    print("CORRECT")
else:
    print("FAIL")