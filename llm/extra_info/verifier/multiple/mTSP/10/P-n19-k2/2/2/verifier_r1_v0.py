import math
from itertools import chain

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def verify_tours():
    robot_0_tour = [0, 1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 0]
    robot_1_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 0]
    robot_0_cost_computed = sum(calculate_distance(cities[robot_0_tour[i]], cities[robot_0_tour[i + 1]]) for i in range(len(robot_0_tour) - 1))
    robot_1_cost_computed = sum(calculate_distance(cities[robot_1_tour[i]], cities[robot_1_tour[i + 1]]) for i in range(len(robot_1_tour) - 1))
    
    if abs(robot_0_cost_computed - 143.98) > 0.01 or abs(robot_1_cost_computed - 97.31) > 0.01:
        return "FAIL"

    all_visited_cities = list(chain(robot_0_tour[1:-1], robot_1_tour[1:-1]))
    unique_cities = set(all_visited_cities)
    
    if len(unique_cities) != 18 or any(city == 0 for city in all_visited_cities):
        return "FAIL"

    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0 or robot_1_tour[0] != 0 or robot_1_tour[-1] != 0:
        return "FAIL"
    
    return "CORRECT"

print(verify_tours())