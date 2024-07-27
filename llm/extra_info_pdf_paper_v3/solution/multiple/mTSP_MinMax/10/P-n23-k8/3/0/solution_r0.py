import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# City coordinates
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

n_robots = 8
depot = city_coords[0]
cities = city_coords[1:]  # Excluding the depot

# Step 1: Initialize clusters for initial solution
kmeans = KMeans(n_clusters=n_robots, random_state=0).fit(cities)
labels = kmeans.labels_

# Assign cities to robots based on clusters
robot_routes = {i: [] for i in range(n_robots)}
for city_index, label in enumerate(labels):
    robot_routes[label].append(city_index + 1)  # +1 because city indices are offset by depot

# Calculate distance matrix
def distance_matrix(coords):
    size = len(coords)
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(i + 1, size):
            dist = euclidean(coords[i], coords[j])
            matrix[i][j] = matrix[j][i] = dist
    return matrix

dist_matrix = distance_matrix(city_coords)

# Function to calculate the cost of a tour
def tour_cost(tour, dist_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += dist_matrix[tour[i]][tour[i + 1]]
    return cost

# Prepare initial tours including the depot
initial_tours = {}
for robot_id, cities in robot_routes.items():
    tour = [0] + cities + [0]
    initial_tours[robot_id] = tour

# Step 2: Initial improvement using 2-opt
def two_opt(tour, dist_matrix):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Consecutive nodes
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if tour_cost(new_tour, dist_matrix) < tour_cost(best, dist_matrix):
                    best = new_tour
                    improved = True
        tour = best
    return best

for robot_id, tour in initial_tours.items():
    initial_tours[robot_id] = two_opt(tour, dist_matrix)

# Calculate the costs and determine the maximum
max_cost = 0
for robot_id, tour in initial_tours.items():
    cost = tour_cost(tour, dist_matrix)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
    if cost > max_cost:
        max_cost = cost

print(f"Maximum Travel Cost: {max_cost}")