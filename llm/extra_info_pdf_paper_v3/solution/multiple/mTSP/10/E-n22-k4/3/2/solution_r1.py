import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans

# Define the cities and their coordinates
cities_coordinates = np.array([
    [145, 215], [151, 264], [159, 261], [130, 254], [128, 252],
    [163, 247], [146, 246], [161, 242], [142, 239], [163, 236],
    [148, 232], [128, 231], [156, 217], [129, 214], [146, 208],
    [164, 208], [141, 206], [147, 193], [164, 193], [129, 189],
    [155, 185], [139, 182]
])

# Number of robots
num_robots = 4

# Calculate pair-wise distances between cities
dist_matrix = distance_matrix(cities_coordinates, cities_coordinates)

# K-means to cluster cities into the number of robots
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(cities_coordinates[1:])

# Determine which cities each robot visits
clusters = kmeans.labels_

# Function to find nearest city not visited
def find_nearest(current_city, cities, visited):
    distances = dist_matrix[current_city]
    min_dist = np.inf
    city_index = -1
    for i in cities:
        if i not in visited and distances[i] < min_dist:
            min_dist = distances[i]
            city_index = i
    return city_index, min_dist

# Dictionary to hold tour for each robot
tours = {i: [0] for i in range(num_robots)}  # start at the depot
tour_costs = {i: 0 for i in range(num_robots)}

# Construct the tour for each robot using the nearest neighbor strategy
for robot in range(num_robots):
    current_city = 0
    visited = {0}
    target_cities = [index + 1 for index, cluster in enumerate(clusters) if cluster == robot]
    while len(target_cities) > 0:
        next_city, cost = find_nearest(current_city, target_cities, visited)
        tours[robot].append(next_city)
        tour_costs[robot] += cost
        visited.add(next_city)
        current_city = next_city
        target_cities.remove(next_city)
    # Return to depot
    cost_to_depot = dist_matrix[current_city][0]
    tours[robot].append(0)
    tour_costs[robot] += cost_to_depot

# Output results
overall_cost = 0
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {tour_costs[robot]:.2f}")
    overall_cost += tour_costs[robot]

print(f"Overall Total Travel Cost: {overall SA - SA - IPI})=%.2f" % overall_cost)