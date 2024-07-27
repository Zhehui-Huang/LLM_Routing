import numpy as np
from math import sqrt

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demands
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Number of robots and their carrying capacity
num_robots = 2
capacity = 160

# Compute the Euclidean distance matrix
distance_matrix = [
    [sqrt((xi - xj)**2 + (yi - yj)**2) for (xj, yj) in coordinates] 
    for (xi, yi) in coordinates
]

# Assign routes and demands to robots while ensuring their capacities are not exceeded
def assign_routes():
    robot_routes = [[] for _ in range(num_robots)]
    loads = [0] * num_robots
    total_cost = 0
    route_costs = []

    for city in range(1, len(coordinates)):  # start from 1 to skip the depot
        assigned = False
        for robot in range(num_robots):
            if loads[robot] + demands[city] <= capacity:
                if not robot_routes[robot]:
                    robot_routes[robot].append(0)
                robot_routes[robot].append(city)
                loads[robot] += demands[city]
                assigned = True
                break
        if not assigned:
            return None  # If no robot can take the city within capacity

    # Calculate cost and add return to depot
    for robot in range(num_robots):
        robot_routes[robot].append(0)
        cost = sum(distance_matrix[robot_routes[robot][i]][robot_routes[robot][i+1]] for i in range(len(robot_routes[robot]) - 1))
        route_costs.append(cost)
        total_cost += cost

    return robot_routes, route_costs, total_cost

# Execute assignment function
routes, costs, total_cost = assign_routes()

# Output results
for index, route in enumerate(routes):
    print(f"Robot {index} Tour: {[0] + route}")
    print(f"Robot {index} Total Travel Cost: {costs[index]:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")