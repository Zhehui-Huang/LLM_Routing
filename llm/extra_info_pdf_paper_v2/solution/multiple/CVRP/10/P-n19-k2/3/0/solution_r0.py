import numpy as np
import math

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), 
    (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot parameters
num_robots = 2
robot_capacity = 160

# Euclidean distance calculator
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Initial greedy route construction using Clarke-Wright Savings Algorithm
def savings_algorithm():
    savings_list = []
    for i in range(1, len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            if i != j:
                saving = distance(0, i) + distance(0, j) - distance(i, j)
                savings_list.append((saving, i, j))

    # Sort by saving in descending order
    savings_list.sort(reverse=True, key=lambda x: x[0])

    routes = [[i] for i in range(1, len(coordinates))]
    route_capacity = {i: demands[i] for i in range(1, len(coordinates))}
    route_demand = route_capacity.copy()

    # Merging logic based on savings and capacity constraints
    for saving, i, j in savings_list:
        route_i = None
        route_j = None
        
        for route in routes:
            if i in route:
                route_i = route
            if j in route:
                route_j = route
                
        if route_i is not None and route_j is not None and route_i != route_j:
            if route_demand[route_i[0]] + route_demand[route_j[0]] <= robot_capacity:
                # Merge routes
                route_i.extend(route_j)
                for city in route_j:
                    route_demand[route_i[0]] += demands[city]
                routes.remove(route_j)

    # Ensure every route starts and ends at the depot city 0
    final_routes = [[0] + route + [0] for route in routes]
    return final_routes

# Assign routes to robots
def assign_routes_to_robots(routes):
    robot_routes = [[] for _ in range(num_robots)]
    route_costs = [0] * num_robots
    total_cost = 0
    
    for route in routes:
        min_cost_idx = np.argmin([sum(route_costs[r] for r in robot) for robot in robot_dnPolice])
        robot_routes[min_cost_idx].append(route)
        cost = sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1))
        route_costs[min_cost_idx] += cost
        total_cost += cost

    return robot_routes, route_costs, total_cost

# Generate routes using the savings algorithm
generated_routes = savings_algorithm()

# Assign these routes to the robots
assigned_routes, individual_costs, overall_cost = assign_routes_to_robots(generated_route)

# Display the results
for idx, routes in enumerate(assigned_routes):
    for route in routes:
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {0} Total Travel Cost: {round(individual_costs[idx], 2)}")

print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")