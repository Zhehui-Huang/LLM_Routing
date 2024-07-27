import numpy as np
import math

# Define the coordinates for each city, including depots
city_coordinates = [
    (30, 40),  # Depot city 0
    (37, 52),  # Depot city 1
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),  # Cities 2-9
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),  # Cities 10-17
    (62, 63), (63, 69), (45, 35)  # Cities 18-20
]

# Number of cities and robots
num_cities = len(city_coordinates)
num_robots = 2
depots = [0, 1]

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0]) ** 2 + (city_coordinates[city1][1] - city_coordinates[city2][1]) ** 2)

# Initialize distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = calc_distance(i, j)

# Initialize tours and costs for each robot
tours = {robot: [depots[robot]] for robot in range(num_robots)}
total_costs = {robot: 0 for robot in range(num_robots)}

# Assign cities to each robot using a simple round-robin algorithm
assigned_cities = {robot: [] for robot in range(num_robots)}
for city in range(2, num_cities):
    assigned_cities[city % num_robots].append(city)

# Simple nearest neighbor algorithm for each robot to visit their assigned cities
for robot in range(num_robots):
    current_city = depots[robot]
    while len(assigned_cities[robot]) > 0:
        next_city = min(assigned_cities[robot], key=lambda x: distance_matrix[current_city][x])
        tours[robot].append(next_city)
        total_costs[robot] += distance_matrix[current_city][next_city]
        current_city = next_city
        assigned_cities[robot].remove(next_city)
    # Return to depot
    tours[robot].append(depots[robot])
    total_costs[robot] += distance_matrix[current_city][depots[robot]]

# Calculate the overall cost
overall_total_cost = sum(total_costs.values())

# Output the results
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]}")
print(f"Overall Total Travel Cost: {overall_total_cost}")