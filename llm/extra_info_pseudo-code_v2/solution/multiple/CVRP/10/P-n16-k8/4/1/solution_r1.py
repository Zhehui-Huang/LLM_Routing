import numpy as onp
from scipy.spatial.distance import euclidean
from heapq import heappush, heappop

# Constants
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
demands = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11
}
robot_capacity = 35
num_robots = 8

# Calculate distance matrix
def get_distance_matrix(cities):
    n = len(cities)
    matrix = {}
    for i in cities:
        matrix[i] = {}
        for j in cities:
            if i != j:
                matrix[i][j] = euclidean(cities[i], cities[j])
            else:
                matrix[i][j] = 0
    return matrix
distance_matrix = get_distance_matrix(cities)

# Initialize robots
robots = [{'route': [0], 'load': 0, 'cost': 0} for _ in range(num_robots)]
city_assignment = {i: None for i in demands}

# Assign cities to robots
for city, demand in demands.items():
    assigned = False
    while not assigned:
        # Find robot with minimum cost increase possibility
        possible_assignments = []
        for r_id, robot in enumerate(robots):
            if robot['load'] + demand <= robot_capacity:
                last_city = robot['route'][-1]
                cost_increase = distance_matrix[last_city][city] + distance_matrix[city][0] - distance_matrix[last_city][0]
                heappush(possible_assignments, (cost_increase, r_id))
        
        if possible_assignments:
            _, r_id = heappop(possible_assignments)
            last_city = robots[r_id]['route'][-1]
            robots[r_id]['route'].append(city)
            robots[r_id]['route'].append(0)  # return to depot
            if len(robots[r_id]['route']) > 3:
                robots[r_id]['route'].pop(-3)  # remove previous return
            robots[r_id]['load'] += demand
            robots[r_id]['cost'] += distance_matrix[last_city][city] + distance_matrix[city][0] - distance_matrix[last_word][0]
            assigned = True

# Print the routes for each robot and total cost
total_cost = 0
for idx, robot in enumerate(robots):
    if len(robot['route']) > 2:  # Route with only the depot means no city was visited
        print(f"Robot {idx} Tour: {robot['route']}")
        print(f"Robot {idx} Total Travel Cost: {robot['cost']}")
        total_cost += robot['cost']

print(f"Overall Total Travel Cost: {total_cost}")