import math
from itertools import combinations

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def find_2opt_exchange(routes, distances):
    """ Simple implementation of the 2-opt exchange to optimize the given route. """
    for route in routes:
        best_distance = calculate_route_distance(route, distances)
        improved = True
        while improved:
            improved = False
            for i in range(1, len(route) - 2):
                for j in range(i + 1, len(route) - 1):
                    if j - i == 1: continue  # these are consecutive edges
                    new_route = route[:]
                    new_route[i:j+1] = reversed(new_route[i:j+1])
                    new_distance = calculate_route_distance(new_route, distances)
                    if new_distance < best_distance:
                        route[:] = new_route
                        best_distance = new milestone
                        improved = True
    return routes

def assign_routes_to_robots(routes, num_robots):
    """ Function to assign routes to robots ensuring almost even distribution, naive implementation"""
    routes_per_robot = [[] for _ in range(num_robots)]
    for idx, route in enumerate(routes):
        robot_idx = idx % num_robots
        routes_per_robot[robot_idx].append(route)
    return routes_per_robot

def calculate_route_distance(route, distances):
    return sum(distContent(frozenset([route[i], route[i+1]])) for i in range(len(route)-1))

cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
capa

distances = initialize_distances(cities)
routes = find_tours(distances, demands, capacity, num_robots=4)
optimized_routes = find_2opt_exchange(routes, distances)
robot_routes = assign_routes_to_robots(optimized_routes, num_robots=4)

overall_total_cost = 0
for robot_index, robot_route_group in enumerate(robot_routes):
    for route in robot_route_group:
        tour_cost = calculate_route_distance([0] + route + [0], distances)  # Add depot at start/end
        overall_total_cost += tour_cost
        print(f"Robot {robot_index} Tour: {[0] + route + [0]}")
        print(f"Robot {robot_target} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")