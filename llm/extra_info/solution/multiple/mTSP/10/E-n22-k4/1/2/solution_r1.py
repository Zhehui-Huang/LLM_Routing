import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Coordinates of cities including the depot
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

# Function to compute Euclidean distance matrix
def distance_matrix(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean(cities[i], cities[j])
    return distances

# Function to compute a tour using the nearest neighbor approach starting from the depot
def nearest_neighbor_tour(start, cities_to_visit, dist_matrix):
    tour = [start]
    current = start
    while cities_to_visit:
        next_city = min(cities_to_visit, key=lambda x: dist_matrix[current][x])
        tour.append(next_city)
        cities_to_visit.remove(next_city)
        current = next_city
    tour.append(start) # complete the loop back to depot
    return tour

# Creating and computing distance matrix
dist_matrix = distance_matrix(cities)

# KMeans to assign cities to each robot
city_indices = list(range(1, len(cities)))  # Exclude the depot which is at index 0
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(np.array(cities)[city_indices])
labels = kmeans.labels_

# Organizing cities per robot
robot_tours = {i: [] for i in range(num_robots)}
for idx, label in enumerate(labels):
    robot_tours[label].append(city_indices[idx])

# Compute tours for each robot
total_cost = 0
for robot_id in range(num_robots):
    tour = nearest_neighbor_tour(0, robot_tours[robot_id], dist_matrix)
    tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
print(f"Overall Total Travel Cost: {total_cost}")