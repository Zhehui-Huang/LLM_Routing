import numpy as np
from scipy.spatial import distance_matrix

# Define the coordinates of cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Generate a distance matrix based on Euclidean distance
coords = np.array(list(cities.values()))
dist_matrix = distance_matrix(coords, coords)

# Number of robots and their start/end depots
robots = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7
}

# Implementing a naive solution that assigns robots to the nearest unvisited city until all cities are visited
from collections import defaultdict

def nearest_neighbor_tour(start_index, unvisited_cities, dist_matrix, return_to_start=True):
    tour = [start_index]
    current_city = start_index
    total_cost = 0
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: dist_matrix[current_city][x])
        total_cost += dist_matrix[current_city][next_city]
        current_city = next_city
        tour.append(current_city)
        unvisited_cities.remove(current_city)
    if return_to_start:
        total_cost += dist_matrix[current_city][start_index]
        tour.append(start_index)
    return tour, total_cost

unvisited_cities = set(range(16))  # all cities
robot_tours = {}
total_overall_cost = 0

for robot_id, start_and_end in robots.items():
    if unvisited_cities:
        tour, cost = nearest_neighbor_tour(start_and_end, unvisited_cities, dist_matrix)
        robot_tours[robot_id] = (tour, cost)
        total_overall_cost += cost

# Output results
for robot_id, (tour, cost) in robot_tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {total_overall_cost}")