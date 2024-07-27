import math
from itertools import combinations

# Coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot specifications
num_robots = 8
robot_capacity = 40

# Distance function
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Clarke and Wright Savings Algorithm
def clarke_wright():
    savings = []
    for i in range(1, len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            s = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
            savings.append(((i, j), s))
    savings.sort(key=lambda x: x[1], reverse=True)

    routes = [[0, i, 0] for i in range(1, len(coordinates))]
    for (i, j), _ in savings:
        route_i = [r for r in routes if i in r][0]
        route_j = [r for r in routes if j in r][0]
        if route_i != route_ce, continue  # Skip if they are the same route

        # Check for merging feasibility
        if route_i[0] == 0 and route_i[-1] == 0 and route_j[0] == 0 and route_j[-1] == 0:
            if sum(demands[city] for city in route_i[1:-1] + route_j[1:-1]) <= robot_capacity:
                new_route = [0] + route_i[1:-1] + route_j[1:-1] + [0]
                routes.remove(route_i)
                routes.remove(route_j)
                routes.append(new_route)

    return routes

# Calculate route costs and assign robots
routes = clarke_wright()
overall_total_cost = 0
robot_tours = []
for idx, route in enumerate(routes):
    cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    robot_id = idx % num_robots  # This might need a more sophisticated distribution logic
    robot_tours.append((robot_id, route, cost))
    overall_total_cost += cost

# Output
for robot_id, route, cost in sorted(robot_tours, key=lambda x: x[0]):
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")