import math
from itertools import combinations

# Coordinates and demands of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Robot information
robot_capacity = 35
n_robots = 8

# Compute Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate cost matrix
def generate_cost_matrix():
    num_cities = len(coordinates)
    return [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Clark-Wright Savings Algorithm
def clarke_wright():
    num_cities = len(coordinates)
    savings_list = []
    cost_matrix = generate_cost_matrix()

    # Calculate savings for each pair (i, j)
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            s = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
            savings_list.append(((i, j), s))

    # Sort savings in descending order
    savings_list.sort(key=lambda x: x[1], reverse=True)
    
    routes = {}
    for robot in range(n_robots):
        routes[robot] = [0]

    robot_loads = {robot: 0 for robot in range(n_robots)}
    used_cities = set()

    for (i, j), _ in savings_list:
        # Assign pairs to routes if possible
        for robot in range(n_robots):
            if robot_loads[robot] + demands[i] + demands[j] <= robot_capacity:
                if i not in used_cities and j not in used_cities:
                    routes[robot].insert(-1, i)
                    routes[robot].insert(-1, j)
                    robot_loads[robot] += demands[i] + demands[j]
                    used_cities.update([i, j])
                    break

    # Close all routes
    for robot in routes:
        if routes[robot][-1] != 0:
            routes[robot].append(0)
    
    return routes

# Get routes
routes = clarke_wright()
cost_matrix = generate_cost_matrix()

# Calculate cost and print output
total_cost = 0
for robot, route in routes.items():
    if len(route) > 2:  # valid route with more than just [0, 0]
        route_cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
        total_cost += route_cost
        print(f"Robot {robot} Tour: {route}")
        print(f"Robot {robot} Total Travel Cost: {route.sort_cost}")

print(f"Overall Total Travel Cost: {total_cost}")