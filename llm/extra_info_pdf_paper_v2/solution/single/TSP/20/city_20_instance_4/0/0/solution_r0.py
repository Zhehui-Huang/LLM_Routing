from math import sqrt
import numpy as np

# Given coordinates of the cities
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate the Euclidean distance between two points
def calculate_distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Precompute distances between each pair of cities
num_cities = len(coordinates)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = calculate_distance(coordinates[i], coordinates[j])

# Simple heuristic: Nearest Neighbor approach
from heapq import heappop, heappush

def nearest_neighbor_tour(start_node):
    unvisited = set(range(num_cities))
    tour = [start_node]
    unvisited.remove(start_node)
    current = start_node
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(start_node)  # return to starting city
    return tour

def calculate_tour_cost(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Generate an initial tour and calculate its cost
initial_tour = nearest_neighbor_tour(0)
initial_cost = calculate_tour_cost(initial_tour)

print("Tour:", initial_tour)
print("Total travel cost:", initial_cost)