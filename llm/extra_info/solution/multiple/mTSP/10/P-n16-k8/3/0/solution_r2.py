import numpy as np
from sklearn.cluster import KMeans

# Coordinates of cities including depot
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
])

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Robot details
num_robots = 8
depot = 0

# Generate tours for each robot
# Splitting cities roughly into clusters/sectors using K-Means, excluding the depot for initial cluster assignment
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:]) # Avoid the depot in clustering
labels = kmeans.labels_

# Assign cities to robots based on clusters
robot_tours = [[] for _ in range(num_robots)]
total_tour_length = []

for i in range(1, num_cities):
    robot_tours[labels[i-1]].append(i)

# Each robot starts and ends at the depot
for i in range(num_robots):
    robot_tours[i] = [depot] + robot_tours[i] + [depot]

def calculate_tour_cost(tour):
    cost = sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    return cost

# Calculate costs and print results
overall_cost = 0
for i in range(num_robots):
    cost = calculate_tour_cost(robot_tours[i])
    overall_cost += cost
    print(f"Robot {i} Tour: {robot_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")