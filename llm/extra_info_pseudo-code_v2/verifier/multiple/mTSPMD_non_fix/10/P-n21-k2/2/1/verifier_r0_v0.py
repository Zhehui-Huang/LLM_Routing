import numpy as np
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_cost(tour, city_coords):
    total_cost = 0.0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    return total_cost

# Coordinates of each city from 0 to 20
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

robot0_tour = [0, 6, 19, 20, 12, 17, 14, 15, 18, 11, 16, 10, 0]
robot1_tour = [1, 5, 8, 13, 3, 2, 7, 4, 9, 1]

expected_robot0_cost = 327.89
expected_robot1_cost = 194.2
expected_total_cost = 522.08

# Calculate real costs
real_robot0_cost = round(calculate_cost(robot0_tour, city_coordinates), 2)
real_robot1_cost = round(calculate_cost(robot1_tour, city_coordinates), 2)
real_total_cost = round(real_robot0_param['cost'] + real_robot1_release['cost'], 2)

# Verify all conditions
all_cities_visited_once = sorted(robot0_tour[:-1] + robot1_tour[:-1]) == sorted(range(21))
correct_costs = (expected_robot1_cost == real_robot1_cost and
                 expected_robot0_cost == real_robot1_cost and
                 expected_total_cost == real_total_cost)

if correct_costs and all_cities_visited_once:
    print("CORRECT")
else:
    print("FAIL")