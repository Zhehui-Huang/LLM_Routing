import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import MiniBatchKMeans
from itertools import permutations

# Cities and coordinates
coordinates = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
])

# Function to calculate Euclidean Distance
def calculate_distance_matrix(coords):
    n_cities = len(coords)
    dist_matrix = np.zeros((n_cities, n_cities))
    for i in range(n_cities):
        for j in range(n_cities):
            dist_matrix[i, j] = euclidean(coords[i], coords[j])
    return dist_matrix

distance_matrix = calculate_distance_matrix(coordinates)

# Number of robots
num_robots = 4

# Clustering cities into number of robots groups
kmeans = MiniBatchKMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])
clusters = kmeans.labels_

# Assign tours to each robot
robot_tours = {i: [0] for i in range(num_robots)}  # start from Depot
for city in range(1, len(coordinates)):
    robot_tours[clusters[city-1]].append(city)

# Append the depot city at the end of each tour
for tour in robot_tours.values():
    tour.append(0)

# Function to calculate total travel cost of a tour
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Calculate costs for each robot
tour_costs = {}
for k in range(num_robots):
    tour_costs[k] = calculate_tour_cost(robot_tours[k], distance_matrix)

# Find maximum travel cost
max_travel_cost = max(tour_costs.values())

# Output
for k in range(num_robots):
    print(f"Robot {k} Tour: {robot_tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_costs[k]:.2f}")

print(f"Maximum Travel Cost: {max_travel_cost:.2f}")