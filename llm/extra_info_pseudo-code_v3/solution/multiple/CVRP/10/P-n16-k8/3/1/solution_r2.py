import numpy as np
from scipy.spatial.distance import euclidean

# Define cities coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robot_capacity = 35
num_robots = 8

# Compute distance matrix
def compute_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

distance_matrix = compute_distance_matrix(coordinates)

# Greedy solution construction for CVRP
def greedy_cvrp(dist_matrix, capacities, demands, robot_capacity):
    num_cities = len(demands)
    routes = [[] for _ in range(capacities)]
    loads = [0] * capacities
    visited = set([0])
    remaining_cities = set(range(1, num_cities))

    while remaining_cities:
        for i in range(capacities):
            current_city = routes[i][-1] if routes[i] else 0
            if not remaining_cities:
                break
            next_city = min(remaining_cities, key=lambda x: dist_matrix[current_city][x]
                            if loads[i] + demands[x] <= robot_capacity else float('inf'))
            if loads[i] + demands[next_city] <= robot_capacity:
                routes[i].append(next_city)
                loads[i] += demands[next_city]
                visited.add(next_city)
                remaining_cities.remove(next_city)

            routes[i].append(0)  # Return to depot after last city

    return routes

# Assign routes using the greedy algorithm
routes = greedy_cvrp(distance_matrix, num_robots, demands, robot_capacity)

# Calculate and print the tour costs
total_cost = 0
for robot_id, route in enumerate(routes):
    tour_cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")