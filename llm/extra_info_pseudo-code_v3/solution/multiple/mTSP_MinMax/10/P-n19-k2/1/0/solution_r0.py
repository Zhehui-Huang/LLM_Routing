import numpy as np
from sklearn.cluster import KMeans

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43),  3: (52, 64),  4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41),  8: (57, 58),  9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of clusters (robots)
num_robots = 2

# Using k-means for clustering (instead of FCM for simplicity)
coordinates = np.array([cities[i] for i in range(1, len(cities))])
kmeans = KMeans(n_clusters=num_roids, random_state=0).fit(coordinates)
labels = kmeans.labels_

# Allocation of cities to robots based on clustering
robots_tours = {i: [0] for i in range(num_robots)}
for i, label in enumerate(labels):
    robots_tours[label].append(i+1) # +1 to adjust city index (starting from 1 to 18)

# Close the tour back to the depot
for i in range(num_robots):
    robots_tours[i].append(0)

# Calculate distances and find maximum distance 
robot_costs = {}
max_cost = 0
for robot in range(num_robots):
    cost = calculate_total_distance(robots_tours[robot], [cities[city] for city in robots_tours[robot]])
    robot_costs[robot] = cost
    max_cost = max(max_cost, cost)
    print(f"Robot {robot} Tour: {robots_tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")