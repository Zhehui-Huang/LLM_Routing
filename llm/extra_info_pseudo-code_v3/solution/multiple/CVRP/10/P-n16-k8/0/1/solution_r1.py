import numpy as np

# Cities coordinates
cities_coordinates = [
    (30, 40),  # Depot City
    (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57),
    (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Demand list
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robot_capacity = 35
num_robots = 8

# Calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Building the distance matrix
num_cities = len(cities_coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(cities_coordinates[i], cities_coordinates[j])

# Greedy algorithm to construct initial solution
def initial_solution():
    routes = []
    load = [0] * num_robots
    routes = [[] for _ in range(num_robots)]
    city_assigned = [False] * num_cities
    city_assigned[0] = True  # Depot is always visited
    for i in range(num_robots):
        current_city = 0
        route = [current_city]
        while True:
            next_city = None
            min_dist = float('inf')
            for city in range(1, num_cities):
                if not city_assigned[city] and load[i] + demands[city] <= robot_capacity:
                    if distance_matrix[current_city][city] < min_dist:
                        min_dist = distance_matrix[current_city][city]
                        next_city = city
            if next_city is None:
                break
            route.append(next_city)
            city_assigned[next_city] = True
            load[i] += demands[next_city]
            current_city = next_city
        route.append(0)  # Return to depot
        routes[i] = route
    return routes

# Calculate the travel cost for each robot route
def calculate_costs(routes):
    costs = []
    for route in routes:
        cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
        costs.append(cost)
    return costs

# Getting the initial solution and costs
routes = initial_solution()
costs = calculate_costs(routes)
total_cost = sum(costs)

# Output tours and costs
for i in range(num_robots):
    if len(routes[i]) > 2:  # exclude routes that just go from depot to depot
        print(f"Robot {i} Tour: {routes[i]}")
        print(f"Robot {i} Total Travel Cost: {costs[i]:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")