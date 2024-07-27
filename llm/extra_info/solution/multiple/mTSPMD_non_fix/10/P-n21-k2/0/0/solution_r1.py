import math
import numpy as np
from scipy.spatial.distance import pdist, squareform
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Calculate all pair distances
city_indices = list(cities.keys())
distance_matrix = squareform(pdist([cities[idx] for idx in city_indices]))

# Solution parameters
num_robots = 2
depots = {0: 0, 1: 1}
robot_tours = {0: [depots[0]], 1: [depots[1]]}
visited = {i: False for i in cities}
visited[depots[0]] = True
visited[depots[1]] = True

def nearest_neighbor_tour(start, unvisited, distance_matrix):
    tour = [start]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: distance_matrix[last, x])
        tour.append(next_city)
        unvisited.remove(next_city)
    return tour

unvisited_cities = set(city_indices) - {depots[0], depots[1]}
robot0_cities = nearest_neighbor_tour(depots[0], unvisited_cities.copy(), distance_matrix)
robot1_cities = nearest_neighbor_tour(depots[1], unvisited_cities - set(robot0_cities), distance_matrix)

robot0_tour = robot0_cities
robot1_tour = robot1_cities

# Calculate the total distance cost
total_cost = 0
robot0_cost = calculate_total_distance(robot0_tour, distance_array)
robot1_cost = calculate_total_distance(robot1_tour, distance_array)
total_cost = robot0_cost + robot1_cost

# Print results
print(f"Robot 0 Tour: {robot0_tour}")
print(f"Robot 0 Total Travel Cost: {robot0_cost}")
print(f"Robot 1 Tour: {robot1_tour}")
print(f"Robot 1 Total Travel Cost: {robot1_cost}\n")
print(f"Overall Total Travel Cost: {total_cost}")