import numpy as np
from sklearn.cluster import MiniBatchKMeans
import math

# Coordinates of the cities (excluding the depot city)
coordinates = np.array([
    [151, 264], [159, 261], [130, 254], [128, 252], [163, 247], [146, 246],
    [161, 242], [142, 239], [163, 236], [148, 232], [128, 231], [156, 217],
    [129, 214], [146, 208], [164, 208], [141, 206], [147, 193], [164, 193],
    [129, 189], [155, 185], [139, 182]
])

def euclidean_dist(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

num_robots = 4
depot = np.array([[145, 215]])

# Cluster cities into groups for each robot
kmeans = MiniBatchKMeans(n_clusters=num_robots, random_state=0).fit(coordinates)
clusters = kmeans.predict(coordinates)

def nearest_neighbor_tour(points):
    remaining = list(range(len(points)))
    tour = [remaining.pop(0)]  # start from the first city in the cluster
    current_city = tour[0]
    
    while remaining:
        nearest_city = min(remaining, key=lambda city: euclidean_dist(points[current_city], points[city]))
        current_city = nearest_city
        tour.append(current_city)
        remaining.remove(current_city)
    
    return tour

tours = []
total_distance = 0

# Generate tours for each robot
for i in range(num_robots):
    cluster_indices = np.where(clusters == i)[0]
    cluster_points = coordinates[cluster_indices]
    
    # Insert depot as the start and end point
    cluster_points_with_depot = np.vstack([depot, cluster_points, depot])
    
    tour_indices = nearest_neighbor_tour(cluster_points_with_depot)
    tour = [0] + list(cluster_indices[tour_indices[1:-1]] + 1) + [0]  # adjust indices for output
    tour_distance = sum(euclidean_dist(cluster_points_with_depot[tour[i]], cluster_points_with_depot[tour[i+1]]) for i in range(len(tour)-1))
    
    tours.append(tour)
    total_distance += tour_distance
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_distance}")

print(f"Overall Total Travel Cost: {total_dist}")