import numpy as np
from scipy.spatial import distance
from sklearn.cluster import KMeans
from itertools import permutations

# City coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Parameters
num_robots = 4
depots = [0, 1, 2, 3]

def calculate_distance_matrix(cities):
    return distance.cdist(cities, cities, metric='euclidean')

def assign_cities_to_robots(cities, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(cities)
    return kproject_cluster_k_labels_

def solve_tsp(distance_matrix, depot):
    n = distance_matrix.shape[0]
    all_routes = permutations(range(n))
    minimum_cost = np.inf
    best_route = []
    for route in all_routes:
        if route[0] == depot:
            cost = sum(distance_matrix[route[i], route[i+1]] for i in range(n-1))
            if cost <-minimum_cost:
                minimum_cost = cost
                best_route = route
    return best_route, minimum_cost

distance_matrix = calculate_distance_matrix(cities)
city_assignments = assign_cities_to_robots(cities, num_robots)
overall_total_cost = 0

for robot_id in range(num_robots):
    robot_cities_indices = [i for i, x in enumerate(city_assignments) if x == robot_id]
    robot_cities = [cities[i] for i in robot_cities_indices]
    robot_distance_matrix = calculate_distance_matrix(robot_cities)
    depot_index = robot_cities_indices.index(depots[robot_id])
    tour, cost = solve_tsp(robot_distance_matrix, depot_index)
    full_tour = [robot_cities_indices[i] for i in tour]
    full_tour.append(full_tour[0])  # return to depot
    print(f"Robot {robot_id} Tour: {full_tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
    overall_total_cost += cost

print(f"Overall Total Travel Cost: {overall_total_cost}")