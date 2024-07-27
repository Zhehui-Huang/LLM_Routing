import numpy as np
from scipy.spatial import distance

# City Coordinates and Demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Initialize distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = distance.euclidean(coordinates[i], coordinates[j])

# Robot info
num_robots = 2
capacity = 160

# Initialize tours (start and end at the depot)
tours = [[0] for _ in range(num_robots)]
remaining_demands = demands.copy()

# Implementing a splitting algorithm to assign cities to robots with respect to the demand and robot capacity
current_robot = 0
load = 0

for city in range(1, num_cities):
    if remaining_demands[city] > 0:
        if load + remaining_demands[city] <= capacity:
            load += remaining_demands[city]
            tours[current_robot].append(city)
        else:
            if current_robot < num_robots - 1:
                tours[current_robot].append(0) # Go back to the depot
                current_robot += 1
                load = remaining_demands[city]
                tours[current_robot].append(city)
            else:
                break

# Ensure all robots return to the depot
for robot in range(num_robots):
    if tours[robot][-1] != 0:
        tours[robot].append(0)

# Calculate the total cost
total_cost = 0
output = ""
for robot, tour in enumerate(tours):
    tour_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    total_cost += tour_cost
    output += f"Robot {robot} Tour: {tour}\nRobot {robot} Total Travel Cost: {tour_cost:.2f}\n"

output += f"Overall Total if not cost: {total_cost:.2f}\n"

print(output)