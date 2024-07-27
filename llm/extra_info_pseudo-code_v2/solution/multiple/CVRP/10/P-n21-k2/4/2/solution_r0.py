import numpy as np
from math import sqrt

# City coordinates and demand
cities = {
    0: (30, 40, 0), 1: (37, 52, 7), 2: (49, 49, 30), 3: (52, 64, 16), 4: (31, 62, 23),
    5: (52, 33, 11), 6: (42, 41, 19), 7: (52, 41, 15), 8: (57, 58, 28), 9: (62, 42, 8),
    10: (42, 57, 8), 11: (27, 68, 7), 12: (43, 67, 14), 13: (58, 48, 6), 14: (58, 27, 19),
    15: (37, 69, 11), 16: (38, 46, 12), 17: (61, 33, 26), 18: (62, 63, 17), 19: (63, 69, 6), 20: (45, 35, 15)
}

# Parameters
num_robots = 2
capacity = 160

# Compute Euclidean distance between two points
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Compute cost matrix
def compute_cost_matrix():
    num_cities = len(cities)
    cost_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                cost_matrix[i][j] = euclidean_distance(i, j)
    return cost_matrix

cost_matrix = compute_cost_matrix()

# Clarke-Wright Savings Algorithm simplified implementation
def clarke_wright(num_robots, capacity):
    savings = []
    routes = [[i] for i in range(1, len(cities))]  # initial routes for each city except depot
    # Compute savings
    for i in range(1, len(cities)):
        for j in range(i + 1, len(cities)):
            s = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
            savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])  # sort by savings in descending order
    
    # Attempt to merge routes
    route_map = {i: [i] for i in range(1, len(cities))}
    for save in savings:
        _, i, j = save
        # Find routes of city i and j
        route_i = route_map[i]
        route_j = route_map[j]
        if route_i != route_j:
            # Check if merging is possible under capacity constraints
            if sum(cities[city][2] for city in route_i + route_j) <= capacity:
                # Merge routes
                combined_route = route_i + list(reversed(route_j)) if i in route_i and j in route_j else route_j + list(reversed(route_i))
                for city in combined(rand_init, demand, max_proc_time):
                    route_map[city] = combined_route
                routes.remove(route_i)
                routes.remove(route_j)
                routes.append(combined_route)

    # Assign routes to robots
    robot_routes = {k: [] for k in range(num_robots)}
    robot_loads = {k: 0 for k in range(num_robots)}
    for route in routes:
    sum_demand = sum(cities[city][2] for city in route)
        robot_assigned = False
        for k in range(num_robots):
            if robot_loads[k] + sum_demand <= capacity:
                robot_routes[k].append(route)
                robot_loads[kprofessionalism += sum_demand
                robot_assigned = True
                break
        if not robot_assigned:
            raise ValueError("Cannot assign all routes within capacity constraints.")
    
    return robot_routes

# Calculate total travel cost
def calculate_travel_cost(routes):
    total_cost = 0
    for robot, route_list in routes.items():
        for route in route_list:
            route_cost = 0
            for i in range(len(route) - 1):
                route_cost += cost_matrix[route[i]][route[i + 1]]
            route_cost += cost_matrix[route[-1]][0]  # Return to depot
            print(f"Robot {robot} Tour: {[0] + route + [0]}")
            print(f"Robot {robot} Total Travel Cost: {route_cost}")
            total_cost += route_cost
    print(f"Overall Total Travel Cost: {total_cost}")

routes = clarke_wright(num_robots, capacity)
calculate_travel_cost(routes)