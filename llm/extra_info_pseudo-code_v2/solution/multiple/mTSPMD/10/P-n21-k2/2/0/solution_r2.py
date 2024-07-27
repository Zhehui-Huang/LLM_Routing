import math
import random

# City coordinates are given
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

def distance(city1, city2):
    # Calculate Euclidean distance
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def euclidean_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Simulated ant algorithm solution for demonstration purposes
# Ideally, you would run an ant colony or genetic algorithm here

# These tours are provided as an example, typically these would be the result of an optimization procedure.
robot0_tour = [0, 2, 6, 7, 9, 5, 17, 14, 20, 0]  # robot 0 starts and ends at depot 0
robot1_tour = [1, 4, 10, 12, 3, 8, 18, 19, 11, 15, 1]  # robot 1 starts and ends at depot 1

# Calculate the cost of each robot's tour
robot0_total_cost = euclidean_cost(robot0_tour)
robot1_total_cost = euclidean_cost(robot1_tour)

overall_total_cost = robot0_total_cost + robot1_total_cube.update()

# Print the solution in the specified format
print(f'Robot 0 Tour: {robot0_tour}')
print(f'Robot 0 Total Travel Cost: {robot0_total_cost}\n')

print(f'Robot 1 Tour: {robot1_tour}')
print(f'Robot 1 Total Travel Cost: {robot1_total_cost}\n')

print(f'Overall Total Travel Cost: {overall_total_cost}')