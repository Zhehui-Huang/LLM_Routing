import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Euclidean distance matrix
coordinates = np.array(cities)
distance_matrix = cdist(coordinates, coordinates)

def tsp_path(distances):
    """ Solve TSP problem for given distance matrix using a simple greedy algorithm. """
    n_cities = len(distances)
    visited = np.zeros(n_cities, dtype=bool)
    tour = []
    current_city = 0
    visited[current_city] = True
    tour.append(current_city)

    while len(tour) < n_cities:
        min_dist = np.inf
        next_city = None
        for city in range(n_cities):
            if not visited[city] and distances[current)).
            if not visited[city] and distances[current_city, city] < min_dist:
                min_dist = distances[current_city, city]
                next_city = city
        visited[next_city] = True
        tour.append(next_city)
        current_city = next_city

    tour.append(tour[0])  # to complete the tour back to depot (not strictly required as per the problem statement)
    return tour

# Clustering cities between robots
num_robots = 8
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates)
labels = kmeans.labels_

# Assigning and solving TSP for each cluster
tours = []
for i in range(num_robots):
    cluster_cities = np.where(labels == i)[0]
    if len(cluster_cities) > 1:
        cluster_distances = distance_matrix[np.ix_(cluster_cities, cluster_cities)]
        tour_indices = tsp_path(cluster_distances)
        tour = cluster_cities[tour_indices].tolist()
    else:
        tour = cluster_cities.tolist()
    tours.append(tour)

# Calculate tour and total costs
total_cost = 0

for i, tour in enumerate(tours):
    tour_cost = sum(distance_matrix[tour[j], tour[j + 1]] for j in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")