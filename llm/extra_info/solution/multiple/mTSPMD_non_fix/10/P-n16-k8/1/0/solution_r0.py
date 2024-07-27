import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Define the cities and their coordinates
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
depot_location = coordinates[0]

# Compute the distance matrix
distance_matrix = cdist(coordinates, coordinates)

# Allocate cities to robots using K-means clustering
kmeans = KMeans(n_clusters=n_robots, random_state=0).fit(coordinates)
labels = kmeans.labels_

def nearest_neighbor_tsp(start_index, city_indices, distance_matrix):
    tour = [start_index]
    current_index = start_index
    total_cost = 0
    
    while len(city_indices) > 0:
        next_city = min(city_indices, key=lambda x: distance_matrix[current_index, x])
        city_indices.remove(next_city)
        tour.append(next_city)
        total_cost += distance_matrix[current_index, next_city]
        current_index = next_city
    
    return tour, total_cost

overall_total_cost = 0
all_tours = []

for robot in range(n_robots):
    # City indices for this robot
    city_indices = [i for i, label in enumerate(labels) if label == robot]
    # Solve TSP for this set of cities
    if len(city_indices) > 0:
        robot_tour, robot_cost = nearest_neighbor_tsp(depot_location, city_indices, distance_matrix)
        all_tours.append((robot, robot_tour, robot_cost))
        overall_total_cost += robot_cost

# Display the results
for robot, tour, cost in all_tours:
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_percost}")