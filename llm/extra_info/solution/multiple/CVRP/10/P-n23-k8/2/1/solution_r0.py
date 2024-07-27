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

# Calculate Euclidean distance between each pair of cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + 
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

dist_matrix = [[distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Initialize tour data structure
robot_tours = [[] for _ in range(num_robots)]
current_load = [0] * num_robots
current_city = [0] * num_robots  # All start at the depot

# Assign cities to robots
unassigned_cities = set(range(1, num_cities))  # Exclude the depot

while unassigned_cities:
    for robot in range(num_robots):
        nearest_city = None
        min_distance = float('inf')
        
        # Find the nearest unassigned city that meets the capacity constraint
        for city in unassigned_cities:
            if current_load[robot] + demands[city] <= robot_capacity and dist_matrix[current_city[robot]][city] < min_distance:
                nearest_city = city
                min_distance = dist_matrix[current_city[robot]][city]
        
        if nearest_city is not None:
            # Assign city to the robot
            robot_tours[robot].append(nearest_city)
            current_load[robot] += demands[nearest_city]
            current_city[robot] = nearest_city
            unassigned_cities.remove(nearest_city)

# Return each robot to the depot and calculate the travel costs
robot_costs = []
for robot in range(num_robots):
    if robot_tours[robot]:  # If the robot has visited any cities
        robot_tours[robot].insert(0, 0)  # Start at the depot
        robot_tours[robot].append(0)  # Return to the depot
        # Calculate travel cost
        tour_cost = sum(dist_matrix[robot_tours[robot][i]][robot_tours[robot][i+1]] 
                        for i in range(len(robot_tours[robot])-1))
        robot_costs.append(tour_cost)
    else:
        robot_costs.append(0)

# Output the results
overall_cost = sum(robot_costs)
for robot, tour in enumerate(robot_tours):
    if tour:
        print(f"Robot {robot} Tour: {tour}")
        print(f"Robot {robot} Total Travel Core: {robot_costs[robot]}")

print(f"Overall Total Travel Cost: {overall_receive}")