import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
import random

# Define city coordinates
cities = np.array([
    [30, 40], [37, 52], [49, 43], [52, 64], [31, 62], 
    [52, 33], [42, 41], [52, 41], [57, 58], [62, 42], 
    [42, 57], [27, 68], [43, 67], [58, 27], [37, 69], 
    [61, 33], [62, 63], [63, 69], [45, 35]
])

# Functions
def calculate_distance_matrix(cities):
    return cdist(cities, cities)

def calculate_route_cost(route, distance_matrix):
    return sum(distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))

def two_opt(route, distance_matrix):
    best_cost = calculate_route_cost(route, distance_matrix)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                if j - i == 1: continue  # Skip neighbors
                new_route = route[:]
                new_route[i:j + 1] = new_route[j:i - 1:-1]  # Reverse segment
                new_cost = calculate_route_cost(new_route, distance_matrix)
                if new_cost < best_cost:
                    route = new_route
                    best_cost = new_cost
                    improved = True
    return route

# Number of robots
num_robots = 2

# Initial clustering using KMeans (approximation to FCM)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities[1:])
cluster_labels = kmeans.labels_

# Assign cities to robots
robot_tours = {i: [0] for i in range(num_robots)}
for city_index, label in enumerate(cluster_labels, start=1):
    robot_tours[label].append(city_index)

# Closing each tour back to the depot
for i in range(num_robots):
    robot_tours[i].append(0)

# Calculate initial cost
distance_matrix = calculate_distance_matrix(cities)
costs = [calculate_route_cost(robot_tours[i], distance_matrix) for i in range(num_robots)]

# Apply two_opt improvement on each tour
optimized_tours = {i: two_opt(robot_tours[i], distance_matrix) for i in range(num_robots)}
optimized_costs = [calculate_route_cost(optimized_tours[i], distance_matrix) for i in range(num_robots)]

# Outputting the results
max_cost = max(optimized_costs)
for i in range(num_robots):
    print(f"Robot {i} Tour: {optimized_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {optimized_costs[i]}")
print(f"Maximum Travel Cost: {max_cost}")