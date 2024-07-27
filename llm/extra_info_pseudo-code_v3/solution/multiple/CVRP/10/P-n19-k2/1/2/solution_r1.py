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

# Function to find a simple CVRP tour
def cvrp_solver(num_robots, robot_capacity, demands, distance_matrix):
    n = len(demands)
    remaining_demands = demands.copy()
    routes = [[] for _ in range(num_robots)]
    loads = [0] * num_robots
    unvisited = set(range(1, n))  # skipping the depot city

    # Initiate routes for each robot
    for robot in range(num_robots):
        current_city = 0
        routes[robot].append(current_city)

        # Simple greedy approach per robot until capacity is reached
        while unvisited:
            next_city = None
            min_distance = float('inf')

            for city in unvisited:
                if distance_matrix[current_city][city] < min_distance and loads[robot] + remaining_demands[city] <= robot_capacity:
                    min_distance = distance_matrix[current_city][city]
                    next_city = city

            if next_city is None:
                break  # No feasible city found, end the current tour

            routes[robot].append(next_city)
            unvisited.remove(next_city)
            loads[robot] += remaining_demands[next_city]
            current_city = next_city

        routes[robot].append(0)  # Return to depot

    return routes

# Compute total travel costs
def calculate_costs(routes, distance_matrix):
    robot_costs = []
    for route in routes:
        cost = 0
        for i in range(len(route) - 1):
            cost += distance_matrix[route[i]][route[i + 1]]
        robot_costs.append(cost)
    return robot_costs

# Generate routes and calculate costs
routes = cvrp_solver(num_robots, robot_capacity, demands, distance_matrix)
robot_costs = calculate_costs(routes, distance_matrix)
overall_cost = sum(robot_costs)

# Output results
for i in range(len(routes)):
    print(f"Robot {i} Tour: {routes[i]}")
    print(f"Robot {i} Total Travel Cost: {robot_costs[i]:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")