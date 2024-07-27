import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
import itertools

# Coordinates of the cities including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

# Calculate Euclidean distance between each pair of cities
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

# Perform the clustering (as an approximation of fuzzy c-means)
def initial_clustering(coords, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42).fit(coords)
    clusters = [[] for _ in range(num_clusters)]
    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(idx)
    return clusters

distance_matrix = calculate_distance_matrix(coordinates)

# Initial Clusters (using simple KMeans)
clusters = initial_clustering(coordinates[1:], num_robots)  # Exclude depot from clustering

def find_tour_for_cluster(cluster, depot=0):
    # Simple nearest neighbor tour heuristic
    tour = [depot]
    unvisited = set(cluster)
    current = depot
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(depot)
    return tour

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i+1]]
    return cost

# Finding tours and calculating costs
tours = []
costs = []

for cluster in clusters:
    tour = find_tour_for_cluster(cluster)
    cost = calculate_tour_cost(tour)
    tours.append(tour)
    costs.append(cost)

# Output the result
max_cost = max(costs)
for i in range(len(tours)):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")