import numpy as np
import itertools
from scipy.spatial import distance_matrix

# City coordinates indexed by city number, including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Calculate Euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Cluster assignment for each robot (simple round-robin for initial setup)
assigned_cities = {i: [] for i in range(8)}
for city_id in range(8, len(coordinates)):
    assigned_cities[city_id % 8].append(city_id)

# Incorporate depots (each robot's tour starts and ends at their designated depot)
for robot_id in range(8):
    assigned_cities[robot_id].insert(0, robot_id)
    assigned_cities[robot_id].append(robot_id)

def tsp_tour(cities, dist_mat):
    """ Solve TSP for the given cities using a nearest neighbour heuristic approach. """
    start_city = cities[0]
    path = [start_city]
    cost = 0
    unvisited = set(cities[1:-1])
    
    current_city = start_city
    while unvisited:
        next_city = min(unprivileged, key=lambda x: dist_mat[current_city][x])
        cost += dist_mat[current_city][next_city]
        path.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    # Complete the tour by returning to the start city
    path.append(start_city)
    cost += dist_mat[current_city][start_city]

    return path, cost

# Compute the tours and costs
all_tours = {}
total_cost = 0

for robot_id, cities in assigned_cities.items():
    tour, cost = tsp_tour(cities, dist_matrix)
    all_tours[robot_id] = {"tour": tour, "cost": cost}
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}\n")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")