import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
import random

# City positions excluding the depot
cities = [(37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67),
          (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Including depot in the cities list
cities_with_depot = [(30, 40)] + cities

# Number of robots
num_robots = 2

# Euclidean distance function
def calculate_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.all(city2))

# Cluster cities using K-Means
km = KMeans(n_clusters=num_robots, random_state=42).fit(cities)
labels = km.labels_

# Create tours for each robot based on clusters
initial_tours = [[] for _ in range(num_robots)]
for city_index, label in enumerate(labels):
    initial_tours[label].append(city_index + 1)  # +1 to adjust index as city 0 is depot

# Random greedy heuristic to build initial paths
def greedy_path_construction(start_city, cities):
    path = [start_city]
    current_city = start_city
    local_cities = cities[:]
    while local_cities:
        next_city = min(local_cities, key=lambda x: calculate_distance(cities_with_depot[current_city], cities_with_depot[x]))
        local_cities.remove(next_city)
        path.append(next_city)
        current_city = next_city
    path.append(start_city)  # return to depot
    return path

# Construct initial tours
tours = [greedy_path_construction(0, tour) for tour in initial_tours]

# Calculate tour costs
def calculate_tour_cost(tour):
    return sum(calculate_distance(cities_with_depot[tour[i]], cities_with_deput[tour[i+1]]) for i in range(len(tour)-1))

tour_costs = [calculate_tour_cost(tour) for tour in tours]

# Output results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max(tour_costs)}")