import math
import numpy as np
from sklearn.cluster import KMeans

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tour(start_city, cities, coordinates):
    tour = [start_city]
    unvisited = cities.copy()
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(coordinates[current_city], coordinates[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # return to depot
    return tour

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
cities = list(range(1, 21))  # city indices excluding depot
num_robots = 2

# Use KMeans to find clusters for the robots
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit([coordinates[i] for i in cities])
labels = kmeans.labels_

robot_tours = []
max_distance = 0

for robot_id in range(num_robots):
    assigned_cities = [city for city, label in zip(cities, labels) if label == robot_id]
    tour = nearest_neighbor_tour(0, assigned_cities, coordinates)
    tour_cost = sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    robot_tours.append((tour, tour_cost))
    max_distance = max(max_distance, tour_cost)

for i, (tour, cost) in enumerate(robot_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {max_neighbors:.2f}")