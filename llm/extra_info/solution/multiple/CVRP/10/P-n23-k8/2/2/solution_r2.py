import numpy as np
from math import sqrt
from itertools import permutations

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Demands
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

# Robots info
num_robots = 8
robot_capacity = 40

def euclidean_distance(coord1, coord2):
    """Calculates the Euclidean distance between two coordinates."""
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def create_distance_matrix(coords):
    """Create a distance matrix for the given list of coordinates."""
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = eucliridean_distance(coords[i], coords[j]) if i != j else float('inf')
    return dist_matrix

distance_matrix = create_distance_matrix(coordinates)

def vehicle_routing(capacity, demands, num_vehicles):
    # Initialization
    routes = []
    total_costs = 0

    # Create a list of cities excluding the depot
    cities = list(range(1, len(coordinates)))  # Excluding the depot city

    # Attempt to find a solution
    while cities:
        for _ in range(num_vehicles):
            if not cities:
                break
            current_route = [0]  # start from the depot
            load = 0
            while cities and load < capacity:
                next_city = min(
                    cities, key=lambda x: distance_matrix[current_route[-1], x]
                    if (load + demands[x] <= capacity) else float('inf')
                )
                
                if load + demands[next_city] > capacity:
                    break

                current_route.append(next_city)
                load += demands[next_city]
                cities.remove(next_city)

            current_route.append(0)  # return to the depot
            route_cost = sum(distance_matrix[current_route[i], current_route[i + 1]] for i in range(len(current_route) - 1))
            routes.append(current_route)
            total_costs += route_cost

    return routes, total_costs

# Find routes for robots
routes, overall_cost = vehicle_routing(robot_capacity, demands, num_robots)

# Output result
for i, route in enumerate(routes):
    print(f"Robot {i} Tour: {route}")
    route_cost = sum(distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))
    print(f"Robot {i} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")