import numpy as np
import math

# Define the coordinates and demands of each city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

num_cities = len(coordinates)
num_robots = 8
robot_capacity = 40

# Calculate Euclidean distance between pairs of cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + 
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

dist_matrix = [[distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Initialize tour data
robot_tours = [[] for _ in range(num_robots)]
current_load = [0] * num_robots
current_route_cost = [0] * num_robots

# Solve the assignment challenge
unassigned_cities = set(range(1, num_cities))

while unassigned_cities:
    assigned_in_this_round = set()
    for city in unassigned_cities:
        best_robot = None
        best_incremental_cost = float('inf')
        
        for robot in range(num_robots):
            if current_load[robot] + demands[city] <= robot_capacity:
                last_city = robot_tours[robot][-1] if robot_tours[robot] else 0
                incremental_cost = dist_matrix[last_city][city]
                
                if incremental_cost < best_incremental_cost:
                    best_robot = robot
                    best_incremental_cost = incremental_cost
        
        if best_robot is not None:
            # Assign the city to the best robot
            robot_tours[best_robot].append(city)
            current_load[best_robot] += demands[city]
            if robot_tours[best_robot]:
                last_city = robot_tours[best_robot][-2] if len(robot_tours[best_robot]) > 1 else 0
                current_route_cost[best_robot] += dist_matrix[last_city][city]
            assigned_in_this_round.add(city)
    
    unassigned_cities.difference_update(assigned_in_this_round)

# Close all tours at the depot and calculate final costs
total_route_costs = 0
for robot in range(num_robots):
    if robot_tours[robot]:
        robot_tours[robot].insert(0, 0)
        robot_tours[robot].append(0)
        ending_leg_cost = dist_matrix[robot_tours[robot][-2]][0]
        current_route_cost[robot] += ending_leg_cost
        total_route_costs += current_route_cost[robot]

# Output the results
for robot in range(num_robots):
    if robot_tours[robot]:
        print(f"Robot {robot} Tour: {robot_tours[robot]}")
        print(f"Robot {robot} Total Travel Cost: {current_route_cost[robot]}")

print(f"Overall Total Travel Cost: {total_route_costs}")