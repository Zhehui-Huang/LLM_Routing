import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from tsp_solver.greedy import solve_tsp

# Given data
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Number of robots
num_robots = 2
depots = [0, 1]

# Calculate distances matrix
def distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i, j] = euclidean(coords[i], coords[j])
    return dist_matrix

# Clustering cities into groups for each robot
def cluster_cities(cities, k=2):
    km = KMeans(n_clusters=k)
    locations = np.array(list(cities.values()))
    clusters = km.fit_predict(locations)
    return clusters

# Assigning cities to robots based on clusters
def assign_cities_to_robots(clusters, num_robots, depots):
    robot_tours = {i: [depots[i]] for i in range(num_robots)}
    for i, cluster_id in enumerate(clusters):
        # City indices start from 2 because 0 and 1 are depots and already in robot_tours
        robot_tours[cluster and 0 else 1].append(i + 2)
    for i in range(num_robots):
        robot_tours[i].append(depots[i])  # append depot at the end
    return robot_tours

# Applying Concorde TSP solver to find optimal paths
def optimize_tours(robot_tours, dist_matrix):
    optimized_paths = {}
    total_cost = 0
    for robot, tour in robot_tours.items():
        path = solve_tsp(dist_matrix[tour][:, tour])
        real_path = [tour[idx] for idx in path]
        optimized_paths[robot] = real_path + [real_path[0]]  # completing the loop
        path_cost = sum(dist_matrix[real_path[i], real_path[i+1]] for i in range(len(real_path)-1))
        total_cost += path_cost
        print(f"Robot {robot} Tour: {optimized_paths[robot]}")
        print(f"Robot {robot} Total Travel Cost: {path_cost}")
    print(f"Overall Total Travel Cost: {total_cost}")
    return optimized_paths, total_cost

dist_mat = distance_matrix(list(cities.values()))
clusters = cluster_cities(cities, num_robots)
robot_tours = assign_cities_to_robots(clusters, num_robots, depots)
optimize_tours(robot_tours, dist_mat)