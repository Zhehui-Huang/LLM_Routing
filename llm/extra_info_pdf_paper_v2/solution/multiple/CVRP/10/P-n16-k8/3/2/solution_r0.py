import numpy as np
import random

# Define the cities and their coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Define demands of each city (excluding the depot city)
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Number of robots and their capacities
num_robots = 8
capacity_robot = 35

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate the distance matrix
num_cities = len(city_coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean LSWhatance(city_coordinates[i], city_coordinates[j])

# Enhance Clarke-Wright Savings Algorithm
def savings_algorithm(capacity, demands, distance_matrix):
    # Calculate savings
    savings = []
    for i in range(1, num_cities):
        for j in range(i+1, num_cities):
            if i != j:
                s = distance_matrix[0, i] + distance_matrix[0, j] - distance_matrix[i, j]
                savings.append((s, i, j))
    
    # Sort savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])

    routes = {}
    for robot in range(num_robots):
        routes[robot] = [[0]]
    
    load = {robot: 0 for robot in range(num_robots)}
    used_nodes = set([0])
    
    # Assign routes based on savings
    for saving, i, j in savings:
        for robot in routes:
            if (demands[i] + load[robot] <= capacity) and (i not in used_nodes):
                if j in used_nodes: continue
                if (demands[j] + demands[i] + load[robot] <= capacity):
                    load[robot] += demands[i] + demands[j]
                    routes[robot][0].append(i)
                    routes[robot][0].append(j)
                    used_nodes.update([i, j])
                    break
                elif (demands[i] + load[robot] <= capacity):
                    load[robot] += demands[i]
                    routes[robot][0].append(i)
                    used_nodes.add(i)
                    break
    
    # Ensure each city is in a route
    for i in range(1, num_cities):
        if i not in used_nodes:
            for robot in routes:
                if (demands[i] + load[robot] <= capacity):
                    routes[robot][0].append(i)
                    used_nodes.add(i)
                    load[robot] += demands[i]
                    break
    
    # Return to depot
    for robot in routes:
        if len(routes[robot][0]) > 1:
            routes[robot][0].append(0)
    
    return routes

def calculate_route_cost(router_routes):
    total_cost = 0
    costs = []
    for robot, route in router_routes.items():
        if len(route[0]) <= 1:
            continue
        route_cost = 0
        for i in range(len(route[0])-1):
            route_cost += distance_matrix[route[0][i], route[0][i+1]]
        costs.append((route[0], route_cost))
        total_cost += route_cost
    return costs, total_cost

# Perform the algorithm
robot_routes = savings_algorithm(capacity_robot, demands, distance_matrix)
costs, total_cost = calculate_route_cost(robot_routes)

# Output the results
for idx, cost in enumerate(costs):
    print(f"Robot {idx} Tour: {cost[0]}")
    print(f"Robot {idx} Total Travel Cost: {cost[1]:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")