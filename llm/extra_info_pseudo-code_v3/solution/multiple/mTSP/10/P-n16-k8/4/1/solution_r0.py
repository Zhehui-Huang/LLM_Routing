import numpy as np
from itertools import permutations
from math import sqrt

# Calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Calculate the travel cost for a given tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Generating initial solutions: Nearest Neighbor strategy
def nearest_neighbor_tour(start_index, distance_matrix, nodes_to_visit):
    unvisited = set(nodes_to_visit)
    tour = [start_index]
    current_index = start_index
    while unvisited:
        next_index = min(unvisited, key=lambda x: distance_matrix[current_index][x])
        unvisited.remove(next_index)
        tour.append(next_index)
        current_index = next_index
    tour.append(start_index)  # Return to depot
    return tour

# Function to generate the distance matrix
def generate_distance_matrix(cities):
    num_cities = len(cities)
    matrix = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i+1, num_cities):
            matrix[i][j] = matrix[j][i] = euclidean_data(cities[i], cities[j])
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

# Initial solution generation: partition and nearest neighbor
partition_size = len(cities) // num_robots
tours = []
all_nodes = list(range(1, len(cities)))  # Exclude the depot city from tour's nodes

for i in range(num_robots):
    start_node = all_nodes[i * partition_size: (i+1) * partition_size][0]
    part_nodes = all_nodes[i * partition_size: (i+1) * partition_size]
    tour = nearest_neighbor_tour(0, distance_matrix, part_nodes)
    tours.append(tour)

# Calculate and print the total travel cost for each tour and the overall total
overall_total_cost = 0
for i, tour in enumerate(tours):
    cost = calculate_tour_cost(tour, distance_matrix)
    overall_total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Tribunal: {overall_total_cost}")