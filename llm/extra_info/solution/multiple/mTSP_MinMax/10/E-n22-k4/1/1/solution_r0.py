import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from itertools import permutations

# Define city locations
city_locations = np.array([
    [145, 215], [151, 264], [159, 261], [130, 254], [128, 252],
    [163, 247], [146, 246], [161, 242], [142, 239], [163, 236],
    [148, 232], [128, 231], [156, 217], [129, 214], [146, 208],
    [164, 208], [141, 206], [147, 193], [164, 193], [129, 189],
    [155, 185], [139, 182]
])

# Number of robots
num_robots = 4

# Function to calculate the TSP tour using a simple heuristic of nearest-neighbor
def calculate_tsp_tour(points):
    start = points[0]
    path = [start]
    unvisited = points[1:]
    while unvisited:
        next_point = min(unvisited, key=lambda x: euclidean(path[-1], x))
        path.append(next_point)
        unvisited.remove(next_point)
    path.append(start)
    return path

# Function to calculate the total cost of the tour
def calculate_tour_cost(tour):
    return sum(euclidean(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Cluster cities into groups (one for each robot)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_locations[1:])
labels = kmeans.labels_

tours = []
costs = []

# Calculate TSP for each cluster
for i in range(num_robots):
    cluster_indices = np.where(labels == i)[0] + 1  # +1 because city indices start from 1, not considering depot initially
    if len(cluster_indices) > 0:
        cluster_points = [city_locations[0]] + list(city_locations[cluster_indices])
        tsp_tour = calculate_tsp_tour(cluster_points)
        tour_cost = calculate_tour_cost(tsp_tour)
        tours.append([0] + [np.where(city_locations == point)[0][0] for point in tsp_tour[1:-1]] + [0])
        costs.append(tour_cost)

max_cost = max(costs)

# Output the results
for idx, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")