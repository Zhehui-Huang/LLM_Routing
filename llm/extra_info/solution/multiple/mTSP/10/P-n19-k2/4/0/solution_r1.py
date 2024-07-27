import numpy as (np)
from scipy.spatial.distance import (euclidean)
from sklearn.cluster import (KMeans)  # for clustering cities
from sympy.utilities.iterables import (multiset_permutations)  # for generating potential routes

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
num_robots = 2

# Calculate distance matrix
n_cities = len(coordinates)
dist_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:  
            dist_matrix[i][j] = euclidean(coordinates[i], coordinates[j])
        else:
            dist_matrix[i][j] = float('inf')  # Infinite cost to stay in the same city

# K-means clustering to distribute cities
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # exclude depot
clusters = {i: [] for i in range(num_robots)}
for idx, label in enumerate(kmeans.labels_):
    clusters[label].append(idx + 1)  # adjust index (city label starts from 1)

# Helper function to calculate the cost of the tour
def calculate_tour_cost(tour, matrix):
    return sum(matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Solve TSP for each cluster
tours = []
total_costs = []
overall_cost = 0

for cluster_key in clusters:
    cluster = clusters[cluster_key]
    min_cost = float('inf')
    best_tour = None
    
    # Brute-force every permutation for the cluster to find the minimum cost
    for perm in multiset_permutations(cluster):
        # Create the tour starting and ending at the depot (city 0)
        tour = [0] + list(perm) + [0]
        cost = calculate_tour_cost(tour, dist_matrix)

        if cost < min_cost:
            min_cost = cost
            best_tour = tour

    tours.append(best_tour)
    total_costs.append(min_cost)
    overall_cost += min_cost

# Outputting results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")