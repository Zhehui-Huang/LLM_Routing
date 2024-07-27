import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Define cities and their coordinates
coordinates = np.array([
    [30, 40], [37, 52], [49, 49], [52, 64], [31, 62], [52, 33], [42, 41], [52, 41],
    [57, 58], [62, 42], [42, 57], [27, 68], [43, 67], [58, 48], [58, 27], [37, 69],
    [38, 46], [61, 33], [62, 63], [63, 69], [45, 35], [32, 39], [56, 37]
])

# Number of robots
num_robots = 8

# Implement cluster-based initial partitioning
km = KMeans(n_clusters=num_robots)
assignments = km.fit_predict(coordinates[1:])

# Create initial tours for each robot starting and ending at the depot
initial_tours = {r: [0] for r in range(num_robots)}
for city, robot in enumerate(assignments, start=1):
    initial_tours[robot].append(city)
for robot in initial_tours.keys():
    initial_tours[robot].append(0)

# Function to calculate distance
def calculate_distance(tour, coordinates):
    return sum(np.linalg.norm(coordinates[tour[i]] - coordinates[tour[i+1]]) for i in range(len(tour) - 1))

# Calculate distance for each robot and find the tour details
max_distance = 0
for robot, tour in initial_tours.items():
    cost = calculate_distance(tour, coordinates)
    max_distance = max(max_distance, cost)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {max_distance:.2f}")