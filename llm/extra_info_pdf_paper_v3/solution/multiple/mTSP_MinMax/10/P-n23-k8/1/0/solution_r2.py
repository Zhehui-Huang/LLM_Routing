import numpy as np
from scipy.spatial.distance import cdist
from scipy.cluster.vq import kmeans2

# Coordinates for each city including the depot
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Calculate Euclidean distance matrix
def distance_matrix(cities):
    return cdist(cities, cities, metric='euclidean')

# Cluster cities using k-means, excluding the depot
def cluster_cities(cities, num_clusters):
    coords = np.array(cities[1:])  # Exclude depot
    _, labels = kmeans2(coords, num_clusters, minit='++')
    clusters = [[] for _ in range(num_clusters)]
    for i, label in enumerate(labels):
        clusters[label].append(i + 1)  # Correct index since cities[1:]
    return clusters

# Find a simple round trip tour for each cluster using the nearest neighbor heuristic
def nearest_neighbor_tour(cluster, dist_matrix):
    if not cluster:  # Empty cluster
        return [], 0
    tour = [0]  # Start at depot
    unvisited = set(cluster)
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda x: dist_matrix[current, x])
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(0)  # Return to depot
    cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    return tour, cost

# Number of robots and initializing tours and costs
NUM_ROBOTS = 8
dist_mat = distance_matrix(cities)
clusters = cluster_cities(cities, NUM_ROBOTS)
all_tours = []
all_costs = []

for cluster in clusters:
    tour, cost = nearest_neighbor_tour(cluster, dist_mat)
    all_tours.append(tour)
    all_costs.append(cost)

# Output the results
for i, (tour, cost) in enumerate(zip(all_tours, all_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

max_cost = max(all_costs)
print(f"Maximum Travel Cost: {max_cost}")