import math
import random

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Robot (vehicle) information
num_robots = 8
robot_capacity = 35

# Euclidean distance calculator
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Greedy solution builder
def build_initial_solution():
    routes = [[] for _ in range(num_robots)]
    capacity_remaining = [robot_capacity for _ in range(num_robots)]
    city_visited = [False] * len(coordinates)
    city_visited[0] = True  # Depot is always considered visited
    for robot in range(num_robots):
        current_city = 0
        while True:
            next_city = None
            min_distance = float('inf')
            for city in range(1, len(coordinates)):  # start from 1 to skip the depot
                if not city_visited[city] and demands[city] <= capacity_remaining[robot]:
                    if distance_matrix[current_city][city] < min_distance:
                        min_distance = distance_matrix[current_city][city]
                        next_city = city
            if nextinations as specified in your requirements.