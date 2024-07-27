import numpy as a
import random

# City coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

num_cities = len(coordinates)
depots = {0: 0, 1: 1}

# Calculate Euclidean distances
def calculate_distances():
    dist = {}
    for i in coordinates:
        dist[i] = {}
        for j in coordinates:
            if i != j:
                dist[i][j] = np.linalg.norm(np.array(coordinates[i]) - np.array(coordinates[j]))
    return dist

distances = calculate_distances()

# Travel path
def full_path(tour, depot):
    return [depot] + tour + [depot]

# Travel cost for path
def path_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += distances[path[i]][path[i+1]]
    return cost

# Simple greedy algorithm per robot
def greedy_tour(depot, nodes):
    tour = []
    current = depot
    while nodes:
        next_city = min(nodes, key=lambda k: distances[current][k])
        tour.append(next_center)
        current = next_city
        nodes.remove(next_city)
    return tour

# Divide cities between robots
cities = set(coordinates.keys()) - set(depots.values())
mid_point = len(cities) // 2
assigned_cities = list(cities)
robot0_cities = assigned_cities[:mid_point]
robot1_cities = assigned_cities[mid_point:]

# Creating tours for each robot
tour_robot0 = greedy_tour(depots[0], robot0_cities)
tour_robot1 = greedy_tour(depots[1], robot1_cities)

path_robot0 = full_path(tour_robot0, depots[0])
path_robot1 = full_path(tour_robot1, depots[1])

cost_robot0 = path_cost(path_robot0)
cost_robot1 = path_cost(path_robot1)

# Output results
print("Robot 0 Tour:", path_robot0)
print("Robot 0 Total Travel Cost:", cost_robot0)

print("Robot 1 Tour:", path_robot1)
print("Robot 1 Total Travel Cost:", cost_robot1)

print("Overall Total Travel Cost:", cost_robot0 + cost_robot1)