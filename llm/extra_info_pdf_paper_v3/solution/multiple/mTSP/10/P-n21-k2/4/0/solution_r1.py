import numpy as np
from math import sqrt

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Distance calculation function
def calculate_distance_matrix(coords):
    num_points = len(coords)
    matrix = np.zeros((num_points, num_points))
    for i in range(num_points):
        for j in range(num_points):
            matrix[i][j] = sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
    return matrix

# Calculate distance matrix
distance_matrix = calculate_distance_matrix(coordinates)

# Assign cities to robots in a simple round-robin fashion
num_robots = 2
robots_cities = {i: [] for i in range(num_robots)}
for i in range(1, len(coordinates)):  # Exclude depot city (index 0)
    robots_cities[i % num_robots].append(i)

# Tour finding function for each robot
def find_tour(robot_cities, distance_matrix):
    tour = [0]  # Start at the depot
    current_city = 0
    total_travel_cost = 0
    
    while robot_cities:
        # Find closest city not yet visited
        next_city = min(robot_cities, key=lambda x: distance_matrix[current_city][x])
        total_travel_cost += distance_matrix[current_city][next_city]
        tour.append(next_city)
        current_city = next_city
        robot_cities.remove(next_city)
    
    # Return to depot
    total_travel_cost += distance_matrix[current_city][0]
    tour.append(0)
    
    return tour, total_travel_cost

# Calculate and display the tours and costs for each robot
overall_total_cost = 0
for robot_id in range(num_robots):
    tour, cost = find_tour(robots_cities[robot_id], distance_matrix)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
    overall_total_cost += cost

print("Overall Total Travel Cost:", overall_total_cost)