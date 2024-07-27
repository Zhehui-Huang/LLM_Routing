import math
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import pdist, squareform

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of robots
num_robots = 2

# Calculate Euclidean distance matrix
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

dist_matrix = np.zeros((19, 19))
for i in range(19):
    for j in range(19):
        dist_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# Cluster cities by using KMeans to roughly divide work among robots
city_ids = list(cities.keys())[1:]  # Excluding depot
city_locs = [cities[city] for city in city_ids]

kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_locs)
labels = kmeans.labels_

# Define a simple TSP solution through a Greedy method (nearest neighbor)
def greedy_tsp(distances, start):
    n = len(distances)
    visited = [False] * n
    tour = [start]
    visited[start] = True

    while len(tour) < n:
        last = tour[-1]
        next_city = min([(distances[last][j], j) for j in range(n) if not visited[j]])
        tour.append(next_city[1])
        visited[next_city[1]] = True

    return tour

# Preparing tours per robot
robots_tours = [[] for _ in range(num_robots)]
total_costs = [0 for _ in range(num_robots)]

for robot in range(num_robots):
    # Gather cities covered by current robot
    robot_cities = [0]  # Depot
    robot_cities.extend([city for i, city in enumerate(city_ids) if labels[i] == robot])
    robot_distances = dist_matrix[robot_cities, :][:, robot_cities]

    # Find tour starting from the depot
    tour = greedy_tsp(robot_distances, 0)
    actual_tour = [robot_cities[idx] for idx in tour]

    # Close the loop to depot
    actual_tour.append(0)
    robots_tours[robot] = actual_tour

    # Calculate the total travel cost for this tour
    for idx in range(len(actual_tour) - 1):
        total_costs[robot] += euclidean_distance(cities[actual_tour[idx]], cities[actual_tour[idx+1]])

# Output the results
overall_total_cost = sum(total_costs)
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {robots_tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")