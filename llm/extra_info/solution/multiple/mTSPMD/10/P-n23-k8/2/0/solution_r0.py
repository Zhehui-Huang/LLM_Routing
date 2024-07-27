import numpy as np
from sklearn.cluster import KMeans
from tsp_solver.greedy import solve_tsp

# City coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Number of robots (clusters)
num_robots = 8

# Initialize KMeans
kmeans = KMeans(n_clusters=num_robots, init=np.array(coordinates[:num_robots]), n_init=1)

# Fit KMeans
kmeans.fit(coordinates)

# Clusters and tours for each robot
clusters = kmeans.labels_
overall_total_cost = 0

# Helper function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

for robot_id in range(num_robots):
    cluster_indices = [i for i, x in enumerate(clusters) if x == robot_id]
    depot = coordinates[robot_id]
    cluster_coords = [coordinates[i] for i in cluster_indices]
    
    # Solve TSP for this cluster
    if len(cluster_coords) > 1:
        distance_matrix = [[euclidean_distance(p1, p2) for p1 in cluster_coords] for p2 in cluster_coords]
        tour = solve_tsp(distance_matrix)
        ordered_indices = [cluster_indices[i] for i in tour]
    else:
        ordered_indices = cluster_indices

    # Ensure the tour starts and ends at the depot
    ordered_indices = [robot_id] + ordered_indices + [robot_id]

    # Calculate the travel cost for this robot
    robot_travel_cost = sum(euclidean_distance(coordinates[ordered_indices[i]], coordinates[ordered_indices[i+1]]) for i in range(len(ordered_indices) - 1))
    
    overall_total_cost += robot_travel_cost
    print(f"Robot {robot_id} Tour: {ordered_indices}")
    print(f"Robot {robot_id} Total Travel Cost: {robot_travel+", "xx":xx_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")