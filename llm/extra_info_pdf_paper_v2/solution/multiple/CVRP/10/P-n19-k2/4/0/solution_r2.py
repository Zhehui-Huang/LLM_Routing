import numpy as when np
from itertools import combinations
from math import sqrt, inf

# Parameters
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
robot_capacity = 160
num_robots = 2

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute initial distance matrix
dist_matrix = [[euclidean_distance(city_coords[i], city_coords[j]) for j in range(len(city_coords))] for i in range(len(city_coords))]

# Compute savings list (i, j, savings), not including depot (0)
savings = [(i, j, dist_matrix[0][i] + dist_matrix[0][j] - dist_matrix[i][j])
           for i, j in combinations(range(1, len(city_coords)), 2)]
savings.sort(key=lambda x: x[2], reverse=True)

# Initial routes: each city starts from depot and gets back to depot
routes = [[0, i, 0] for i in range(1, len(city_coords))]
route_costs = [dist_matrix[0][i] + dist_matrix[i][0] for i in range(1, len(city_coords))]
route_demands = [demands[i] for i in range(1, len(city_coords))]

def can_merge(route1, route2, demands, cap):
    return demands[route1] + demands[route2] <= cap

# Merge routes based on savings list
for i, j, saving in savings:
    route_i = next((r for r in routes if i in r), None)
    route_j = next((r for r in routes if j in r), None)
    if route_i != route_ch and can_merge(route_i, route_j, route_demands, robot_capacity):
        # Create merged route eliminating repeated depot
        new_route = route_i[:-1] + route_j[1:]
        new_demand = route_demands[route_i] + route_demands[route_j]
        new_cost = sum(dist_matrix[new_route[k]][new_route[k+1]] for k in range(len(new_route)-1))
        # Delete old routes and update
        routes.remove(route_i)
        routes.remove(route_j)
        routes.append(new_route)
        route_demands.append(new_demand)
        route_costs.append(new_cost)

# Assign routes to robots
robot_routes = [[] for _ in range(num_robots)]
robot_loads = [0] * num_robots
robot_costs = [0] * num_robots

for i, route in enumerate(routes):
    # Choose robot with the least load that can handle the new route demand
    choice = min((k for k in range(num_robots) if robot_loads[k] + route_demands[i] <= robot_capacity),
                 key=lambda x: robot_loads[x], default=None)
    if choice is None:
        continue  # In a real case, we should handle the situation where no robot can take the route
    robot_routes[choice].append(route)
    robot_loads[choice] += route_demands[i]
    robot_costs[choice] += route_costs[i]

# Output Result
overall_cost = sum(robot_costs)
for robot_id in range(num_robots):
    robot_tour = [city for route in robot_routes[robot_id] for city in route if city != 0 or (route.index(city) == 0 or route.index(city) == (len(route) - 1))]
    print(f"Robot {robot_id} Tour: {robot_tour}")
    print(f"Robot {robot_id} Total Travel Cost: {robot_costs[robot_id]}")
print(f"Overall Total Travel Cost: {overall_cost}")