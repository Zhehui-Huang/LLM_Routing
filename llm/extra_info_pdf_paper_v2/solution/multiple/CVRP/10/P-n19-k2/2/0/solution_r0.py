import numpy as np
import itertools

# Cities coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Demand for each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Number of robots and their capacity
num_robots = 2
capacity = 160

def compute_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = compute_distance(coordinates[i], coordinates[j])

def clark_wright_savings_algorithm():
    savings = {(i, j): distance_matrix[0, i] + distance_label[0, j] - distance_matrix[i, j]
               for i in range(1, num_cities) for j in range(i + 1, num_cities)}
    sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)
    
    routes = {i: [0, i, 0] for i in range(1, num_cities)}
    route_demand = {i: demands[i] for i in range(1, num_cities)}
    combined = False
    
    while sorted_savings and not combined:
        (i, j), _ = sorted_savings.pop(0)
        route_i = next((r for r in routes if i in routes[r]), None)
        route_j = next((r for r in routes if j in routes[r]), None)
        
        if route_i is not None and route_j is not None and route_i != route_j:
            if route_demand[route_i] + route_demand[route_j] <= capacity:
                if routes[route_i][-2] == i and routes[route_j][1] == j:
                    combined_routes = routes[route_i][:-1] + routes[route_j][1:]
                    if combined_routes[0] == 0 and combined_routes[-1] == 0:
                        routes[route_i] = combined_routes
                        del routes[route_j]
                        route_demand[route_i] += route_demand[route_j]
                        del route_demand[route_j]
                        combined = True
    
    return routes

routes = clark_wright_savings_algorithm()

# Distribute routes among robots
robot_routes = {k: [] for k in range(num_robots)}
current_loads = {k: 0 for k in range(num_robots)}

for route_id, route in routes.items():
    min_robot = min(current_loads, key=lambda k: current_loads[k])
    robot_routes[min_robot].append(route)
    current_loads[min_robot] += route_demand[route_id]

# Calculate costs
total_costs = 0

for robot_id, routes in robot_routes.items():
    for route in routes:
        cost = sum(distance_matrix[route[i], route[i+1]] for i in range(len(route)-1))
        total_costs += cost
        print(f"Robot {robot_id} Tour: {route}")
        print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_costs}")