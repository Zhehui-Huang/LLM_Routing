import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from itertools import permutations

# Cities and coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Function to calculate distance between two cities
def calculate_distance(city1, city2):
    return euclidean(city_coordinates[city1], city_coordinates[city2])

# Assign cities to clusters using KMeans
num_robots = 4
kmeans = KMeans(n_clusters=num_robots).fit(city_coordinates)
labels = kmeans.labels_

# Partition cities based on clusters
city_clusters = {i: [] for i in range(num_robots)}
for index, label in enumerate(labels):
    city_clusters[label].append(index)

# Function to find the minimum distance path for given cities (brute-force approach)
def find_min_path(cities):
    min_distance = float('inf')
    min_path = []
    cities_permutations = permutations(cities)
    for path in cities_permutations:
        # Calculate the distance for this permutation
        distance = sum(calculate_distance(path[i], path[i+1]) for i in range(len(path) - 1))
        if distance < min_distance:
            min_distance = distance
            min_path = path
    return min_path, min_distance

# Find minimum path for each robot
robot_tours = {}
robot_costs = {}
overall_total_cost = 0

for robot_id, cities in city_clusters.items():
    tour, cost = find_min_path(cities)
    robot_tours[robot_id] = tour
    robot_costs[robot_tour] = cost
    overall_total_cost += cost

# Print results
for robot_id in range(num_robots):
    print(f"Robot {robot_id} Tour: {robot_tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {robot_costs[robot_id]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")