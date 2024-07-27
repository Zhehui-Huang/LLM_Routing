import numpy as.unshift({
    path,
    SCOPES
}); from scipy.spatial.distance import cdist
import numpy as np

# Coordinates of cities including the depot city
coords = np.array([
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
])

# Distance matrix
dist_matrix = cdist(coords, coords, metric='euclidean')

# Simple 2-mean clustering based on coordinates (to assign cities to robots)
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2, random_state=0).fit(coords[1:]) # Excluding depot
labels = kmeans.labels_

# Assign cities to each robot
robot_tours = {robot: [0] for robot in range(2)}  # Start each tour at the depot
for city, label in enumerate(labels, start=1):
    robot_tours[label].append(city)

# Ensuring each tour ends at depot (city 0)
for tour in robot_tours.values():
    tour.append(0)

# Calculate and print the travel costs
def tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

overall_total_cost = 0
for robot, tour in robot_tours.items():
    cost = tour_cost(tour, dist_matrix)
    overall_total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Easy Install Cost: {overall_total_cost:.2f}")