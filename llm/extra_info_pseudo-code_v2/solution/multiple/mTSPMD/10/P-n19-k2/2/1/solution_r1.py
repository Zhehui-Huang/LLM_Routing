import numpy as np
import math
from itertools import permutations

# City Coordinates and depots
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
depots = [0, 1]  # Depots corresponding to robot 0 and robot 1
num_robots = 2

# Calculate distance matrix
def calculate_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)
            dist_matrix[i][j] = dist_matrix[j][i] = dist
    return dist_matrix

distance_matrix = calculate_distance_matrix(coordinates)

# Use a basic method (e.g., nearest neighbor per robot) for initial feasible solution
def nearest_neighbor_tour(start_index, remaining):
    tour = [start_index]
    while remaining:
        nearest = min(remaining, key=lambda x: distance_matrix[tour[-1]][x])
        tour.append(nearest)
        remaining.remove(nearest)
    tour.append(start_index)  # return to starting depot
    return tour

# Initialize the tours
cities = set(range(len(coordinates)))
remaining_cities = cities - set(depots)
tours = [nearest_neighbor_tour(depots[i], list(remaining_cities)) for i in range(num_robots)]

# Calculate travel cost for a given tour
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Calculate total cost and print results
total_cost = 0

for i in range(len(tours)):
    tour_cost = calculate_tour_cost(tours[i])
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")