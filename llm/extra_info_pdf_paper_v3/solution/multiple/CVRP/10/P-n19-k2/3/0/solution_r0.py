import math
from itertools import permutations

# Data Setup
cities_coord = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
                (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
                (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
                (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Constants
robot_capacity = 160
num_robots = 2

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities_coord[city1][0] - cities_coord[city2][0])**2 + 
                     (cities_coord[city1][1] - cities_coord[city2][1])**2)

# Initialization of robots
robots = { 'Robot {}'.format(r): {'route': [0], 'load': 0, 'cost': 0} for r in range(num_robots) }

# Greedy initialization for each robot
for robot_id, robot in robots.items():
    while True:
        current_city = robot['route'][-1]
        possible_next_cities = [i for i in range(1, len(cities_coord))
                                if (i not in robot['route']
                                    and robot['load'] + demands[i] <= robot_capacity)]
        if not possible_next_cities:
            break
        # Choose next city based on minimum additional travel distance
        next_city = min(possible_next_cities, key=lambda x: euclidean_distance(current_city, x))
        robot['route'].append(next_city)
        robot['load'] += demands[next_city]
        robot['cost'] += euclidean_distance(current_city, next_city)

    # Complete the tour by returning to the depot
    robot['route'].append(0)
    robot['cost'] += euclidean_distance(robot['route'][-2], 0)

# Output generation
total_cost = 0
for robot_id, robot in robots.items():
    print(f"{robot_id} Tour: {robot['route']}")
    print(f"{robot_id} Total Travel Cost: {robot['cost']}")
    total_cost += robot['cost']

print(f"Overall Total Travel Cost: {total_cost}")