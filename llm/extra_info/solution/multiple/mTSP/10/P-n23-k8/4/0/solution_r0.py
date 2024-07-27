import math
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

# Define the coordinates of the depot and the other cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Calculate the distance matrix
def euclidean_dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

n_cities = len(coordinates)
distance_matrix = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_dist(*coordinates[i], *coordinates[j])

# Assign robots to cities using clustering
num_robots = 8
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # excluding depot
labels = kmeans.labels_

# Assign cities to robots as per cluster label
robots_cities = {i: [1 + index for index, label in enumerate(labels) if label == i] for i in range(num_robots)}

# Function to calculate the cost of a tour
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    return cost

# Create tours and calculate costs
overall_total_cost = 0
results = []

# Generating dummy tours (returning to depot after visit each city)
for robot_id, cities in robots_cities.items():
    tour = [0] + cities + [0]
    cost = tour_cost(tour)
    results.append((robot_id, tour, cost))
    overall_total_cost += cost

# Output results
for robot_id, tour, cost in results:
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {round(cost, 2)}")

print(f"\nOverall Total Travel Cost: {round(overall_total_cost, 2)}")