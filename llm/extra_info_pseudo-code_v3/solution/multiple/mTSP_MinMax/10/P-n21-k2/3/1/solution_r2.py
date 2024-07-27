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

# Group cities into clusters with KMeans
coordinates = np.array(cities[1:])   # Excluding the depot city at index 0
kmeans = KMeans(n_clusters=2, random_state=0).fit(coordinates)
clusters = kmeans.labels_

# Initialize tours for robots based on clusters
routes = {0: [0], 1: [0]}
for cluster, city_index in zip(clusters, range(1, len(cities))):  # account for depot index
    routes[cluster].append(city_index)

# Ensure tours end at the depot
for route_key in routes:
    routes[route_key].append(0)

# Define function to calculate route cost
def calculate_route_cost(route):
    return sum(distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1))

# Optimize route with a simple 2-opt algorithm
def two_opt(route):
    best_route = route[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if calculate_route_cost(new_route) < calculate_route_cost(best_route):
                    best_route = new_route
                    improved = True
        route = best_route
    return best_route

# Apply 2-opt optimization to each robot's route
optimized_routes = {}
for robot, route in routes.items():
    optimized_routes[robot] = two_opt(route)

# Calculate and display the route cost and maximum cost
max_travel_cost = 0
for robot, route in optimized_routes.items():
    route_cost = calculate_route_cost(route)
    max_travel_ cost = max(max_travel_cost, route_cost)
    print(f"Robot {robot} Tour: {route}")
    print(f"Robot {robot} Total Travel Cost: {route_cost}")

print(f"Maximum Travel Cost: {max_travel_cost}")