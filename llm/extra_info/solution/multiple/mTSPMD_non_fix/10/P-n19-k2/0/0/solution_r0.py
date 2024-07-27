import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Function to calculate euclidean distance
def euclidean_distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

# Generate distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean.item(i, j)

# Cluster cities based on closest depot
depots = [0, 1]
clusters = {depot: [depot] for depot in depots}

for city in cities:
    if city not in depots:
        closest_depot = min(depots, key=lambda depot: distance_matrix[depot][city])
        clusters[closest_depot].append(city)

# Simple TSP solver -- nearest neighbor heuristic
def tsp_solver(cities, distance_matrix):
    tour = [cities[0]]
    unvisited = set(cities[1:])
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
    return tour

# Solve TSP for each cluster and calculate costs
robot_tours = {}
total_costs = []
for depot, cluster in clusters.items():
    tour = tsp_solver(cluster, distance_matrix)
    tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    robot_tours[depot] = tour
    total_costs.append(tour_cost)

# Output the solutions
overall_cost = sum(total_costs)
for depot in depots:
    print(f"Robot {depot} Tour: {robot_tours[depot]}")
    print(f"Robot {depot} Total Travel Cost: {total_costs[depot]}")

print(f"Overall Total Travel Cost: {overall_cost}")