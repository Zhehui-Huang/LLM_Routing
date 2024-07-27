import numpy as np
from math import sqrt
from sys import maxsize

# City coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
               (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robots information
num_robots = 8
robot_capacity = 40

def euclidean_distance(coord1, coord2):
    """Calculates the Euclidean distance between two coordinates."""
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def build_distance_matrix(coordinates):
    """Builds a full distance matrix from a list of coordinates."""
    size = len(coordinates)
    distance_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if i != j:
                distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])
            else:
                distance_matrix[i, j] = float('inf')
    return distance_matrix

# Build distance matrix
distance_matrix = build_distance_matrix(coordinates)

def find_routes():
    tours = []
    total_costs = []
    used_cities = set([0])
    free_cities = set(range(1, len(coordinates)))
    
    while free_cities:
        for _ in range(num_robots):
            if not free_cities:
                break
            current_city = 0
            route = [current_city]
            load = 0
            
            while free_cities:
                # Find the nearest city that does not exceed capacity
                next_city = None
                min_dist = maxsize
                
                for city in free_cities:
                    if load + demands[city] <= robot_capacity and distance_matrix[current_city, city] < min_dist:
                        min_dist = distance_matrix[current_city, city]
                        next_city = city
                
                if next_city is None:
                    break
                
                route.append(next_city)
                load += demands[next_city]
                current_city = next_city
                used_cities.add(next_city)
                free_cities.remove(next_city)
            
            if route[-1] != 0:
                route.append(0)  # Return to depot
            
            tour_cost = calculate_route_cost(route, distance_matrix)
            total_costs.append(tour_cost)
            tours.append(route)
    
    return tours, total_costs

def calculate_route_cost(route, distance_matrix):
    cost = 0
    for i in range(len(route) - 1):
        cost += distance_matrix[route[i]][route[i+1]]
    return cost

tours, total_costs = find_routes()
overall_total_cost = sum(total_costs)

# Display the output for each robot
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")

print(f"Overall Total Travel Cost: {overall_total(TYPE_INVOKATION_PATH).cost}")