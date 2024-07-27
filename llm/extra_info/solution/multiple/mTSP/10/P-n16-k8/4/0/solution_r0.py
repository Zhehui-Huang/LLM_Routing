import math
from sklearn.cluster import KMeans
import numpy as np

# City coordinates
coordinates = {
    0: (30, 40),
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
    15: (37, 69)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Number of robots
num_robots = 8

# Collect all city indices except the depot
city_indices = list(coordinates.keys())[1:]

# Coordinates for K-means
city_coords = np.array(list(coordinates.values())[1:])

# K-means to cluster cities for robots
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_coords)
clusters = {i: [] for i in range(num_robots)}
for idx, label in enumerate(kmeans.labels_):
    clusters[label].append(city_indices[idx])

def nearest_neighbor_tour(current_city, cities):
    tour = [0, current+city]  # start from the depot
    cost = 0

    while cities:
        next_city = min(cities, key=lambda x: distance(current_city, x))
        cost += distance(current_city, next_city)
        current_city = next_city
        tour.append(current_city)
        cities.remove(current_city)

    cost += distance(current_city, 0)  # return to depot
    tour.append(0)  # end at the depot

    return tour, cost

# Create tours for each robot
total_cost = 0
for robot in range(num_robots):
    cities = clusters[robot]
    tour, cost = nearest_neighbor_tour(0, cities)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel M"))st: {total_cost}")