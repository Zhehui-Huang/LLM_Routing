import math
import random

# Defining the cities and their demands
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), 
          (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
num_robots = 2
robot_capacity = 160

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate initial distances
distances = {}
for i in range(len(cities)):
    for j in range(len(cities)):
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Calculate savings
savings = {}
for i in range(1, len(cities)):
    for j in range(i + 1, len(cities)):
        savings[(i, j)] = distances[(0, i)] + distances[(0, j)] - distances[(i, j)]

# Sorting savings in descending order
sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)

# Initialize routes - each non-depot city starts on its own route
routes = {i: [0, i, 0] for i in range(1, len(cities))}

# Clarke-Wright algorithm with capacity constraint
for ((i, j), saving) in sorted_savings:
    # Find routes containing cities i and j
    route_i = None
    route_j = None

    for route_id, route in routes.items():
        if i in route:
            route_i = route_id
        if j in route:
            route_j = route_id
            
    if route_i != route_j and None not in (route_i, route_j):
        # Check if can merge without exceeding capacity
        demand_i = sum(demands[k] for k in routes[route_i] if k != 0)
        demand_j = sum(demands[k] for k in routes[route_j] if k != 0)
        if demand_i + demand_j <= robot_capacity:
            # Merge routes
            new_route = routes[route_i][:-1] + routes[route_j][1:]
            if routes[route_i][1] == i and routes[route_j][-2] == j:
                routes[route_i] = new_route
                del routes[route_j]
            elif routes[route_j][1] == i and routes[route_i][-2] == j:
                routes[route_j] = new_route
                del routes[route_i]

# Assign routes to robots
robot_routes = list(routes.values())[:num_robots]

# Calculate the cost of each route
robot_costs = []
for route in robot_routes:
    cost = sum(distances[(route[i], route[i+1])] for i in range(len(route) - 1))
    robot_costs.append(cost)

# Output results
overall_cost = sum(robot_costs)
for idx, route in enumerate(robot_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {round(robot_costs[idx], 2)}")

print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")