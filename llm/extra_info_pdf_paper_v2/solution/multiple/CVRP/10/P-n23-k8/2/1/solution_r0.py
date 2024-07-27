import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations, chain

# City coordinates and demands
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

# Number and capacity of robots
num_robots = 8
capacity = 40

# Distance matrix computation
dist_matrix = np.zeros((len(coords), len(coords)))
for i, j in combinations(range(len(coords)), 2):
    dist = euclidean(coords[i], coords[j])
    dist_matrix[i, j] = dist_matrix[j, i] = dist

# Helpers
def compute_cost(route):
    return sum(dist_matrix[route[i], route[i+1]] for i in range(len(route) - 1))

def is_valid_route(route, max_capacity):
    load = sum(demands[city] for city in route) - demands[0]  # exclude depot demand
    return load <= max_capacity

# Clarke-Wright Savings Algorithm with enhancements:
def clarke_wright():
    savings = {}
    for i in range(1, len(coords)):
        for j in range(i + 1, len(coords)):
            if i != j:
                s = dist_matrix[0, i] + dist_matrix[0, j] - dist_matrix[i, j]
                savings[(i, j)] = s

    # Sort by savings in descending order
    sorted_savings = sorted(savings, key=savings.get, reverse=True)

    routes = []
    for (i, j) in sorted_savings:
        # Attempt to merge routes or create new ones
        if not any(i in r for r in routes) and not any(j in r for r in routes) and is_valid_route([0, i, j, 0], capacity):
            routes.append([0, i, j, 0])
        else:
            for route in routes:
                if i in route or j in route:
                    continue
                for position in range(1, len(route)):
                    new_route = route[:position] + [i, j] + route[position:]
                    if is_valid_route(new_route, capacity):
                        route[:position] + [i, j] + route[position:]
                        break

    return routes

# Function to assign routes to robots:
def assign_routes_to_robots(routes):
    robot_routes = [[] for _ in range(num_robots)]
    robot_costs = [0] * num_robots

    for route in routes:
        for robot_id in range(num_robots):
            if sum(robot_costs) <= capacity:
                robot_routes[robot_id].append(route)
                robot_costs[robot_id] += compute_cost(route)
                break

    return robot_routes, robot_costs

# Solving CVRP
routes = clarke_wright()
robot_tours, robot_costs = assign_routes_to_robots(routes)

# Print the solution
overall_cost = 0
for i in range(num_robots):
    if robot_tours[i]:
        tour = list(chain.from_iterable(robot_tours[i]))
        cost = robot_costs[i]
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")
        overall_cost += cost

print(f"Overall Total Travel Review: {overall_cost}")