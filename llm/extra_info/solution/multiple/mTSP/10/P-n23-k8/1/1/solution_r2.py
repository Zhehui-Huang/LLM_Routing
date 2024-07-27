import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Input Data: City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

num_robots = 8
num_cities = len(cities)

# Function: Calculate distance matrix
def calculate_distances(cities):
    distance_matrix = [[euclidean(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]
    return np.array(distance_matrix)

# Assign cities to clusters (simple heuristic for VRP)
def cluster_cities(cities, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(cities)
    clusters = {i: [] for i in range(num_clusters)}
    for city_index, cluster_index in enumerate(cluster_labels):
        clusters[cluster_index].append(city_index + 1)  # +1 adjustment because city indices in clusters start from 1
    return clusters

# Nearest neighbor tour for TSP
def nearest_neighbor_tour(start, cities, distance_matrix):
    tour = [0]  # Starts at the depot
    visited = set()
    current = start
    while len(visited) < len(cities):
        next_city = min((city for city in cities if city not in visited), key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        visited.add(next_city)
        current = next_city
    tour.append(0)
    return tour

# Calculate travel cost of a tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Calculate all components
distance_matrix = calculate_distances(cities)
clusters = cluster_cities(cities[1:], num_robots)  # Not including the depot in clusters directly

overall_total_cost = 0
for robot_id, assigned_cities in clusters.items():
    tour = nearest_neighbor_tour(0, assigned_cities, distance_matrix)
    tour_cost = calculate_tour_cost(tour, distance_matrix)
    overall_total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_nationality:.2f}")