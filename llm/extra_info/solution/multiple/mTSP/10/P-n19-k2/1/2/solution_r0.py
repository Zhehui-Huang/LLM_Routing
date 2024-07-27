import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from itertools import permutations

def calculate_distance(city1, city2):
    return euclidean(city1, city2)

def total_tour_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

def solve_tsp_brute_force(cities, coordinates):
    min_tour = None
    min_cost = float('inf')
    for perm in permutations(cities):
        tour = [0] + list(perm) + [0]  # starting and ending at the depot
        cost = total_tour_cost(tour, coordinates)
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
    return min_tour, min_cost

# Define coordinates for each city including the depot
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
               (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Number of robots
num_robots = 2

# Cluster cities (except the depot) into the number of robots groups
city_indices = np.array(range(1, len(coordinates)))  # exclude depot city 0 in clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit([coordinates[i] for i in city_indices])

# Assign cities to robots based on clusters
robot_city_groups = {i: [] for i in range(num_robots)}
for idx, label in enumerate(kmeans.labels_):
    robot_city_groups[label].append(city_indices[idx])

# Solve TSP for each robot
overall_total_cost = 0
for robot_id, cities in robot_city_groups.items():
    tour, cost = solve_tsp_brute_force(cities, coordinates)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
    overall_total_cost += cost

print(f"Overall Total Travel Cost: {overall_total_cost}")