import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Define cities and their coordinates
coordinates = np.array([
    [30, 40], [37, 52], [49, 49], [52, 64], [31, 62], [52, 33], [42, 41],
    [52, 41], [57, 58], [62, 42], [42, 57], [27, 68], [43, 67], [58, 48],
    [58, 27], [37, 69]
])

# Number of robots
num_robots = 8
depot_city = 0

# Calculate the Euclidean distance matrix
distance_matrix = np.zeros((16, 16))
for i in range(16):
    for j in range(16):
        distance_matrix[i, j] = euclidean(coordinates[i], coordinates[j])

# Using KMeans to cluster cities (excluding the depot city)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])
city_clusters = kmeans.labels_

# Assign cities to robots based on clusters
robot_tours = [[] for _ in range(num_robots)]
for city, cluster in enumerate(city_clusters, start=1):  # start=1 to adjust index as depot is 0
    robot_tours[cluster].append(city)

# Append and prepend the depot city to each tour
for tour in robot_tours:
    tour.insert(0, depot_city)
    tour.append(depot_city)

# Function to calculate the total cost of a tour
def tour_cost(tour, dist_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += dist_matrix[tour[i], tour[i+1]]
    return cost

# Calculate costs for each robot's tour and find maximum cost
costs = [tour_cost(tour, distance_matrix) for tour in robot_tours]
max_cost = max(costs)

# Output the results
for i, tour in enumerate(robot_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")
print(f"Maximum Travel Cost: {max_cost}")