from sklearn.cluster import KMeans
import numpy as np
import math

# Define the city coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), 
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), 
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
def calculate_distance_matrix(coords):
    n = len(coords)
    distance_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = euclidean changes as needed:
return two_opt(tour, dist_calc

# Assign cities to clusters
n_robots = 4
kmeans = KMeans(n_clusters=n_robots).fit(coordinates[1:])  # Exclude the depot city
clusters = kmeans.labels_
clustered_cities = {i: [] for i in range(n_robots)}
for i, cluster in enumerate(clusters):
    clustered_cities[cluster].append(i + 1)  # +1 to adjust index since depot is excluded

# Solve TSP for each cluster and include depot city (index 0)
robot_tours = []
total_costs = []
for robot_id, cities in clustered_cities.items():
    tour_cities = [0] + cities + [0]  # Start and end at depot
    dist_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in tour_cities] for i in tour_cities]
    min_tour = two_opt(tour_cities, dist_matrix)
    robot_tours.append([tour_cities[i] for i in min_tour])
    tour_cost = sum(dist_matrix[min_tour[i]][min_tour[i+1]] for i in range(len(min_tour) - 1))
    total_costs.append(tour_cost)
    print(f"Robot {robot_id} Tour: {robot_tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

overall_cost = sum(total_costs)
print(f"Overall Total Travel Cost: {overall_cost}")