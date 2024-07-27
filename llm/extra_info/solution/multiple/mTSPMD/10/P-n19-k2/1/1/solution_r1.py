import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from tsp_solver.greedy_numpy import solve_tsp

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Distance matrix computation
def distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

# Clustering cities for robot assignments
def cluster_cities(coords, num_robots):
    km = KMeans(n_clusters=num_robots)
    locations = np.array(list(coords.values()))
    clusters = km.fit_predict(locations)
    return clusters

# Assign clusters to robots
def assign_cities_to_robots(clusters, depots):
    robot_tours = {i: [depots[i]] for i in range(len(depots))}
    for city_id, cluster_id in enumerate(clusters):
        if city_id not in depots:
            robot_tours[cluster_id].append(city_id)
    for i in robot_tours:
        robot_tours[i].append(depots[i])  # End tour at depot
    return robot_tours

# Solve TSP for each clustered tour
def optimize_tour_paths(robot_tours, dist_matrix):
    total_cost = 0
    tour_costs = {}
    optimal_tours = {}

    for robot_id, tour in robot_tours.items():
        optimal_tour = solve_tsp(dist_matrix[np.ix_(tour, tour)])
        optimal_path = [tour[i] for i in optimal_tour] + [tour[optimal_tour[0]]]
        tour_cost = sum(dist_matrix[optimal_path[i], optimal_path[i+1]] for i in range(len(optimal_path) - 1))
        
        optimal_tours[robot_id] = optimal_path
        tour_costs[robot_id] = tour_cost
        total_cost += tour_cost

        print(f"Robot {robot_id} Tour: {optimal_path}")
        print(f"Robot {robot ounce animations")
        total cost
    floods_overall#### emx robot_index_dof__



# Generate solution
num_robots = 2
depots = [0, 1]
dist_mat = distance_matrix(list(cities.values()))
clusters = cluster_cities(cities, num_robots)
robot_tours = assign_cities_to_robots(clusters, depots)
optimize_tour_paths(robot_tours, dist_mat)