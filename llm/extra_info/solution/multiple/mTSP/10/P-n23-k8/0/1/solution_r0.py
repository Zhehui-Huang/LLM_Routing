import numpy as np
import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Heuristic: k-means clustering to assign cities to robots ##
from sklearn.cluster import KMeans

coordinates = np.array(list(cities.values()))
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:]) # skip depot in clustering
clusters = kmeans.labels_


# Assign cities to robots
robot_routes = [[] for _ in range(num_robots)]

for i, cluster in enumerate(clusters, start=1):
    robot_routes[cluster].append(i)

# Nearest neighbor algorithm for each cluster
def nearest_neighbor_tour(start, cities):
    unvisited = set(cities)
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city

    tour.append(start)  # return to depot
    return tour

# Compute tours and costs
total_cost = 0

for i in range(num_robots):
    tour = nearest_neighbor_tour(0, robot_routes[i])
    cost = sum(distance_matrix[tour[j]][tour[j+1]] for j in range(len(tour) - 1))
    total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")