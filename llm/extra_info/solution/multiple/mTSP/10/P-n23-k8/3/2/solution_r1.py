import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Cities and their coordinates
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Calculate the distance matrix
n_cities = len(city_coords)
dist_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        dist_matrix[i][j] = euclidean(city_coords[i], city_coords[j])

# Clustering cities into k clusters (one for each robot)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_coords)
labels = kmeans.labels_

# Function to compute the TSP tour using the nearest neighbor heuristic
def tsp_tour(start_city, cities):
    tour = [start_city]
    current_city = start_city
    unvisited_cities = set(cities)
    if start_city in unvisited_cities:
        unvisited_cities.remove(start_city)

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: dist_matrix[current_city][x])
        tour.append(next_city)
        current_city = next_city
        unvisited_cities.remove(current_city)

    tour.append(start_city)  # return to the starting city
    return tour

# Calculate the TSP for each robot based on its cluster
robots_tours = []
overall_cost = 0
start_index = 0  # Depot city index

for robot_id in range(num_robots):
    cluster_cities = [i for i, label in enumerate(labels) if label == robot_id]
    if start_index in cluster_cities:
        cluster_cities.remove(start_index)
    if cluster_cities:  # Check if the cluster is non-empty
        tour = tsp_tour(start_index, [start_index] + cluster_cities)
        tour_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        robots_tours.append((robot_id, tour, tour_cost))
        overall_cost += tour_cost
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")