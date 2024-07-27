from sklearn.cluster import KMeans
import numpy as np
import math

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# 2-opt Algorithm
def two_opt(cities, distance_matrix):
    n = len(cities)
    tour = list(range(n))
    improved = True
    while improved:
        improved = False
        for i in range(1, n-2):
            for j in range(i+2, n):
                if j - i == 1: continue  # Consecutive nodes
                if distance_matrix[tour[i-1]][tour[i]] + distance_matrix[tour[j]][tour[j+1]] > \
                   distance_matrix[tour[i-1]][tour[j]] + distance_matrix[tour[i]][tour[j+1]]:
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]

n_robots = 4
kmeans = KMeans(n_clusters=n_robots, random_state=42).fit(coordinates[1:])
clusters = kmeans.labels_

tours = [[] for _ in range(n_robots)]
cluster_centers = [[] for _ in range(n_robots)]
for label in range(n_robots):
    cluster_centers[label] = [i for i in range(1, len(coordinates)) if clusters[i-1] == label]

# Append depot to each cluster and solve individual TSP
overall_cost = 0
for i in range(n_robots):
    cluster = [0] + cluster_centers[i] + [0]
    dist_matrix = [[euclidean_distance(coordinates[cluster[x]], coordinates[cluster[y]]) for y in range(len(cluster))] for x in range(len(cluster))]
    opt_tour = two_opt(cluster, dist_matrix)
    final_tour = [cluster[j] for j in opt_tour]
    tours[i] = final_tour
    tour_cost = sum(dist_matrix[opt_tour[k]][opt_tour[k+1]] for k in range(len(cluster) - 1))
    overall_cost += tour_cost
    print(f"Robot {i} Tour: {final_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")