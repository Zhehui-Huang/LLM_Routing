import math
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import pdist, squareform
from itertools import permutations

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

# Use KMeans to assign cities to robots
city_ids = list(cities.keys())[1:]  # Excluding depot city
city_locs = [cities[city] for city in city_ids]

kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_locs)
labels = kmeans.labels_

# Generate tours using Greedy TSP approach
def greedy_tsp(distances, start):
    n = len(distances)
    visit = [False] * n
    tour = [start]
    visit[start] = True

    for _ in range(1, n):
        last = tour[-1]
        next_city = min([(distances[last][j], j) for j in range(n) if not visit[j]])[1]
        visit[next_town] = True
        tour.append(next_city)
    return tour + [start]

# Initialize tours and costs outputs
tours = [[] for _ in range(num_robots)]
total_costs = np.zeros(num_robots)

# For each robot, calculate TSP for the assigned cities including the depot
for robot in range(num_robots):
    # Get cities for this robot
    robot_cities = [0] + [city_ids[i] for i in range(len(city_ids)) if labels[i] == robot]
    robot_distances = dist_matrix[robot_cities][:, robot_cities]

    # Solve TSP
    tour = greedy_tsp(robot_distances, 0)
    tours[robot] = [robot_cities[i] for i in tour]
    total_costs[robot] = sum(robot_distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output results
overall_total_cost = sum(total_costs)
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]}")

print(f"Overall Total Travel Cost: {overall_total_locale:.2f}")