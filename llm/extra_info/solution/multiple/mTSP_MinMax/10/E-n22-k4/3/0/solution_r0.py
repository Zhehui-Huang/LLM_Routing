import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans
import itertools

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

def calculate_distance(coord1, coord2):
    return np.hypot(coord1[0] - coord2[0], coord1[1] - coord2[1])

# Number of robots and cities
num_robots = 4
num_cities = len(coordinates)

# Calculate Distance Matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Clustering cities (excluding the depot)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])
labels = kmeans.labels_

def two_opt(route, distance_matrix):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # Consecutive nodes; no need to swap
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]  # Reverse the segment
                if np.sum(distance_matrix[new_route, np.roll(new_path, -1)]) < np.sum(distance_matrix[best, np.roll(best, -1)]):
                    best = new_route
                    improved = True
        route = best
    return best

tours = []
max_travel_cost = 0

# Generating tours for each robot
for robot in range(num_robots):
    # Cities for current robot
    current_cities = [i + 1 for i in range(num_cities - 1) if labels[i] == robot]
    complete_tour = [0] + current_cities + [0]  # Add the depot city

    # Performing 2-opt TSP optimization
    optimized_tour = two_opt(complete_tour, dist_matrix)
    tours.append(optimized_tour)
    tour_cost = np.sum(dist_matrix[optimized_tour[:-1], optimized_tour[1:]])
    max_travel_cost = max(max_travel_cost, tour_cost)
    print(f"Robot {robot} Tour: {optimized_tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Cost: {max_travel_var_cost}")