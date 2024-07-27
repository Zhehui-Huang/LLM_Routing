import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# City coordinates (excluding the depot city as a destination)
coordinates = [
    (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232),
    (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]
depot = (145, 215)

# Function to calculate the Euclidean distance between cities
def calc_distance(c1, c2):
    return euclidean(c1, c2)

# Initialize tours using K-means clustering
kmeans = KMeans(n_clusters=4, random_state=0).fit(coordinates)
labels = kmeans.labels_
clusters = {i: [] for i in range(4)}
for i, label in enumerate(labels):
    clusters[label].append(i + 1)  # city indices adjusted for 0-based index of depot

# Definition of a simple 2-opt algorithm for local optimization
def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if calc_tour_distance(new_route) < calc_tour_distance(best):
                    best = new_route
                    improved = True
        route = best
    return best

# Function to calculate the total distance of a tour
def calc_tour_distance(tour):
    total_dist = calc_distance(depot, coordinates[tour[0] - 1])
    for i in range(1, len(tour)):
        total_dist += calc_distance(coordinates[tour[i-1] - 1], coordinates[tour[i] - 1])
    total_dist += calc_distance(coordinates[tour[-1] - 1], depot)
    return total_dist

# Optimize each cluster using 2-opt
tours = {}
for robot_id, tour in clusters.items():
    tour = [0] + tour + [0]  # add depot at the start and the end
    optimized_tour = two_opt(tour)
    tours[robot_id] = optimized_tour

# Print tours and calculate costs
max_cost = 0
for robot_id, tour in tours.items():
    tour_cost = calc_tour_distance(tour[1:-1])  # exclude depot for cost calculation
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
    max_cost = max(max_cost, tour_cost)

print(f"Maximum Travel Course: {max_cost}")