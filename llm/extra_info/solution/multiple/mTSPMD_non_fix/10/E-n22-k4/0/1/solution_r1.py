import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans
from itertools import permutations

# City coordinates
coordinates = np.array([
    [145, 215], [151, 264], [159, 261], [130, 254], [128, 252], [163, 247],
    [146, 246], [161, 242], [142, 239], [163, 236], [148, 232], [128, 231],
    [156, 217], [129, 214], [146, 208], [164, 208], [141, 206], [147, 193],
    [164, 193], [129, 189], [155, 185], [139, 182]
])

# Number of robots and their starting cities (depots)
num_robots = 4
depots = [0] * num_robots  # All starting at the depot city 0

# Function to compute Euclidean distance matrix
def compute_distance_matrix(coords):
    return distance_matrix(coords, coords)

# Solve the simplified Traveling Salesman Problem for small clusters
def solve_tsp(distances):
    n = len(distances)
    min_tour = None
    min_cost = float('inf')
    
    # Check all permutations for small number of cities
    for perm in permutations(range(1, n)):
        perm = [0] + list(perm)  # starting from the initial city (depot)
        cost = sum(distances[perm[i], perm[i + 1]] for i in range(n - 1))
        
        if cost < min_cost:
            min_cost = cost
            min_tour = perm
    
    return min_tour, min_cost

# Cluster cities into groups using K-Means
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(coordinates)
labels = kmeans.labels_

tours = []
costs = []
total_cost = 0

# Assign cities to robots based on clusters and solve TSP for those cities
for robot in range(num_robots):
    cluster_indices = np.where(labels == robot)[0]
    cluster_coords = coordinates[cluster_indices]
    dist_matrix = compute_distance_matrix(cluster_coords)
    
    if len(cluster_indices) > 1:
        tsp_tour, tsp_cost = solve_tsp(dist_matrix)
        complete_tour = [cluster_indices[i] for i in tsp_tour]
    else:
        complete_tour = [cluster_indices[0]]
        tsp_cost = 0
    
    tours.append(complete_tour)
    costs.append(tsp_cost)
    total_cost += tsp_cost

# Output resulting tours and costs
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {costs[robot]}")
print(f"Overall Total Travel Cost: {total_cost}")