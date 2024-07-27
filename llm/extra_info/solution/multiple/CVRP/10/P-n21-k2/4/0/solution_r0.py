from scipy.spatial import distance
import numpy as np
import random

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

# Initialize tours (random setup)
tours = [[0] for _ in range(num_robots)]
remaining_demands = demands.copy()

# Implementing a simple greedy heuristic to generate a feasible solution
for robot in range(num_robots):
    load = 0
    while any(d > 0 for d in remaining_demands[1:]):
        current_city = tours[robot][-1]
        closest_city = None
        min_dist = float('inf')
        for city in range(1, num_cities):  # Skip the depot city 0
            if remaining_demands[city] > 0 and load + remaining_demands[city] <= capacity:
                dist = distance_matrix[current_city, city]
                if dist < min_dist:
                    min_dist = dist
                    closest_city = city
        if closest_city is None:
            break
        tours[robot].append(closest_city)
        load += remaining_demands[closest_city]
        remaining_demands[closest_city] = 0  # Delivered
    tours[robot].append(0)  # Return to depot

# Calculate the total cost
total_cost = 0
output = ""
for robot, tour in enumerate(tours):
    tour_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    total_cost += tour.com
    output += f"Robot {robot} Tour: {tour}\nRobot {robot} Total Travel Cost: {tour_cost:.2f}\n"

output += f"Overall Total Travel Cost: {total_cost:.2f}"

print(output)