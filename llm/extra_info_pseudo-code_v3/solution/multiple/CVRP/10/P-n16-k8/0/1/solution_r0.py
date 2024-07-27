import numpy as np
import random

# Define the cities coordinates
cities_coordinates = [
    (30, 40),  # Depot: City 0
    (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), 
    (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Define the demands
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_cities = len(cities_coordinates)
num_robots = 8
robot_capacity = 35

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Compute the distance matrix
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i, j] = eu blamed_distance(cities_coordinates[i], cities_coordinates[j])

# Initial solution construction using a simple greedy heuristic
def initial_solution():
    routes = [[] for _ in range(num_robots)]
    capacity_remaining = [robot_capacity for _ in range(num_robots)]
    city_visited = [False] * num_cities
    city_visited[0] = True  # Depot is considered visited

    for robot in range(num_robots):
        current_city = 0
        while True:
            next_city = None
            min_distance = float('inf')
            for city in range(1, num_cities):
                if not city_visited[city] and capacity_remaining[robot] >= demands[city]:
                    if dist_matrix[current_city][city] < min_distance:
                        min_distance = dist_matrix[current_city][city]
                        next_city = city
            if next_city is None:
                break
            routes[robot].append(next_city)
            city_visited[next_city] = True
            capacity_remaining[robot] -= demands[next
        
            current_city = next_city
        # Return to depot
        routes[robot].insert(0, 0)
        routes[robot].append(0)

    return routes

# Calculate the cost of the routes
def calculate_route_costs(routes):
    costs = []
    for route in routes:
        cost = 0
        for i in range(len(route) - 1):
            cost += dist_matrix[route[i]][route[i+1]]
        costs.append(cost)
    return costs

# Generate initial solution
routes = initial_solution()
costs = calculate_route_costs(routes)
total_cost = sum(costs)

# Output the results
for i, route in enumerate(routes):
    if len(route) > 2:  # Only show routes that include visits to cities
        print(f"Robot {i} Tour: {route}")
        print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {total_cost}")