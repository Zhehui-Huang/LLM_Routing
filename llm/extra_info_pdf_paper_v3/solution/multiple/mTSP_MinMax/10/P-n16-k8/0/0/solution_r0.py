import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# The coordinates of all cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Calculate Euclidean distances between all pairs of cities
def calculate_distances(coords):
    num_cities = len(coords)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean(coords[i], coords[j])
    return distances

distances = calculate_distances(coordinates)

# Define number of robots
num_robots = 8

# Perform clustering to assign cities to robots
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # exclude depot
labels = kmeans.labels_

# Create a route for each robot starting and ending at the depot
tours = {i: [0] for i in range(num_robots)}
for i, label in enumerate(labels):
    tours[label].append(i + 1)  # city indices are offset by 1

# Ensure each tour ends at the depot
for tour in tours.values():
    tour.append(0)

# Function to compute the total travel cost of a tour
def compute_tour_cost(tour, dist_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += dist_matrix[tour[i]][tour[i+1]]
    return total_cost

# Calculate cost for each tour and find the maximum
costs = {}
max_cost = 0
for robot_id, tour in tours.items():
    cost = compute_tour_cost(tour, distances)
    costs[robot_id] = cost
    max_cost = max(max_cost, cost)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")