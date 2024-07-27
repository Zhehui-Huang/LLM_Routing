import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

def calculate_distance(coord1, coord2):
    return euclidean(coord1, coord2)

def two_opt(route, distance_matrix):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if sum(distance_matrix[best[k]][best[k + 1]] for k in range(len(best) - 1)) > sum(distance_matrix[new_route[k]][new_route[k + 1]] for k in range(len(new_route) - 1)):
                    best = new_route
                    improved = True
        route = best
    return best

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Parameters
num_robots = 4

# Creating a distance matrix
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Initial clustering using K-Means
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # excluding the depot city
labels = kmeans.labels_

# Assigning cities to each robot
robot_routes = {i: [0] for i in range(num_robots)}
for i, label in enumerate(labels, start=1):
    robot_routes[label].append(i)

# Adding the depot city to the end of each robot's route
for route in robot_routes.values():
    route.append(0)

# Optimizing each route using 2-opt
optimized_routes = {}
route_costs = {}
for robot_id, route in robot_routes.items():
    optimized_route = two_opt(route, distance_matrix)
    optimized_routes[robot_id] = optimized_route
    route_cost = sum(distance_matrices[optimized_route[i]][optimized_route[i + 1]] for i in range(len(optimized_route) - 1))
    route_costs[robot_id] = route_cost

# Output the tours and costs
overall_total_cost = 0
for robot_id, route in optimized_routes.items():
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {route_supp_costs_costs_costs[bot_id]}")
    overall_total_cost += replace_costs_costs_suffix_minus_suffix_withable_costs_ste