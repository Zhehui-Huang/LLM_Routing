import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# City coordinates, including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Parameters
num_robots = 4
depot_index = 0

# Helper function: Calculate the Euclidean distance
def calculate_distance(i, j):
    return np.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Simple function to create a tour using the nearest neighbor heuristic
def nearest_neighbor_tour(start, points):
    unvisited = set(points)
    tour = [start]
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda x: calculate_distance(current, x))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)  # return to depot
    return tour

# Function to calculate the total travel cost of a tour
def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Cluster the cities (excluding the depot)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # we offset by 1 to exclude depot
clusters = kmeans.labels_

# Assign cities to each robot based on clusters
robot_tours = [[] for _ in range(num_robots)]
for idx, cluster_id in enumerate(clusters, start=1):  # offset index as we excluded depot earlier
    robot_tours[cluster_id].append(idx)

# Creating a tour for each robot and calculate the cost
max_cost = 0
for robot_id, tour_cities in enumerate(robot_tours):
    if not tour_cities:
        print(f"Robot {robot_id} Tour: [0, 0]")
        print(f"Robot {robot_id} Total Travel Cost: 0")
    else:
        tour = nearest_neighbor_tour(depot_index, tour_cities)
        cost = calculate_tour_cost(tour)
        max_cost = max(max_cost, cost)
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {cost}")

# Print the maximum cost amongst all robots
print(f"Maximum Travel Cost: {max_cost}")