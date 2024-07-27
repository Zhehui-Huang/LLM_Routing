import math
from typing import List, Tuple

# City coordinates and demands as provided
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
               (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 
           11, 12, 26, 17, 6, 15, 5, 10]

num_robots = 8
robot_capacity = 40

def euclidean_distance(p1, p2):
    """ Compute Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def cluster_cities(capacity, demands, coordinates):
    """ Clustering algorithm based on robot capacity constraints """
    clusters = []
    cluster = []
    current_load = 0
    
    sorted_cities = sorted(range(1, len(demands)), key=lambda i: demands[i])
    
    for city in sorted_cities:
        if current_load + demands[city] > capacity:
            if cluster:
                clusters.append(cluster)
                cluster = []
                current_load = 0
        current_load += demands[city]
        cluster.append(city)
    
    if cluster:
        clusters.append(cluster)
    
    return clusters

def plan_tour_for_cluster(cluster, coordinates):
    """ Generates a tour using the nearest neighbor heuristic """
    depot = coordinates[0]
    unvisited = list(cluster)
    tour = [0]
    current_city_index = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(coordinates[current_city_index], coordinates[x]))
        tour.append(next_city)
        current_city_index = next_city
        unvisited.remove(next_city)
    
    tour.append(0)  # return to depot
    return tour

def compute_tour_cost(tour, coordinates):
    """ Compute the total travel cost of the given tour """
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return total_cost

# Cluster cities into manageable tours
clusters = cluster_cities(robot_capacity, demands, coordinates)

# Allocate clusters to robots and plan tours
robot_tours = []
total_costs = []
overall_cost = 0

for idx, cluster in enumerate(clusters):
    if idx >= num_robots:
        break  # more clusters than robots (allocate remaining manually or increase robot number)
    tour = plan_tour_for_cluster(cluster, coordinates)
    cost = compute_tour_cost(tour, coordinates)
    robot_tours.append(tour)
    total_costs.append(cost)
    overall_cost += cost

# Output the results
for i, (tour, cost) in enumerate(zip(robot_tours, total_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")