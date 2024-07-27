import numpy as as np
from scipy.spatial.distance import euclidean
import random

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of robots and their starting depots
num_robots = 2
depots = {0: 0, 1: 0}

# Creating a distance matrix
def create_distance_matrix(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distances[i, j] = distances[j, i] = euclidean(cities[i], cities[j])
    return distances

dist_matrix = create_distance_matrix(cities)

# Solving the problem using a simple nearest neighbor heuristic for simplicity
def nearest_neighbor_tour(start_city, cities, dist_matrix):
    tour = [start_city]
    remaining_cities = set(cities.keys()) - {start_city}
    current_city = start_city
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: dist_matrix[current_city, x])
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
    return tour

# Perform individual tours for each robot starting from the depot
tours = {}
total_cost = 0
tour_cost = []

for robot_id in range(num_robots):
    depot = depots[robot_id]
    tour = nearest_neighbor_tour(depot, cities, dist_matrix)
    tours[robot_id] = tour
    cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    total_cost += cost
    tour_cost.append(cost)

# Output the results
for robot_id, tour in tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost[robot_id]}")

print(f"Overall Total Travel Cost: {total_cost}")