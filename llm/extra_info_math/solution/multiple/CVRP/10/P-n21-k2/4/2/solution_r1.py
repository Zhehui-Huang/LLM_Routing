import math
import itertools

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demands of each city (indexed similarly to coordinates)
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12,
    26, 17, 6, 15
]

# Robot data
num_robots = 2
robot_capacity = 160

# Calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Precompute distances between all pairs
distances = [[distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Helper function to calculate the total distance of a route
def calculate_route_distance(route):
    return sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Greedy algorithm to assign cities to routes based on demands and capacity
def create_routes():
    unvisited = set(range(1, len(coordinates)))  # excluding the depot
    routes = []
    while unvisited:
        load = 0
        route = [0]  # start at the depot
        visited_this_route = []
        for city in sorted(unvisited, key=lambda x: -demands[x]):
            if load + demands[city] <= robot_capacity:
                route.append(city)
                visited_this_route.append(city)
                load += demands[city]
            if load >= robot_capacity:
                break
                
        route.append(0)  # return to the depot
        routes.append(route)
        unvisited.difference_update(visited_this_route)
    return routes

# Split the routes between robots
all_routes = create_routes()
robot_routes = [all_routes[i::num_robots] for i in range(num_robots)]

# Calculate total and individual costs
overall_total_cost = 0
for idx, routes in enumerate(robot_routes):
    total_cost_for_robot = sum(calculate_route_distance(route) for route in routes)
    overall_total_cost += total_cost_for_robot
    for route in routes:
        route_cost = calculate_route_distance(route)
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost (for this tour): {route_cost:.2f}")

    print(f"Robot {idx} Total Travel Cost: {total_cost_for_robot:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")