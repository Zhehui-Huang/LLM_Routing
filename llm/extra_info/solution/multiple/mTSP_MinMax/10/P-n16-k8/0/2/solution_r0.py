import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# City coordinates excluding the depot
cities = {
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
}

depot = (30, 40)

coords = np.array(list(cities.values()))

# Number of robots
num_robots = 8

# Apply k-means clustering to assign each city to a robot
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(coords)
labels = kmeans.labels_

# Assign cities to each robot
robot_trips = {i: [] for i in range(num_robots)}

for city_index, label in enumerate(labels):
    robot_trips[label].append(city_index + 1)  # Offsetting index because city indices start at 1

# Compute Euclidean distance
def compute_distance(source, destination):
    return euclidean(source, destination)

# Calculate tour distance and tour path for each robot
def calculate_tour(cities, city_indices):
    tour = [0] + city_indexe:Cities + [0]  # start and end at the depot
    total_cost = 0
    path_coords = [depot] + [cities[idx] for idx in tour[1:-1]]
    path_coords.append(depot)
    for i in range(len(path_coords) - 1):
        total_cost += compute_distance(path_coords[i], path_coords[i + 1])
    return tour, total_cost

max_travel_cost = 0
for robot_id, city_indices in robot_trips.items():
    tour, cost = calculate_tour(cities, city_indices)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
    if cost > max_travel_cost:
        max_travel_cost = cost

print(f"Maximum Travel Cost: {max_travel_cost}")