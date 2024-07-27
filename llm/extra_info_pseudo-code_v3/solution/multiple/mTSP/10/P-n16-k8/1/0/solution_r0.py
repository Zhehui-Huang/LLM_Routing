import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# City coordinates and robot information
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64),
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

num_robots = 8

# Calculate Euclidean distance matrix
distance_matrix = cdist(coordinates, coordinates)

# Function to compute tour cost
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Function to solve the TSP problem for one robot
def solve_tsp(distances, start_node=0):
    from itertools import permutations

    n = len(distances)
    min_route = None
    min_cost = float('inf')
    
    for perm in permutations(range(1, n)):
        current_route = [start_node] + list(perm) + [start_node]
        current_cost = calculate_tour_cost(current_route, distances)
        if current_cost < min_cost:
            min_cost = current_cost
            min_route = current_route
    
    return min_route, min_cost

# Assign cities to clusters (each robot will handle one cluster)
city_indices = range(1, len(coordinates))  # Exclude the depot city
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])
clusters = kmeans.labels_

# Solve TSP for each robot
overall_total_cost = 0
for robot_id in range(num_robots):
    indices = [0] + [idx + 1 for idx, cluster in enumerate(clusters) if cluster == robot_id]
    robot_coords = [coordinates[idx] for idx in indices]
    robot_distances = cdist(robot_coords, robot_coords)
    
    tour, cost = solve_tsp(robot_distances)
    overall_total_cost += cost
    
    # Map local index back to original index
    actual_tour = [indices[i] for i in tour]
    
    print(f"Robot {robot_id} Tour: {actual_tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}\n")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")