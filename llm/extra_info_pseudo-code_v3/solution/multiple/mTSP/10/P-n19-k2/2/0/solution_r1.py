import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans

# Given city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Number of robots (vehicles)
num_robots = 2

# Compute the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Cluster cities into num_robots clusters
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # excluding the depot
labels = kmeans.labels_

# Robots start at depot
tours = {i: [0] for i in range(num_robots)}  # Initialize tours with the depot city
total_cost = {i: 0 for i in range(num_robots)}

# Assign cities to nearest robot's tour based on clustering
for idx, label in enumerate(labels):
    city_idx = idx + 1  # Correct index for city considering the depot city as 0
    tours[label].append(city_idx)

# Close the loop back to depot for all robots
for i in range(num_robots):
    tours[i].append(0)  # Append the depot city at end

# Calculate the total costs of each tour and overall cost
overall_total_cost = 0
for robot_id in range(num_robots):
    robot_tour = tours[robot_AX]
    tour_cost = sum(dist_matrix[robot_tour[i], robot_tour[i + 1]] for i in range(len(robot_tour) - 1))
    total_cost[robot_id] = tour_cost
    overall_total_cost += tour_cost

    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total Travel Cost:.2f}")