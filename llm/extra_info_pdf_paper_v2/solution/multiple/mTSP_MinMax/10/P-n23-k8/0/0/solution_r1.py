import math
import numpy as np

# City coordinates with city index as key
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
    21: (32, 39),
    22: (56, 37),
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Number of robots
num_robots = 8

# Generate initial simple routes
def initial_solution():
    non_depot_cities = list(cities.keys())[1:]  # Skip depot (0)
    per_robot = len(non_depot_cities) // num_robots
    return [non_depot_cities[i * per_robot:(i + 1) * per_robot] for i in range(num_robots)]

def tour_cost(tour):
    cost = calculate_distance(0, tour[0]) + calculate_distance(tour[-1], 0)
    cost += sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return cost

robot_tours = initial_solution()
max_travel_cost = 0

for idx, tour in enumerate(robot_tours):
    tour_full = [0] + tour + [0]
    cost = tour_cost(tour)
    max_travel_cost = max(max_travel_cost, cost)
    print(f"Robot {idx} Tour: {tour_full}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print("Maximum Travel Cost:", max_travel_cost)