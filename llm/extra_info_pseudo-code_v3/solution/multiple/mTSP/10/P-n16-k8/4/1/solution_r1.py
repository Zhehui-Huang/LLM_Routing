import numpy as np
from itertools import permutations
from math import sqrt

# Calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Generating initial solution using the Greedy Nearest Neighbor algorithm
def nearest_neighbor_tour(start_index, distance_matrix, unvisited):
    tour = [start_start_index]
    while unvisited:
        next_index = min(unvisited, key=lambda x: distance_matrix[tour[-1]][x])
        unvisited.remove(next_index)
        tour.append(next_index)
    tour.append(start_start_index)  # Return to depot
    return tour

# Function to generate the distance matrix
def generate_distance_matrix(cities):
    num_cities = len(cities)
    matrix = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                matrix[i][j] = euclidean_distance(cities[i], cities[j])
            else:
                matrix[i][j] = float('inf')
    return matrix

# Initializing city coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Create distance matrix
distance_matrix = generate_distance_matrix(cities)

# Number of robots
num_robots = 8

# Calculate tours splitting the locations equally among the robots
nodes_per_robot = (len(cities) - 1) // num_robots
remaining_nodes = (len(cities) - 1) % num_robots

tours = []
start_node = 0
nodes_visited = 0

for r in range(num_robots):
    if nodes_visited < len(cities) - 1:
        range_end = nodes_per_robot + (1 if remaining_nodes > 0 else 0)
        remaining_nodes -= 1
        tour_nodes = list(range(1, len(cities)))[nodes_visited:nodes_visited + range_end]
        nodes_visited += range_end
        tours.append(nearest_neighbor_tour(0, distance_matrix, set(tour_nodes)))

# Calculate and print the travel cost
overall_total_cost = 0
for i, tour in enumerate(tours):
    cost = sum(distance_matrix[tour[j]][tour[j + 1]] for j in range(len(tour) - 1))
    overall_total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {round(cost, 2)}")

print(f"Overall Total Travel Cost: {round(overall_total_cost, 2)}")