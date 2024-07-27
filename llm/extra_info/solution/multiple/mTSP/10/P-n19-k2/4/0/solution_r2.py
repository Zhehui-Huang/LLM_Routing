import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Define the coordinates for the cities
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of cities and robots
num_cities = len(coordinates)
num_robots = 2

# Compute the distance matrix
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i, j] = euclidean(coordinates[i], coordinates[j])

# Classify the cities into 2 clusters using KMeans, excluding the depot city
kmeans = KMeans(n_clusters=num_robots, random_state=42)
labels = kmeans.fit_predict(coordinates[1:])  # Exclude the depot for clustering

# Assign cities to each robot based on cluster
robot_clusters = {i: [1 + idx for idx, label in enumerate(labels) if label == i] for i in range(num_robots)}

# Simple Nearest Neighbor TSP Solver
def nearest_neighbor_tsp(start_city, cities, dist_matrix):
    tour = [start_city]
    current_city = start_city
    total_cost = 0
    unvisited_cities = set(cities)

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: dist_matrix[current_city][x])
        total_cost += dist_matrix[current_city][next_city]
        tour.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city

    # Return to start
    tour.append(start_city)
    total_cost += dist_matrix[current_city][start_city]
    return tour, total_cost

# Compute the tours for each robot
overall_total_cost = 0
result = []

for i in range(num_robots):
    cities_to_visit = robot_clusters[i]
    if not cities_to_visit:
        continue  # No cities assigned to this robot
    tour, total_cost = nearest_neighbor_tsp(0, cities_to_visit, dist_matrix)
    overall_total_cost += total_cost
    result.append((i, tour, total_cost))

# Displaying the solution
for (robot, tour, cost) in result:
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travelagliari_costost: {overall_total_cost}")