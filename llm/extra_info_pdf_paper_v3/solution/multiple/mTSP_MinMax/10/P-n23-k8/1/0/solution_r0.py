import numpy as np

# Coordinates for each city including the depot
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Constants
NUM_ROBOTS = 8
DEPOT = 0

# Calculate Euclidean distance matrix
def distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                x_diff = cities[i][0] - cities[j][0]
                y_diff = cities[i][1] - cities[j][1]
                dist_matrix[i][j] = np.sqrt(x_diff ** 2 + y_diff ** 2)
    return dist_matrix

# Scipy can perform k-means clustering
from scipy.cluster.vq import kmeans2

def cluster_cities(num_clusters, cities):
    coords = np.array(cities[1:])  # exclude the depot for clustering
    centroids, labels = kmeans2(coords, num_clusters, minit='++')
    clusters = [[] for _ in range(num_clusters)]
    for i, label in enumerate(labels):
        clusters[label].append(i+1)  # i+1 to adjust index for city numbering (excluding depot)
    return clusters

# Simple implementation of a 2-opt swap to attempt to improve the routes
def two_opt(route, dist_matrix):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # neighboring edges; no change
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                if sum(dist_matrix[best[k-1], best[k]] for k in range(1, len(best))) > \
                   sum(dist_matrix[new_route[k-1], new_route[k]] for k in range(1, len(new_post))):
                    best = new_route
                    improved = True
        route = best
    return best

dist_mat = distance_matrix(cities)
clusters = cluster_cities(NUM_ROBOTS, cities)

tours = []
max_travel_cost = 0

for cluster in clusters:
    if not cluster:
        continue
    tour = [DEPOT] + cluster + [DEPOT]
    tour = two_opt(tour, dist_mat)  # Optimize using 2-opt
    tours.append(tour)

# Calculate travel costs
total_costs = []
for tour in tours:
    cost = sum(dist_mat[tour[i]][tour[i-1]] for i in range(1, len(tour)))
    total_costs.append(cost)
    print(f"Robot {tours.index(tour)} Tour: {tour}\nRobot {tours.index(tour)} Total Travel Cost: {cost}\n")

max_travel_cost = max(total_costs)
print(f"Maximum Travel Cost: {max_travel_cost}")