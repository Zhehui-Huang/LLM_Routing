import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Define city coordinates
city_coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
               (45, 35)]

# Assign depots
depots = [0, 1]

# Number of robots and depots alignment (assuming one secret robot per depot for simplicity)
num_robots = len(depots)

# Distance function
def calculate_distance(city1, city2):
    return euclidean(city_coords[city1], city_coords[city2])

# K-means clustering to assign cities to nearest depot
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_coords)
labels = kmeans.labels_

# Create tours for each robot
tours = {i: [] for i in range(num_robots)}
for city, label in enumerate(labels):
    tours[label].append(city)

# Nearest neighbor search within each cluster to form a tour
def nearest_neighbor_tour(cities, start):
    tour = [start]
    current = start
    unvisited = set(cities)
    unvisited.remove(start)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    return tour

# Generate tours and calculate costs
total_cost = 0
results = []

for robot_id, initial_depots in enumerate(depots):
    tour = nearest_neighbor_tour(tours[robot_id], initial_depots)
    tour_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    total_cost += tour_cost
    results.append((robot_id, tour, tour_cost))

# Display results
for result in results:
    robot_id, tour, cost = result
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")