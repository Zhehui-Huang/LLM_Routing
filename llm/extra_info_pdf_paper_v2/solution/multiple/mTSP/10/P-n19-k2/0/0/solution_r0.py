import numpy as np
from scipy.spatial.distance import cdist

# City coordinates (index corresponds to city numbers)
coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
num_robots = 2

# Helper functions
def euclidean_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def nearest_neighbor_tour(start_city, cities, city_coords):
    tour = [start_city]
    current_city = start_city
    local_coords = city_coords.copy()
    
    while len(local_coords) > 1:
        current_index = tour[-1]
        next_index = np.argmin([euclidean_distance(city_coords[current_index], coord) if i not in tour else float('inf') for i, coord in enumerate(city_coords)])
        tour.append(next_index)

    return tour + [start_city]

# Clustering cities for each robot (simplified approach)
kmeans_centroids = [(30, 40), (40, 40)]  # Initial centroids (simplified)
cluster_labels = [np.argmin([euclidean Distance(coord, centroid) for centroid in kmeans_centroids]) for coord in coords[1:]]  # Exclude depot

# Assigning cities to each robot
robot_tours = {i: [0] for i in range(num_robots)}  # Start at depot
for i, cluster_id in enumerate(cluster_labels):
    robot_tours[cluster_id].append(i + 1)  # city indices are offset by 1

# Completing tours by solving small TSP for each robot
for i in range(num_robots):
    full_tour = nearest_neighbor_tour(0, robot_tours[i][1:], coords)
    robot_tours[i] = full_tour

# Calculate the distances for each robot's tour
def calculate_tour_cost(tour, coords):
    return sum(euclidean_distance(coords[tour[i]], coords[tour[i + 1]]) for i in range(len(tour) - 1))

# Output
total_cost = 0
for i in range(num_robots):
    tour_cost = calculate_tour_cost(robot_tours[i], coords)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {robot_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")