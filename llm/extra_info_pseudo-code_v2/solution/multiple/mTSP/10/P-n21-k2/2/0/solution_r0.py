import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Define the number of robots and list of city coordinates
num_robots = 2
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
               (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
               (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Calculate distance matrix
distance_matrix = cdist(coordinates, coordinates, metric='euclidean')

# Cluster cities (excluding depot) using KMeans
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])
labels = kmeans.labels_

# Function to find tour using Nearest Neighbor algorithm
def nearest_neighbor_tour(start_city, cities, distance_matrix):
    tour = [start_city]
    current_city = start_city
    remaining_cities = set(cities)
    remaining_cities.remove(start_city)
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: distance_matrix[current_city, city])
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
    tour.append(start_city)
    return tour

# Function to calculate total travel cost of a tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Assign tours to each robot and compute the tours
tours = []
total_costs = []

for robot in range(num_robots):
    cities_for_robot = [i + 1 for i in range(len(labels)) if labels[i] == robot]  # adding 1 because city indices shifted by 1
    if cities_for_robot:
        cities_for_robot.append(0)  # Add depot (index 0)
        tour = nearest_neighbor_tour(0, cities_for_robot, distance_matrix)
        tours.append(tour)
        total_costs.append(calculate_tour_cost(tour, distance_matrix))

# Output results
overall_total_cost = sum(total_costs)
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")