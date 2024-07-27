import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans
import random

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Calculate distance matrix
distance_matrix = distance_matrix(coordinates, coordinates)

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def initialize_clusters(n_clusters, coordinates):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(coordinates)
    return kmeans.labels_

def assign_cities_to_robots(labels, n_robots):
    tours = [[] for _ in range(n_robots)]
    for i, label in enumerate(labels):
        tours[label].append(i+1)  # we skip the depot which is indexed as 0
    return tours

def optimize_tour(tour):
    # Simple optimization using a greedy strategy
    current_location = 0
    optimized_tour = [0]
    unvisited = set(tour)
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current_location][x])
        optimized_tour.append(next_city)
        unvisited.remove(next_city)
        current_location = next_city
    optimized_tour.append(0)
    return optimized_tour

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour)-1):
        cost += distance_matrix[tour[i]][tour[i+1]]
    return cost

# Cluster the cities and initialize the tours
labels = initialize_clusters(num_robots, coordinates[1:]) # skip depot
initial_tours = assign_cities_to_robots(labels, num_robots)

# Optimize each tour and calculate the costs
final_tours = []
costs = []
for tour in initial_tours:
    optimized_tour = optimize_tour(tour)
    cost = calculate_tour_cost(optimized_tour)
    final_tours.append(optimized_tour)
    costs.append(cost)

# Results
max_cost = max(costs)
for i, tour in enumerate(final_tours):
    print(f'Robot {i} Tour: {tour}')
    print(f'Robot {i} Total Travel Cost: {costs[i]}')

print(f'Maximum Travel Cost: {max_cost}')