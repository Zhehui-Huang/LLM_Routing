import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Coordinates of the cities
coordinates = np.array([
    (30, 40),
    (37, 52),
    (49, 49),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 48),
    (58, 27),
    (37, 69)
])

n_robots = 8
depot_location_index = 0

# Compute the Euclidean distance matrix
distance_matrix = cdist(coordinates, coordinates)

# Cluster cities into n_robots clusters
kmeans = KMeans(n_clusters=n_robots, random_state=0).fit(coordinates)
labels = kmeans.labels_

# Function to perform the nearest neighbor heuristic for TSP
def nearest_neighbor_tsp(start_index, city_indices, distance_matrix):
    tour = [start_index]
    current_index = start, city_indices.pop(start_index, None)
    total_cost = 0
    
    while city_indices:
        next_city = min(city_indices, key=lambda x: distance_matrix[current_index, x])
        total_cost += distance_matrix[current_index, next_city]
        current_index = next_city
        tour.append(next_city)
        city_indices.pop(next_city)
    
    return tour, total_cost

# Dictionary to store tours for each robot
robot_tours = {}
total_cost = 0

for robot in range(n_robots):
    # Find cities corresponding to the current cluster
    city_indices = {i for i, cluster_id in enumerate(labels) if cluster_id == robot}
    if len(city_indices) > 0:
        if depot_location_index in city_indices:
            start_city = depot_location_index
        else:
            start_city = city_indices.pop()  # Start at any city for now if depot not in cluster
        
        tour, cost = nearest_neighbor_tsp(start_city, city_indices, distance_matrix)
        robot_tours[robot] = (tour, cost)
        total_cost += cost

# Output results
for robot, (tour, cost) in robot_tours.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")