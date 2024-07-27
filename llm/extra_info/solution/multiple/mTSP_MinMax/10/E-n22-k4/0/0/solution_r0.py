import math
from typing import List, Tuple
from sklearn.cluster import KMeans
import numpy as np

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Helper function to calculate Euclidean distance between two cities
def euclidean_dist(idx1: int, idx2: int) -> float:
    x1, y1 = coordinates[idx1]
    x2, y2 = coordinates[idx2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Calculate distances matrix
num_cities = len(coordinates)
distances = [[euclidean_dist(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Number of robots
num_robots = 4

# Initial solution - clustering cities into groups
kmeans = KMeans(n_clusters=num_robots, random_state=42)
city_indices = np.array(range(1, num_cities))  # city indices excluding depot
city_locations = np.array(coordinates)[city_indices]
clusters = kmeans.fit_predict(city_locations)

# Creating tours for each robot and compute distances
tours = {i: [0] for i in range(num_robots)}  # starting each tour from the depot
total_costs = {i: 0 for i in range(num_robots)}

for robot in range(num_robots):
    prev_city = 0  # start from depot
    for city_index, cluster in enumerate(clusters):
        if cluster == robot:
            city = city_indices[city_index]
            tours[robot].append(city)
            total_costs[robot] += distances[prev_city][city]
            prev_city = city
    # Return to depot
    tours[robot].append(0)
    total_costs[robot] += distances[prev_city][0]

# Computing max cost
max_travel_cost = max(total_costs.values())

# Displaying results
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]:.2f}")

print(f"Maximum Travel Cost: {max_travel_cost:.2f}")