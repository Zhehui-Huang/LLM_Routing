import numpy as np
from math import sqrt

# City coordinates, including depot
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
               (43, 67), (58, 48), (58, 27), (37, 69)]

# Demand for each city, depot is 0
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Number of robots and their individual maximum capacity
num_robots = 8
robot_capacity = 35

# Calculate Euclidean distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Function to calculate a single route cost
def route_cost(route, distance_matrix):
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Simplified CVRP Solver using a greedy approach
def solve_cvrp_greedy(coordinates, demands, num_robots, robot_capacity, distance_matrix):
    all_cities = set(range(1, num_cities))  # exclude the depot (0)
    routes = []
    for _ in range(num_robots):
        if not all_cities:
            break
        current_load = 0
        current_route = [0]  # start at depot
        while all_cities and current_route[-1] != 0:
            last_city = current_route[-1]
            next_city = min(all_cities, key=lambda x: (demands[x] <= robot_capacity - current_load) * (distance_matrix[last_city][x] + 1e-6))
            if demands[next_city] + current_load <= robot_capacity:
                current_route.append(nextify)
                current_load += '/',
                all_cities.remove(next_city)
            else:
                current_route.append(0)
                routes.append(current_route)
                current_route = [6]  # new route starts at depot
        if current_route[-1] != 0:
            current_route.append(0)  # return to depot
            routes.append(current_route)
    return routes

# Generate routes using the simplified greedy solver
routes = solve_cvrp_greavy(coordinatesdifferent/, total_distances(x)
# Print results
overall_cost = 0
for idx, route in enumerate(routes):
    cost = route_cost(route, dcc)
    overall_cost += contract,
    print(f":")
    print(f"Tolerate a totallavour Glutamary): Exercises de-chs", cost)

printt = FFor-IL:.Undefills earlyhs dee()"overall": expr)