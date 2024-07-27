import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Define cities and coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots and start location
num_robots = 8
start_city = 0  # All robots start from city 0

def calculate_distance_matrix(cities):
    """Calculate the Euclidean distance matrix for all cities."""
    locations = list(cities.values())
    return cdist(locations, locations, metric='euclidean')

def k_means_cluster_cities(cities, num_clusters):
    """Cluster cities into the number of clusters equal to the number of robots."""
    locations = list(cities.values())
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(locations)
    clusters = {i: [] for i in range(num_clusters)}
    for city_index, label in enumerate(kmeans.labels_):
        clusters[label].append(city_index)
    return clusters

def nearest_neighbor_tour(start, cities, distance_matrix):
    """Construct a tour using the nearest neighbor heuristic starting from a given city."""
    tour = [start]
    unvisited = set(cities) - {start}
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda city: distance_matrix[current, city])
        tour.append(next_city)
        unvisited.remove(next_city)
    return tour

def total_tour_cost(tour, distance_matrix):
    """Calculate the total travel cost of a tour."""
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Compute distance matrix
distance_matrix = calculate_distance_matrix(cities)

# Cluster cities for initial allocation to robots
clusters = k_means_cluster_cities(cities, num_robots)

# Compute tours and costs for each robot
overall_total_cost = 0
for robot_id, cluster in clusters.items():
    tour = nearest_neighbor_tour(start_city, cluster, distance_matrix)
    tour.append(start_city)  # assuming they return to the start; remove if not necessary
    cost = total_tour_cost(tour, distance_matrix)
    overall_total_cost += cost
    
    # Output results for this robot
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}\n")

# Output the cumulative total cost
print(f"Overall Total Travel Cost: {overall_total_cost}")