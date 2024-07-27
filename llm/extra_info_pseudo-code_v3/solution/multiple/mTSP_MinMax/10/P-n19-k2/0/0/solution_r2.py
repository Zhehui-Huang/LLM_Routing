import numpy as np
from scipy.spatial import distance
from sklearn.cluster import KMeans

# Coordinates of the cities, including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

num_robots = 2
depot_index = 0

def compute_distance(c1, c2):
    """ Calculates the Euclidean distance between two cities """
    return distance.euclidean(c1, c2)

def initialize_routes(k_clusters):
    """ Initializes routes using K-Means clustering """
    kmeans = KMeans(n_clusters=k_clusters).fit(coordinates[1:])  # Exclude the depot
    labels = kmeans.labels_
    
    routes = [[] for _ in range(k_clusters)]
    for i, label in enumerate(labels):
        routes[label].append(i + 1)
    
    # Adding depot to the start and end of each route
    for route in routes:
        route.insert(0, depot_index)
        route.append(depot_index)
    return routes

def calculate_route_cost(route):
    """ Calculates the total cost for a given tour """
    return sum(compute_distance(coordinates[route[i]], coordinates[route[i+1]]) for i in range(len(route) - 1))

def optimize_routes(routes):
    """ Optimizes routes through a simple swap heuristic (could be enhanced with more complex algorithm) """
    improved = True
    while improved:
        improved = False
        for route_index, route in enumerate(routes):
            best_cost = calculate_route_cost(route)
            for i in range(1, len(route) - 2):
                for j in range(i + 1, len(route) - 1):
                    new_route = route[:]
                    new_route[i], new_route[j] = new_route[j], new_route[i]
                    new_cost = calculate_route_cost(new_route)
                    if new_cost < best_cost:
                        routes[route_index] = new_route
                        best_cost = new_cost
                        improved = True
    return routes

# Initialize and optimize routes
routes = initialize_routes(num_robots)
optimized_routes = optimize_routes(routes)

# Calculate costs and find maximum cost
costs = [calculate_route_cost(route) for route in optimized_routes]
max_cost = max(costs)

# Output results
for idx, route in enumerate(optimized_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {int(costs[idx])}")
print(f"Maximum Travel Cost: {int(max_cost)}")