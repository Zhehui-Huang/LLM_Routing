import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Coordinates of cities including the depot (index 0)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Calculate distance matrix
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i, j] = euclidean(coords[i], coords[j])
    return distance_matrix

distance_matrix = calculate_distance_matrix(coordinates)

# KMeans clustering to assign cities to 4 robots
kmeans = KMeans(n_clusters=4, random_state=0).fit(coordinates[1:])  # Ignore depot for clustering
city_clusters = kmeans.labels_

# Nearest neighbor TSP solution for each cluster
def nearest_neighbor_tsp(distances, start_point):
    num_points = len(distances)
    unvisited = set(range(num_points))
    unvisited.remove(start_point)
    tour = [start_point]
    current_point = start_point

    while unvisited:
        next_point = min(unvisited, key=lambda x: distances[current_point][x])
        tour.append(next_point)
        unvisited.remove(next_point)
        current_point = next_point

    tour.append(start_point)  # Return to start
    return tour

# Calculate the travel cost for a given tour
def calculate_tour_cost(tour, distance_matrix):
    total = 0
    for i in range(len(tour) - 1):
        total += distance_matrix[tour[i]][tour[i + 1]]
    return total

# Generate results
overall_total_cost = 0
print("Detailed Robot Tours and Costs:")
for i in range(4):
    cities_in_cluster = [0] + [idx + 1 for idx, cluster in enumerate(city_clusters) if cluster == i]
    tour = nearest_neighbor_tsp(distance_matrix[np.ix_(cities_in_cluster, cities_in_cluster)], 0)
    real_tour = [cities_in_cluster[j] for j in tour]
    tour_cost = calculate_tour_cost(real_tour, distance_matrix)
    overall_total_cost += tour_cost
    print(f"Robot {i} Tour: {real_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_ cost:.2f}")