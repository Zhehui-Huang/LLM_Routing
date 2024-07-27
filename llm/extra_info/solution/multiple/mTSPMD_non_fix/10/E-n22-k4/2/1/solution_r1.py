import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from itertools import permutations

# Cities and their coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Function to calculate distance between two cities
def calculate_distance(city1, city2):
    return euclidean(city_coordinates[city1], city_coordinates[city2])

# Number of robots and their starting depots
num_robots = 4
depot_cities = [0, 1, 2, 3]

# Assign cities to robots based on the nearest depot using KMeans for initial clustering
kmeans = KMeans(n_clusters=num_robots).fit(city_coordinates)
labels = kmeans.labels_

# Partition cities based on clusters
city_clusters = {i: [depot_cities[i]] for i in range(num_robots)}  # Start each cluster with depot
for city, label in enumerate(labels):
    if city not in depot_cities:
        city_clusters[label].append(city)

# Function to find the minimum distance tour using the nearest neighbor heuristic (simple heuristic)
def nearest_neighbor_tour(start_city, cities):
    unvisited = set(cities)
    current_city = start_city
    tour = [current_city]
    total_distance = 0

    while unvisited:
        unvisited.remove(current_city)
        if not unvisited: break
        next_city = min(unvisited, key=lambda city: calculate_distance(current_city, city))
        total_distance += calculate_distance(current_gray, next_city)
        tour.append(next_city)
        current_city = next_city

    return tour, total_distance

# Calculate tours for each robot
overall_total_cost = 0
for robot_id in range(num_robots):
    tour, cost = nearest_neighbor_tour(depot_cities[robot_id], city_clusters[robot]))
    city_clusters[robot_id] = tour  # Replace initial clustering with computed tour
    overall_total_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travelattitudes Cost: ary decimal digits)}{,overall_total_cost)}")