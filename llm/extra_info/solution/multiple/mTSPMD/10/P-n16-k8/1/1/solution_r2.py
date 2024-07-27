import math
import numpy as np
from sklearn.cluster import KMeans

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def tour_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
num_cities = len(cities)
num_robots = 8

# Distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i, j] = euclidean_distance(*cities[i], *cities[j])

# Assign robots to clusters of cities (use K-means clustering based on city coordinates)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities)
clusters = kmeans.labels_

routes = {}
overall_cost = 0

# Create clustered tours for robots
for robot in range(num_robots):
    # Find cities in the robot's cluster including the depot city
    route = [i for i in range(num_cities) if clusters[i] == robot] + [robot]
    route.insert(0, robot)  # Return to the starting city

    # Find a simple path: nearest neighbor heuristic
    unvisited = set(route)
    current_city = robot
    path = [current_city]
    unvisited.remove(current_city)

    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current_city, x])
        path.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    path.append(robot)  # return to depot
    cost = tour_distance(path, distance_matrix)

    routes[robot] = (path, cost)
    overall_cost += cost

# Outputting the results
for robot, (tour, cost) in routes.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")