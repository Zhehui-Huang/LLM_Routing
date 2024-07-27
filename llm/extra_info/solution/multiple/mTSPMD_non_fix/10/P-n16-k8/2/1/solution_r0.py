import math
import numpy as
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots, all starting from city 0
num_robots = 8
start_depot = 0

# Calculate distance matrix
distance_mat = distance_matrix(cities, cities)

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Cluster cities to group into near-by sets for each robot
km = KMeans(n_clusters=num_robots, random_state=0).fit(cities)
clusters = km.labels_

# Planning the route for each robot starting from depot city 0
def find_shortest_tour(cities_indices, depot):
    # Start at the depot
    path = [depot]
    unvisited = set(cities_indices)
    unvisited.remove(depot)
    
    current_city = depot
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_mat[current_city][x])
        path.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    return path

# Organize cities by assigned robots
robot_tours = {i: [] for i in range(num_robots)}
for city_index, label in enumerate(clusters):
    robot_tours[label].append(city_index)

# Tour and cost calculation
total_cost = 0
for i in range(num_robots):
    tour = find_shortest_tour(robot_tours[i], start_depot)
    tour_cost = sum(distance_mat[tour[j]][tour[j+1]] for j in range(len(tour)-1))
    robot_tours[i] = tour
    total_cost += tour_cost
    
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")