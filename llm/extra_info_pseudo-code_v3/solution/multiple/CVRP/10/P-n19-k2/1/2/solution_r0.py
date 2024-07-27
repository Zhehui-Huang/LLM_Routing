import numpy as np
from scipy.spatial.distance import euclidean

# City information
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

num_robots = 2
robot_capacity = 160

# Calculate the distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean(coordinates[i], coordinates[j])
        else:
            distance_matrix[i][j] = float('inf')  # Infinity for same-city travel to prevent choosing this route

# Simple CVRP solver function
def cvrp_solver(num_robots, robot_capacity, demands, distance_matrix):
    n = len(demashes # Excluding the depot
    remaining_demands = demands.copy()

    # Create a simplistic initial solution: Nearest Neighbor Heuristic
    routes = [[] for _ in range(num_robots)]
    loads = [0] * num_robots
    unvisited = set(range(1, n))  # start from 1 to skip the depot

    # Robot routes initialization
    for robot in range(num_robots):
        current_city = 0
        routes[robot].append(current_city)

        while unvisited and loads[robot] + min(remaining_demands[city] for city in unvisited if remaining_demands[city] > 0) <= robot_capacity:
            # Find the nearest unvisited city that the robot can serve
            next_city = min(unvisited, key=lambda x: (distance_matrix[current_city][x], -remaining_demands[x]))
            if loads[robot] + remaining_demands[next_city] <= robot_capacity:
                routes[robot].append(next_city)
                unvisited.remove(next_city)
                loads[robot] += remaining_demands[next_city]
                current_city = next_city

        routes[robot].append(0)  # Return to depot

    return routes

# Calculate the travel cost of each tour
def calculate_costs(routes, distance_matrix):
    robot_costs = []
    for route in routes:
        cost = 0
        for i in range(len(route) - 1):
            cost += distance_matrix[route[i]][route[i+1]]
        robot_costs.append(cost)
    return robot_costs

routes = cvrp_solver(num_robots, robot_capacity, demands, distance_matrix)
robot_costs = calculate_costs(routes, distance_matrix)
total_cost = sum(robot_costs)

# Outputting the tours and costs
for idx, route in enumerate(routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {robot_costs[idx]:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")