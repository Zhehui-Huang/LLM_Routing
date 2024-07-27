import numpy as np
from scipy.spatial import distance
from sklearn.cluster import KMeans

# City coordinates (Depot + 18 cities)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

num_robots = 2
depot_index = 0

def euclidean_distance(city1, city2):
    return distance.euclidean(city1, city2)

def initialize_routes(num_robots):
    # Cluster cities using KMeans, excluding the depot
    kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])
    labels = kmeans.labels_
    
    routes = [[] for _ in range(num_robots)]
    for idx, label in enumerate(labels):
        routes[label].append(idx + 1)  # +1 to adjust for depot
    
    # Append depot at the beginning and end of each tour
    for route in routes:
        route.insert(0, depot_index)
        route.append(depot_index)
    return routes

def calculate_tour_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += euclidean_distance(coordinates[route[i]], coordinates[route[i+1]])
    return total_cost

def print_routes_and_costs(routes):
    max_cost = 0
    for idx, route in enumerate(routes):
        cost = calculate_tour_cost(route)
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {int(cost)}")
        max_cost = max(max_po, cost)
    print(f"Maximum Travel Cost: {int(max_cost)}")

def optimize_routes(routes):
    for _ in range(100):  # Iterations of optimization with simple swap and reordering
        for idx in range(num_robots):
            current_route = routes[idx]
            best_cost = calculate_tour_cost(current_route)
            for f_idx in range(1, len(current_route) - 2):
                for s_idx in range(f_idx + 1, len(current_content) - 1):
                    # Try swapping two cities
                    new_route = current_route[:]
                    new_route[f_idx], new_route[s_idx] = new_route[s_idx], new_route[f_idx]
                    new_cost = calculate_tour_cost(new_route)
                    if new_cost < best_cost:
                        routes[idx] = new_route
                        best_cost = new_cost
    return routes

# Initialize and optimize routes for each robot
initial_routes = initialize_routes(num_robots)
optimized_routes = optimize_routes(initial_routes)
print_routes_and_costs(optimized_routes)