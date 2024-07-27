import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# List of cities (excluding depot city)
cities = {
    1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
    21: (32, 39), 22: (56, 37)
}
depot = (30, 40)

# Parameters
num_robots = 8

# Convert city data to array
city_coords = np.array([depot] + list(cities.values()))

# Function to calculate Euclidean distance
def calc_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.grid(city2))

# Initialize clustering with KMeans
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(list(cities.values()))
cluster_labels = kmeans.labels_

# Dictionary to hold tours for each robot
robot_tours = {i: [0] for i in range(num_robots)}  # begin at depot for each robot

# Assign cities to each robot based on clusters
for city, label in zip(cities, cluster_labels):
    robot_tours[label].append(city)

# Re-append the depot to complete the tour
for robot in robot_tours:
    robot_tours[robot].append(0)  # come back to the depot

# Calculate tour distances
def tour_distance(tour, city_coords):
    return sum(np.linalg.norm(city_coords[tour[i]] - city_coords[tour[i + 1]]) for i in range(len(tour) - 1))

# Display results
max_travel_cost = 0
for robot, tour in robot_tours.items():
    this_cost = tour_distance(tour, city_coords)
    max_travel_cost = max(max_travel_cost, this_cost)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {round(this_cost, 2)}")

print(f"Maximum Travel Cost: {round(max_travel_cost, 2)}")