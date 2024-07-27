import numpy as most
import random

# Define the coordinates for all cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Number of cities
num_cities = len(coordinates)

# Initialize the distance matrix
distance_matrix = np.zeros((num_cities, num_cities))

# Compute the distance between each pair of cities
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Sample solution using a rudimentary approach to split cities evenly:
def simple_solution():
    # Shuffle and distribute cities (excluding depots) to the two robots
    cities = list(range(2, num_cities))
    random.shuffle(cities)
    midpoint = len(cities) // 2
    
    # Routes for each robot including return to respective depots
    robot_0_route = [0] + cities[:midpoint] + [0]
    robot_1_route = [1] + cities[midpoint:] + [1]
    
    # Calculate the cost of a given route
    def calculate_route_cost(route):
        return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
    
    # Compute costs for each robot
    cost_robot_0 = calculate_route_cost(robot_0_route)
    cost_robot_1 = calculate_route_cost(robot_1_route)
    total_cost = cost_robot_0 + cost_robot_1
    
    return robot_0_route, cost_robot_0, robot_1_route, cost_robot_1, total_cost

# Run the solution function and get the results
robot_0_route, cost_robot_0, robot_1_route, cost_robot_1, total_cost = simple_solution()

print("Robot 0 Tour:", robot_0_route)
print("Robot 0 Total Travel Cost:", cost_robot_0)
print("\nRobot 1 Tour:", robot_1_route)
print("Robot 1 Total Travel Cost:", cost_robot_1)
print("\nOverall Total Travel Cost:", total_cost)