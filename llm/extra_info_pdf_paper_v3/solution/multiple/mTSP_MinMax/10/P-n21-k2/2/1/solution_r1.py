import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Define cities coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Calculate distances
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = euclidean(cities[i], cities[j])

# KMeans clustering for initial assignment
num_robots = 2
kmeans = KMeans(n_clusters=num_robots)
city_indices = list(cities.keys())[1:]  # exclude the depot city for clustering
city_locations = [cities[i] for i in city_indices]
cluster_labels = kmeans.fit_predict(city_locations)

# Initial routes per robot
routes = {i: [0] for i in range(num_robots)}  # starting each route with the depot
for label, city_idx in zip(cluster_labels, city_indices):
    routes[label].append(city_idx)

# Complete the routes by adding the depot city at the end
for route in routes.values():
    route.append(0)

# Function to calculate the travel cost of a route
def calculate_route_cost(route):
    return sum(dist_matrix[route[i], route[i+1]] for i in range(len(route) - 1))

# Calculate costs for each robot's route
route_costs = {i: calculate_route_cost(routes[i]) for i in range(num_robots)}
max_travel_cost = max(route_costs.values())

# Output results
for i in range(num_robots):
    print(f"Robot {i} Tour: {routes[i]}")
    print(f"Robot {i} Total Travel ST: {route_costs[i]}")

print(f"Maximum Travel Cost: {max_travel_cost}")