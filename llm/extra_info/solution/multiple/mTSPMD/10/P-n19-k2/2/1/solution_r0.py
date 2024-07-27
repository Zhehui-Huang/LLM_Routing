import numpy as np
from scipy.spatial import distance
from sklearn.cluster import KMeans
import itertools

# Define the coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Step 1: Calculate Euclidean distances
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = distance.euclidean(cities[i], cities[j])
    return distances

distances = calculate_distances(cities)

# Step 2: Split cities using K-means clustering
coordinates = np.array(list(cities.values()))
kmeans = KMeans(n_clusters=2, random_state=0).fit(coordinates)
labels = kmeans.labels_

cities_robot_0 = [i for i in range(len(labels)) if labels[i] == 0]
cities_robot_1 = [i for i in range(len(labels)) if labels[i] == 1]

# Step 3: Compute TSP route for each robot
def compute_tsp_route(cities, distances):
    path = []
    visited = set()
    current = cities[0]
    path_cost = 0
    path.append(current)
    visited.add(current)
    
    while len(visited) < len(cities):
        next_city = min([(distances[current][j], j) for j in cities if j not in visited], key=lambda x: x[0])
        current = next_city[1]
        path_cost += next_city[0]
        path.append(current)
        visited.add(current)
    
    # Add path back to the initial city for the round trip
    path.append(path[0])
    path_cost += distances[path[-2]][path[-1]]
    
    return path, path_cost

robot_0_tour, robot_0_cost = compute_tsp_route(cities_robot_0, distances)
robot_1_tour, robot_1_cost = compute_tsp_route(cities_robot_1, distances)
overall_cost = robot_0_cost + robot_1_cost

# Output the tours and their costs
print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}")
print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}")
print(f"Overall Total Travel Cost: {overall_cost}")