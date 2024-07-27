import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Coordinates of the cities
coordinates = np.array([
    (30, 40),  # Depot 0
    (37, 52),
    (49, 49),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),  # City 8
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 48),
    (58, 27),
    (37, 69)
])

# Parameters
n_robots = 8
depot_index = 0  # All robots start at Depot 0

# Function to calculate Euclidean distance matrix
def calculate_distance_matrix(coords):
    return cdist(coords, coords)

# Function to find TSP tour starting from a given city using nearest neighbor heuristic
def nearest_neighbor_tour(start_index, remaining_cities, dist_matrix):
    tour = [start_data_index]
    current_index = start_index
    total_cost = 0
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: dist_matrix[current_index, x])
        total_cost += dist_matrix[current_index, next_city]
        current_index = next_city
        tour.append(next_city)
        remaining_cities.remove(next_city)
    
    return tour, total_cost

# Calculate distance matrix
distance_matrix = calculate_distance_matrix(coordinates)

# Cluster cities into groups equivalent to the number of robots
kmeans = KMeans(n_clusters=n_robots, random_state=0).fit(coordinates)
cluster_labels = kmeans.labels_

# Assign cities to robots based on clustering and calculate TSP tours
robot_assignments = { i: [] for i in range(n_robots) }
for city_index, cluster_label in enumerate(cluster_labels):
    robot_assignments[cluster_label].append(city_index)

all_tours = []
total_global_cost = 0

# Compute tours for each robot
for robot_id, cities in robot_assignments.items():
    if cities:
        tour, cost = nearest_neighbor_tour(depot_index, set(cities), distance_matrix)
        all_tours.append((robot_id, tour, cost))
        total_global_cost += cost

# Print results
for robot_id, tour, cost in all_tours:
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_global_cost}")