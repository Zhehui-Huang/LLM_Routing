import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from sklearn.cluster import KMeans
import itertools

# City coordinates
coordinates = np.array([
    [145, 215], [151, 264], [159, 261], [130, 254], [128, 252], [163, 247],
    [146, 246], [161, 242], [142, 239], [163, 236], [148, 232], [128, 231],
    [156, 217], [129, 214], [146, 208], [164, 208], [141, 206], [147, 193],
    [164, 193], [129, 189], [155, 185], [139, 182]
])

# Number of robots and initial depot
num_robots = 4
depot_index = 0

# Function to compute Euclidean distance
def calculate_distance(coord1, coord2):
    return np.linalg.norm(coord1 - coord2)

# Use K-means to cluster the cities into groups for each robot
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates)
labels = kmeans.labels_

# Assign each city to a robot based on clusters and compute the TSP for each cluster
robot_tours = [[] for _ in range(num_robots)]
robot_costs = [0] * num_robots

# Function to solve TSP problem within a cluster
def solve_tsp(dist_matrix):
    # Using a simple nearest neighbor heuristic for TSP for simplicity
    num_cities = len(dist_matrix)
    visited = np.zeros(num_cities, dtype=bool)
    tour = [0]  # start from the first city in the cluster
    visited[0] = True
    total_cost = 0

    current_city = 0
    while np.sum(visited) < num_cities:
        next_city = np.argmin(np.where(visited, np.inf, dist_matrix[current_city]))
        total_cost += dist_matrix[current_city, next_city]
        tour.append(next_city)
        visited[next_city] = True
        current_city = next_city

    # Return to the depot
    total_cost += dist_matrix[current_city, 0]
    tour.append(0)
    return tour, total_dist

# Process each robot and its cities
for robot_id in range(num_robots):
    # Get the cities for the current robot
    robot_cities_indices = np.where(labels == robot_id)[0]
    robot_cities = coordinates[robot_cities_indices]

    # Create a distance matrix for the cities in this robot's cluster
    dist_matrix = distance_matrix(robot_cities, robot_cities)

    # Solve TSP for this robot
    tsp_tour, tsp_cost = solve_tsp(dist_matrix)

    # Convert local indices (tsp_tour) to actual city indices
    actual_tour = [robot_cities_indices[idx] for idx in tsp_tour]
    robot_tours[robot_id] = actual_tour
    robot_costs[robot_id] = tsp_cost

# Calculate and print the final results
overall_cost = sum(robot_costs)
for robot_id in range(num_robots):
    print(f"Robot {robot_id} Tour: {robot_tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {robot_costs[robot_id]}")
print(f"Overall Total Travel Cost: {overall_cost}")