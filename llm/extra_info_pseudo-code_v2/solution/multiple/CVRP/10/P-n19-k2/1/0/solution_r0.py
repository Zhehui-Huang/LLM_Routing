import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations

# Data for the cities
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
robot_capacity = 160
num_robots = 2

# Computing the cost matrix (Euclidean distances)
def compute_cost_matrix(coords):
    num_cities = len(coords)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = euclidean(coords[i], coords[j])
    return matrix

cost_matrix = compute_cost_matrix(coordinates)

# Clarke-Wright Savings Algorithm
def clarke_wright_savings(depot, demands, cost_matrix, capacity):
    def calculate_savings():
        savings = []
        n = len(cost_matrix)
        for i in range(1, n):
            for j in range(i + 1, n):
                if i != j and i != depot and j != depot:
                    s = cost_matrix[depot][i] + cost_matrix[depot][j] - cost_matrix[i][j]
                    savings.append((s, i, j))
        return sorted(savings, reverse=True, key=lambda x: x[0])

    def can_merge(route1, route2, demands, capacity):
        demand_route1 = sum(demands[c] for c in route1)
        demand_route2 = sum(demands[c] for c in route2)
        return demand_route1 + demand_route2 <= capacity

    routes = [ [0, i, 0] for i in range(1, len(cost_matrix)) if demands[i] <= capacity ]
    savings = calculate_savings()

    for saving, i, j in savings:
        for r1 in range(len(routes)):
            if i in routes[r1]:
                for r2 in range(len(routes)):
                    if j in routes[r2] and r1 != r2:
                        if routes[r1][-2] == i and routes[r2][1] == j:
                            if can_merge(routes[r1], routes[r2], demands, capacity):
                                routes[r1] = routes[r1][:-1] + routes[r2]
                                routes.pop(r2)
                                break

    return routes

routes = clarke_wright_savings(0, demands, cost_matrix, robot_capacity)

# Assigning routes to vehicles
def assign_routes_to_vehicles(routes, num_vehicles):
    # Simple greedy assignment (improvements might be needed for load balancing)
    vehicle_routes = {k: [] for k in range(num_vehicles)}
    vehicle_loads = {k: 0 for k in range(num_vehicles)}
    for route in sorted(routes, key=lambda x: -len(x)):
        assigned = False
        for v in range(num_vehicles):
            if sum(demands[city] for city in route[1:-1]) + vehicle_loads[v] <= robot_capacity:
                vehicle_routes[v].append(route)
                vehicle_loads[v] += sum(demands[city] for city in route[1:-1])
                assigned = True
                break
        if not assigned:
            print("Could not assign all routes within vehicle capacities!")

    return vehicle_routes

vehicle_routes = assign_routes_to_vehicles(routes, num_robots)

# Display plan
def display_plan(vehicle_routes):
    overall_cost = 0
    for v, routes in vehicle_routes.items():
        for route in routes:
            cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
            overall_cost += cost
            print(f"Robot {v} Tour: {route}")
            print(f"Robot {v} Total Travel Cost: {cost}")
    print(f"Overall Total Travel Cost: {overallTranslation Cost: {overall_cost}")

display_plan(vehicle_routes)