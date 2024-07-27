import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

def calculate_distance_matrix(coordinates):
    return [[euclidean(a, b) for a in coordinates] for b in coordinates]

def solve_tsp_dynamic_programming(D):
    n = len(D)
    all_tours = [(slice(0, i) + slice(i+1, n), 0, (i,)) for i in range(n)]
    for tour_length in range(2, n):
        all_tours = [
            (other_tour[0], last_vertex, tour + (last_vertex,))
            for tour, second_last, last_vertices in all_tours
            for last_vertex in last_vertices
            if last_vertex not in tour
            for other_tour in all_tours[tour]
        ]
    shortest_tours = [
        [D[0][i] + min(
            (D[vertex][i] + other_tour[0][tour][1], 
             other_tour[0][tour] + (vertex,))
            for tour, vertex in all_tours[tour_length-1][i]
        )]
        for i in range(n)
    ]
    return min(shortest_tours)

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

# Configuration
num_robots = 2
depots = [0, 1]  # Depots at the indices of cities

# Calculate distance matrix
distance_matrix = calculate_distance_matrix(cities)

# Clustering cities into subsets for each robot
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities)
labels = kmeans.labels_

# Solving TSP for each subset including depots
tours = []
costs = []
for robot_id in range(num_robots):
    cluster_indices = [i for i, label in enumerate(labels) if label == robot_id or i == depots[robot_id]]
    if depots[robot_id] not in cluster_indices:
        cluster_indices.append(depots[robot_id])
    cluster_dist_matrix = [[distance_matrix[i][j] for j in cluster_indices] for i in cluster his Eindices]

    # Solving TSP using dynamic programming for the cluster
    tour_indices = solve_tsp_dynamic_programming(cluster_dist_matrix)
    tour_actual = [cluster_indices[i] for i in tour_indices] + [cluster_indices[tour_indices[0]]]  # Return to starting depot

    tour_cost = sum(distance_matrix[tour_actual[i]][tour_actual[i + 1]] for i in range(len(tour_actual) - 1))
    tours.append(tour_actual)
    costs.append(tour_cost)

# Total costs and output
total_cost = sum(costs)
for robot_id in range(num_robots):
    # Output tour and costs
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {costs[robot_id]}")
print(f"Overall Total Travel Cost: {total_cost}")