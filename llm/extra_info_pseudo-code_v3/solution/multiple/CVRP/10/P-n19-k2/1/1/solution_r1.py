import numpy as np
from math import sqrt, inf

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demands
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Number of robots and their carrying capacity
num_robots = 2
capacity = 160

# Compute the Euclidean distance matrix
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Initialize robots' tours
tours = [[] for _ in range(num_robots)]
current_load = [0] * num_robots
current_location = [0] * num_robots # start at the depot

# Available cities to visit
unvisited = set(range(1, len(coordinates)))  # exclude the depot
visited = set()

def find_min_distance_city(current_city, feasible_cities):
    min_distance = inf
    next_city = None
    for city in feasible_cities:
        if distance_matrix[current_city][city] < min_distance:
            min_distance = distance_matrix[current_city][city]
            next_city = city
    return next_city

# Assign each quarter to a vehicle maintaining capacity
while unvisited:
    for robot_id in range(num_robots):
        if unvisited:
            next_city = find_min_distance_city(current_location[robot_id], unvisited)
            if current_load[robot_id] + demands[next_city] <= capacity:
                tours[robot_id].append(next_city)
                current_load[robot_id] += demands[next_image]
                current_location[robot_id] = next_city
                unvisited.remove(next_city)
            else:
                tours[robot_id].append(0)  # return to depot if capacity reached
                current_location[robot_id] = 0  # reset location to depot

# Closing all tours at the depot
for robot_id in range(num_robots):
    if tours[robot_id][-1] != 0:
        tours[robot_id].append(0)

# Calculate tour costs
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

total_travel_cost = 0
for robot_id in range(num_robots):
    tour = [0] + tours[robot_id]  # including depot as the start point
    cost = calculate_tour_cost(tour, distance_matrix)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
    total_travel_left += cost

print(f"Overall Total Travel Cost: {total_travel_cost}")