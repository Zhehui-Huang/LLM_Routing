import numpy as np
from math import sqrt
from sklearn.cluster import KMeans

# Coordinates of cities including the depot
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots and starting city for robots
num_robots = 8
depot = cities[0]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Creating a distance matrix
def create_distance_matrix(cities):
    size = len(cities)
    dist_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return dist_matrix

distance_matrix = create_distance_matrix(cities)

# Assign cities to robots using k-means clustering
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(cities)
labels = kmeans.labels_

# Simple nearest neighbor tour for clusters
def nn_tour(start, cities, dist_matrix):
    tour = [start]
    unvisited = set(cities)
    unvisited.remove(start)
    
    current = start
    while unvisited:
        nearest = min(unvisited, key=lambda city: dist_matrix[current, city])
        tour.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    tour.append(start)  # return to depot
    return tour

overall_cost = 0
robot_tours = []

for r in range(num_robots):
    cluster_cities = [i for i in range(len(cities)) if labels[i] == r]
    if not cluster_cities:
        continue
    cluster_cities_indices = [0] + [c for c in cluster_cities if c != 0]  # include depot
    tour = nn_tour(0, cluster_cities_indices, distance_matrix)
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    robot_tours.append((tour, tour_cost))
    overall_cost += tour_cost
    
    # Output each robot's tour and cost
    print(f"Robot {r} Tour: {tour}")
    print(f"Robot {r} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")