import numpy as np
from math import sqrt

# Cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8,
    8, 7, 14, 6, 19, 11, 12, 26, 17, 6,
    15, 5, 10
]

# Robot settings
num_robots = 8
capacity = 40
depot = 0

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Initialize variables to manage tours
tours = [[] for _ in range(num_robots)]
current_loads = [0] * num_robots
current_locations = [depot] * num_robots
unvisited = set(range(1, num_cities))  # Exclude the depot

# Implementation of a simplified greedy heuristic
while unvisited:
    for robot in range(num_robots):
        if not unvisited:
            break

        current_city = current_locations[robot]
        next_city = None
        min_distance = float('inf')

        for city in unvisited:
            if distance_matrix[current_city][city] < min_distance and current_loads[robot] + demands[city] <= capacity:
                next_city = city
                min_distance = distance_matrix[current_city][city]

        if next_city is not None:
            tours[robot].append(next_city)
            current_loads[robot] += demands[next_city]
            current_locations[robot] = next_city
            unvisited.remove(next_city)

# Ensure all robots return to the depot
total_cost = 0

for robot in range(num_robots):
    if tours[robot]:
        tours[robot].insert(0, depot)
        tours[robot].append(depot)
        tour_cost = sum(distance_matrix[tours[robot][i]][tours[robot][i + 1]] for i in range(len(tours[robot]) - 1))
        print(f"Robot {robot} Tour: {tours[robot]}")
        print(f"Robot {robot} Total Travel Cost: {tour_cost:.2f}")
        total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost:.2f}")