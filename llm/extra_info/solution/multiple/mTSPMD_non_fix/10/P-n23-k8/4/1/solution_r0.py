import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Number of robots and their depots
num_robots = 8
depots = [0] * num_robots

# Calculate distances matrix
n_cities = len(cities)
distances = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distances[i][j] = euclidean(cities[i], cities[j])

# Cluster cities around the depots
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities)
labels = kmeans.labels_

# Assign tours to robots
tours = [[] for _ in range(num_robots)]
for city, label in enumerate(labels):
    tours[label].append(city)

# Find shortest path tours with 2-opt algorithm
def two_opt(tour):
    min_change = -1
    while min_change < 0:
        min_change = 0
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if i == 1 and j == len(tour) - 1:
                    continue
                change = (distances[tour[i-1], tour[i]] + distances[tour[j-1], tour[j]]) - (distances[tour[i-1], tour[j-1]] + distances[tour[i], tour[j]])
                if change > 0:
                    tour[i:j] = reversed(tour[i:j])
                    min_change += change
    return tour

# Optimize and calculate costs
overall_total_cost = 0

for robot_id in range(num_robots):
    depot = depots[robot_id]
    tour = [depot] + tours[robot_id]
    if depot not in tour:
        tour.append(depot)
    
    optimized_tour = two_opt(tour)
    total_cost = 0
    for k in range(1, len(optimized_tour)):
        total_cost += distances[optimized_tour[k-1], optimized_tour[k]]

    print(f"Robot {robot_id} Tour: {optimized_tour}")
    print(f"Robot {robot_id} Total Travel Cost: {total_cost:.2f}")
    overall_total_cost += total_cost

print(f"Overall Total Travel Cost: {overall_total_data_cost:.2f}")