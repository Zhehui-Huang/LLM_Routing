import numpy as np
import math
from sklearn.cluster import KMeans

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}
num_cities = len(cities) - 1  # excluding the depot city
num_robots = 8

# Helper function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Step 2: Assign initial clusters using K-means
city_coords = np.array([coord for coord in cities.values()])
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_coords[1:])  # exclude depot
labels = kmeans.labels_

# Step 3: Creating tours for each robot
routes = {i: [0] for i in range(num_robots)}  # starting each route at the depot
for city_index, label in enumerate(labels, start=1):  # city indices shifted by 1
    routes[label].append(city_index)

# Closing each route at the depot
for route in routes.values():
    route.append(0)

# Step 4: Calculate route distance and determine maximum travel cost
def calculate_route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(cities[route[i]], cities[route[i+1]])
    return cost

# Displaying results
max_travel_cost = 0
for i, route in routes.items():
    cost = calculate_route_cost(route)
    max_travel_cost = max(max_travel_cost, cost)
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {round(cost, 2)}")

print(f"Maximum Travel Cost: {round(max_travel_cost, 2)}")