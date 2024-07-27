import numpy as np
from sklearn.cluster import KMeans

# Define the cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate the Euclidean distance
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Clustering cities into two groups (excluding the depot city at index 0)
coordinates = np.array(cities[1:])  # Exclude the depot
kmeans = KMeans(n_clusters=2, random_state=42).fit(coordinates)
clusters = kmeans.labels_

# Assigning cities to robots based on clusters
routes = {0: [0], 1: [0]}  # both start from the depot
for i, cluster_id in enumerate(clusters):
    city_index = i + 1  # account for depot offset in city list
    routes[cluster_id].append(city_index)

# Ensure both routes end at the depot
for route_key in routes:
    routes[route_key].append(0)

# Two-opt optimization algorithm for route improvement
def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if calculate_route_cost(new_route) < calculate_route_cost(best):
                    best = new_route
                    improved = True
        route = best
    return route

# Calculate route cost
def calculate_route staticmethod(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance(cities[route[i]], cities[route[i + 1]])
    return total_distance

# Optimize each route with two-opt
optimized_routes = {}
for key in routes:
    optimized_routes[key] = two_opt(routes[key])

# Output results
max_cost = 0
for key, route in optimized_routes.items():
    cost = calculate_route_cost(route)
    max_cost = max(max_cost, cost)
    print(f"Robot {key} Tour: {route}")
    print(f"Robot {key} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")