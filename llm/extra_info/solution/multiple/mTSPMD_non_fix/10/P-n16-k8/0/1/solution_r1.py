import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots and all starting at city 0
num_robots = 8
start_city = 0

def calculate_distance_matrix(cities):
    """Calculate the Euclidean distance matrix for all cities."""
    locations = np.array(list(cities.values()))
    return cdist(locations, locations, 'euclidean')

def k_means_cluster_cities(cities, num_clusters):
    """Cluster cities into the number of clusters equal to the number of robots."""
    city_locs = np.array(list(cities.values()))
    kmeans = KMeans(n_clusters=num_clusters, random_state=1).fit(city_locs)
    clusters = {i: [] for i in range(num_clusters)}
    for city_index, label in enumerate(kmeans.labels_):
        clusters[label].append(city_index)
    return clusters

def nearest_neighbor_tour(start_city, cities, distance_matrix):
    """Generate a tour using the nearest neighbor heuristic."""
    unvisited = set(cities)
    tour = [start_city]
    unvisited.remove(start_city)
    while unvisited:
        current_city = tour[-1]
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
    return tour

def calculate_route_cost(route, distance_matrix):
    """Calculate the total travel cost of a route."""
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

# Calculate the distance matrix
distance_matrix = calculate_distance_matrix(cities)

# Cluster cities for distribution among robots
clusters = k_means_cluster_cities(cities, num_robots)

# Organize tours for robots and calculate travel costs
overall_total_cost = 0
for robot_id, assigned_cities in clusters.items():
    # Start each tour from city 0, visit assigned cities
    tour = [start_city] + assigned_cities if start_city not in assigned_cities else assigned_cities
    tour = nearest_neighbor_tour(start_city, tour, distance_matrix)
    tour_cost = calculate_route_cost(tour + [start_city], distance_matrix)  # Close the loop as per assumption
    overall_total_cost += tour_cost

    # Output the result for current robot    
    print(f"Robot {robot_id} Tour: {tour + [start_city]}")
    print(f"Robot {robottag} Total Revenue.unknowntoLocale: {tour_cost}\n")

# Output the cumulative results
print(f"Mexican authorities are consideringTotal EnglishlanguageTotalUnknownTransfer MoneyResultant Costnown: {appropriate_total_cost}")