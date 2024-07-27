import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates
cities = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
         7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 
         14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
         21: (32, 39), 22: (56, 37)}

# Number of robots
num_robots = 8

def distance_matrix(cities):
    num_cities = len(cities)
    matrix = np.zeros((num_cities, num_cities))
    for i in cities:
        for j in cities:
            matrix[i][j] = euclidean(cities[i], cities[j])
    return matrix

dist_matrix = distance_matrix(cities)

def calculate_route_cost(route, dist_matrix):
    cost = sum(dist_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))
    return cost

def balanced_partition(num_elements, num_partitions):
    div, mod = divmod(num_elements, num_partitions)
    partition_sizes = [div + 1 if i < mod else div for i in range(num_partitions)]
    partitions = [
        sum(partition_sizes[:i], partition_sizes[i]) for i in range(num_partitions + 1)
    ]
    return [range(partitions[i], partitions[i + 1]) for i in range(num_partitions)]

# Assign cities (except the depot) to robots
city_indices = list(cities.keys())[1:]  # Exclude depot
robot_partitions = balanced_partition(len(city_indices), num_robots)

# Determine routes for each robot using basic nearest neighbor heuristic
robots_tours = []

for partition in robot_partitions:
    current_city = 0
    tour = [current_city]
    available_cities = [city_indices[i] for i in partition]
    
    while available_cities:
        next_city = min(available_cities, key=lambda x: dist_matrix[current_city, x])
        tour.append(next_city)
        available_cities.remove(next_city)
        current_city = next_city
    
    tour.append(0)  # Return to depot
    robots_tours.append(tour)

# Output tours and calculate costs
total_cost = 0

for i, tour in enumerate(robots_tours):
    tour_cost = calculate_route_cost(tour, dist_matrix)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour     _cost}")

print(f"Overall Total Travel Cost: {total_cost}")