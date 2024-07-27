import random
from math import sqrt

# Parameters
cities_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
num_robots = 2
robot_capacity = 160
num_cities = len(cities_coordinates)

def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_savings():
    savings = []
    d0 = [euclidean_distance(0, i) for i in range(num_cities)]
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            s = d0[i] + d0[j] - euclidean_distance(i, j)
            savings.append((s, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

def merge_routes(routes, savings):
    route_map = {i: [i] for i in range(num_cities)}
    for s, i, j in savings:
        route_i = route_map[i]
        route_j = route_map[j]
        if route_i is not route_j:
            demand_i = sum(demands[k] for k in route_i)
            demand_j = sum(demains[k] for k in route_j)
            if demand_i + demand_j <= robot_capacity:
                route_i.extend(route_j)
                for k in route_j:
                    route_map[k] = route_i
                demands[i] += demands[j]
    return list(set(map(tuple, route_map.values())))

def calculate_route_cost(route):
    cost = euclidean_distance(0, route[0])
    for i in range(len(route) - 1):
        cost += euclidean_distance(route[i], route[i+1])
    cost += euclidean_distance(route[-1], 0)
    return cost

# Main execution flow
savings_list = calculate_savings()
initial_routes = [[i] for i in range(1, num_cities)]  # start from city 0 (depot)
merged_routes = merge_routes(initial_routes, savings_list)
route_costs = [calculate_route_cost(route) for route in merged_routes]

# Calculate assignments to robots and total travel cost
total_cost = sum(route_costs)
robot_assignment = []
loads = [0] * num_robots
for i, route in enumerate(merged_routes):
    assigned_robot = min(range(num_robots), key=lambda k: loads[k])
    loads[assigned_robot] += sum(demands[city] for city in route)
    robot_assignment.append(assigned_robot)

# Output results
for robot in range(num_robots):
    robot_routes = [merged_routes[i] for i in range(len(merged_routes)) if robot_assignment[i] == robot]
    robot_cost = sum(route_costs[i] for i in range(len(route_costs)) if robot_assignment[i] == robot)
    print(f"Robot {robot} Tour: {[0] + [city for route in robot_routes for city in route] + [0]}")
    print(f"Robot {robot} Total Travel Cost: {robot_cost}")

print("Overall Total Travel Cost:", total_cost)