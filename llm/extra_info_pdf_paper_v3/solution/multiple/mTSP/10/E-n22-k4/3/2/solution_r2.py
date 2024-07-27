import numpy as np
from scipy.spatial.distance import euclidean
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans
import itertools

# Cities coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Number of robots
num_robots = 4

# Creating the distance matrix
city_points = np.array(list(cities.values()))
dist_matrix = distance_matrix(city_points, city_points)

# K-means to cluster cities into routes for robots
kmeans = KMeans(n_clusters=num_robots, random_state=0)
clusters = kmeans.fit_predict(city_points[1:]) # Exclude depot

def calc_tour_cost(tour):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Allocate cities based on clusters, starting tours for each robot with the depot
robot_tours = {i: [0] for i in range(num_robots)}

for i, cluster_id in enumerate(clusters, start=1):
    robot_tours[cluster_id].append(i)

# Each robot returns to the depot after the tour
for tour in robot_tours.values():
    tour.append(0)

# Calculate tour costs
robot_costs = {robot: calc_tour_cost(tour) for robot, tour in robot_tours.items()}
overall_cost = sum(robot_costs.values())

# Output results
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {robot_tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {robot_costs[robot]:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")