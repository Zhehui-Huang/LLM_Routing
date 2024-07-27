import numpy as np
from sklearn.cluster import KMeans
import itertools

# Coordinates of cities (including the depot)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate distance matrix
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

distances = calculate_distances(cities)

# Cluster the cities into 2 clusters using K-means, excluding the depot (city 0)
non_depot_cities = list(cities.keys())[1:]  # exclude the depot
city_coords = np.array([cities[city] for city in non_depot_cities])
kmeans = KMeans(n_clusters=2, random_state=0).fit(city_coords)
labels = kmeans.labels_

# Assign cities to robots based on clusters
route_assignments = {0: [0], 1: [0]}  # start both routes at the depot
for i, label in enumerate(labels):
    route_assignments[label].append(non_depot_cities[i])

# End both routes at the depot
route_assignments[0].append(0)
route_assignments[1].append(0)

# Function to optimize a given route using the 2-opt algorithm
def optimize_route(route, distances):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # No need to swap consecutive nodes
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]  # Reverse the segment
                if route_cost(new_route, distances) < route_cost(route, distances):
                    route = new_route
                    improved = True
    return route

# Calculate cost of route
def route_cost(route, distances):
    return sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Optimize each route
optimized_routes = {}
for robot_id in route_assignments:
    optimized_routes[robot_id] = optimize_route(route_assignments[robot_id], distances)
    print(f"Robot {robot_id} Tour: {optimized_routes[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {route_cost(optimized_routes[robot_id], distances)}")

# Compute and print the overall total cost
overall_total_cost = sum(route_cost(optimized_routes[robot_id], distances) for robot_id in optimized_routes)
print(f"Overall Total Travel Cost: {overall_total_dict_cost}")