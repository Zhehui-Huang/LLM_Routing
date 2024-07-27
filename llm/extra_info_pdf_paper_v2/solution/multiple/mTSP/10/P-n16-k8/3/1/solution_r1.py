import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean, cdist

# Define the cities coordinates (excluding the depot)
cities = [
    (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 48), (58, 27), (37, 69)
]
depot = (30, 40)
cities.insert(0, depot)  # insert depot at index 0

# Number of robots
num_robots = 8

# Clustering the cities into groups for each robot
kmeans = KMeans(n_clusters=num_robots, random_state=42)
clusters = kmeans.fit_predict(cities)
clustered_cities = {i: [] for i in range(num_robots)}

for city_index, cluster_id in enumerate(clusters):
    clustered_cities[cluster_id].append(city_index)

# Function to compute the total distance of a given tour
def compute_tour_distance(tour, city_coordinates):
    distance = 0
    for i in range(len(tour) - 1):
        distance += euclidean(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    return distance

# Utilize nearest neighbor heuristic to solve the TSP for the given city indices
def nearest_neighbor_tsp(start_city, city_indices, city_coordinates):
    tour = [start_city]
    remaining_cities = set(city_indices)
    remaining_cities.remove(start_city)
    
    current_city = start_city
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: euclidean(city_coordinates[current_city], city_coordinates[x]))
        tour.append(next_city)
        current_city = next_city
        remaining_cities.remove(next_city)
    tour.append(start_city)  # Return to the start point
    return tour

# Calculate tours and distances for each robot
overall_total_distance = 0

for i in range(num_robots):
    tour = nearest_neighbor_tsp(0, clustered_cities[i], cities)
    tour_distance = compute_tour_distance(tour, cities)
    overall_total_distance += tour_distance
    print(f'Robot {i} Tour: {tour}')
    print(f'Robot {i} Total Travel Cost: {tour_distance:.2f}')

print(f'Overall Total Travel Cost: {overall_total_distance:.2f}')