import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Helper function to calculate the cost of a tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# 2-opt optimization for a single tour
def two_opt(tour, distance_matrix):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1:
                    continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour, distance_matrix) < calculate_tour_cost(best, distance_matrix):
                    best = new_tour
                    improved = True
                    break
            if improved:
                break
    return best

# City coordinates
cities = np.array([
    [30, 40], [37, 52], [49, 49], [52, 64], [31, 62], [52, 33], [42, 41], [52, 41], 
    [57, 58], [62, 42], [42, 57], [27, 68], [43, 67], [58, 48], [58, 27], [37, 69], 
    [38, 46], [61, 33], [62, 63], [63, 69], [45, 35]
])

# Calculate the distance matrix
distance_matrix = cdist(cities, cities, metric='euclidean')

# KMeans clustering to partition the cities among robots
kmeans = KMeans(n_clusters=2, random_state=42).fit(cities[1:])  # Excluding the depot city
labels = kmeans.labels_

# Assign cities to robots
robot_routes = {0: [0], 1: [0]}  # Starting at the depot
for idx, label in enumerate(labels):
    robot_routes[label].append(idx + 1)  # Adding 1 because cities in labels start from 1

# Add the depot city to the end of the tour
for robot_id in robot_routes:
    robot_routes[robot_id].append(0)

# Optimizing tours using the 2-opt algorithm
optimized_tours = {}
overall_cost = 0

for robot_id in robot_routes:
    optimized_route = two_opt(robot_routes[robot_id], distance_matrix)
    optimized_tours[robot_id] = optimized_route
    tour_cost = calculate_tour_cost(optimized_route, distance_matrix)
    overall_cost += tour_cost
    print(f"Robot {robot_id} Tour: {optimized_route}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")