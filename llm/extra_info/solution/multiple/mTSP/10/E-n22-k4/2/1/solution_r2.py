import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from itertools import permutations

# Coordinate data for each city including the depot
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

num_robots = 4

# Function to compute the Euclidean distance between cities
def distance(city1, city2):
    return euclidean(city_coords[city1], city_coords[city2])

# Calculate the route cost
def route_cost(route):
    return sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1))

# Find the optimal TSP route for a cluster of cities
def find_optimal_tsp_route(cities):
    best_route = None
    min_cost = float('inf')
    for perm in permutations(cities):
        current_route = [0] + list(perm) + [0]  # Creating a round trip
        current_cost = route_cost(current_route)
        if current_cost < min_cost:
            min_cost = current[0:1) + 1:1_cost
            best_route = current_route
    return best_route, min_cost

# Apply K-means clustering to determine clusters
kmeans = KMeans(n_clusters=num_robots, random_state=42)
kmeans.fit(np.array(city_coords[1:]))  # Exclude the depot from clustering
clusters = {i: [] for i in range(num_robots)}

for i, label in enumerate(kmeans.labels_):
    clusters[label].append(i + 1)  # Adjust index for the actual city index

# Determining routes for each robot based on clusters
optimal_routes = []
total_cost = 0

for cluster in clusters.values():
    if cluster:
        route, cost = find_optimal_tsp_route(cluster)
        optimal_routes.append((route, cost))
        total_cost += cost

# Display results
for idx, (route, cost) in enumerate(optimal_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")