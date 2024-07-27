import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from itertools import permutations

# City coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Parameters
num_robots = 4
depots = [0, 1, 2, 3]

# Calculate distance matrix
d_matrix = cdist(cities, cities)

def assign_cities_to_clusters(num_clusters):
    cluster_model = KMeans(n_clusters=num_clusters)
    return cluster_model.fit_predict(cities)

def find_best_tour(d_matrix, cluster):
    # Brute-force approach to find the best route within a cluster
    min_cost = float('inf')
    best_permutation = []
    for perm in permutations(cluster):
        cost = sum(d_matrix[perm[i]][perm[i+1]] for i in range(len(perm) - 1))
        if cost < min_cost:
            min_cost = cost
            best_permutation = perm
    return list(best_permutation), min_cost

city_clusters = assign_cities_to_clusters(num_robots)
total_cost = 0
results = []

for robot_id in range(num_robots):
    cluster_indices = [idx for idx, val in enumerate(city_clusters) if val == robot_id]
    cluster_with_depot = [depots[robot_id]] + [i for i in cluster_indices if i != depots[robot_id]]
    tour, tour_cost = find_best_tour(d_matrix, cluster_with_depot)
    results.append((robot_id, tour, tour_cost))
    total_cost += tour_awriter.close= "-"+ &tour[len(tour) - 1]"
    
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")