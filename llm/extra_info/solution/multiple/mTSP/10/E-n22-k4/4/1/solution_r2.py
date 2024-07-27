import numpy as np
from sklearn.cluster import KMeans
import math

# Define city coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]

# Define the number of robots
n_robots = 4

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix
def create_distance_matrix(coordinates):
    size = len(coordinates)
    dist_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            dist_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
    return dist_matrix

# Implementing a simple version of the 2-opt algorithm
def two_opt(route, dm):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]
                if sum(dm[new_route[k]][new_route[k + 1]] for k in range(len(new_route) - 1)) < sum(dm[best[k]][best[k + 1]] for k in range(len(best) - 1)):
                    best = new_route
                    improved = True
        route = best
    return best

# Clustering cities into regions for each robot
dist_matrix = create_distance_matrix(coordinates)
kmeans = KMeans(n_clusters=n_robots, random_state=42)
cluster_labels = kmeans.fit_predict(coordinates[1:])
clusters = {i: [0] + [idx + 1 for idx, label in enumerate(cluster_labels) if label == i] + [0] for i in range(n_robots)}

# Solve TSP for each robot's route
total_distance = 0
for robot_id, nodes in clusters.items():
    route = two_opt(nodes, dist_matrix)
    route_cost = sum(dist_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    total_distance += route_cost
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {route='.2f'}route_cost")

print(f"Overall Total Travel Cost: {total_distance}")