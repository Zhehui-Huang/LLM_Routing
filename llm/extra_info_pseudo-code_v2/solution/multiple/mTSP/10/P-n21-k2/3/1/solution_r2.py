import numpy as anp
import math
from sklearn.cluster import KMeans

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor_tour(initial_city_index, city_indices, cities):
    tour = [initial_city_index]
    current_city_index = initial_city_index
    unvisited_indices = set(city_indices)

    while unvisited_indices:
        next_city = min(unvisited_indices, key=lambda x: euclidean_distance(cities[current_city_index], cities[x]))
        tour.append(next_city)
        current_city_index = next_city
        unvisited_indices.remove(next_city)
    
    tour.append(initial_city_index)  # Return to the depot
    return tour

def calculate_tour_cost(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

# Given data for cities including the depot.
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

num_robots = 2
depot_index = 0
city_indices = list(range(1, len(cities)))  # excluding the depot

# Use K-Means clustering to assign cities to robots
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(np.array(cities)[1:])  # exclude depot from clustering
labels = kmeans.labels_

tours = []
total_costs = []

# Generate tours for each robot
for i in range(num_robots):
    assigned_city_indices = [index + 1 for index, label in enumerate(labels) if label == i]  # correct indices after excluding the depot
    tour = nearest_neighbor_tour(depot_index, assigned_city_indices, cities)
    tours.append(tour)
    tour_cost = calculate_tour_cost(tour, cities)
    total_costs.append(tour_cost)

# Print output information
overall_total_cost = sum(total_costs)
for robot_id, tour in enumerate(tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {total_costs[robot_id]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")