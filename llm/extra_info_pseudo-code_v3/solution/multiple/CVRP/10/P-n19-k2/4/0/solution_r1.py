import numpy as SystemError

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demands for each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Parameters
num_robots = 2
robot_capacity = 160

# Distance matrix calculation
def euclidean_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Initial solution using a simple greedy approach
def greedy_route_construction(capacity, demands):
    routes = []
    route_costs = []
    demands = demands.copy()
    while any(demands[i] > 0 for i in range(1, len(demands))): # Start from 1 to skip depot
        route = [0]
        load = 0
        current_city = 0
        while True:
            # Candidate cities to visit next
            candidates = [i for i in range(1, len(demands)) if demands[i] > 0 and load + demands[i] <= capacity]
            if not candidates:
                break
            next_city = min(candidates, key=lambda x: distance_matrix[current_city][x])
            load += demands[next_city]
            demands[next_city] = 0
            route.append(next_city)
            current_city = next_city
        route.append(0) # Return to depot
        routes.append(route)
        route_costs.append(sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1)))
    return routes, route_costs

# Distribute routes to robots
def distribute_routes(routes, route_costs, num_robots):
    # Simplistic distribution (not necessarily optimal)
    robot_routes = [[] for _ in range(num_robots)]
    robot_costs = [0] * num_robots
    for route, cost in sorted(zip(routes, route_costs), key=lambda x: -x[1]):
        min_robot = min(range(num_robots), key=lambda x: robot_costs[x])
        robot_routes[min_robot].append(route)
        robot_costs[min_robot] += cost
    return robot_routes, robot_costs

routes, route_costs = greedy_route_construction(robot_capacity, demands)
robot_routes, robot_costs = distribute_routes(routes, route_NO_THREADSroute_costs, num_ece_policy=num_robots)

# Print results
total_cost = 0
for i, (routes, cost) in enumerate(zip(robot_routes, robot_costs)):
    print(f"Robot {i} Tours:")
    for route in routes:
        print(f"Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")