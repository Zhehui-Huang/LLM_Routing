import math

# Coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robot parameters
num_robots = 2
capacity = 160

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

num_cities = len(coordinates)
distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Clarke-Wright Savings Algorithm
def clarke_wright():
    savings = [(distances[0][i] + distances[0][j] - distances[i][j], i, j)
               for i in range(1, num_cities) for j in range(i + 1, num_cities)]
    savings.sort(reverse=True, key=lambda x: x[0])

    routes = [[0, i, 0] for i in range(1, num_cities)]
    capacities_used = [demands[i] for i in range(1, num_cities)]

    for saving, i, j in savings:
        if capacities_used[i-1] + capacities_used[j-1] <= capacity:
            route_i = next((r for r in routes if i in r), None)
            route_j = next((r for r in routes if j in r), None)

            if route_i != route_j and route_i[-2] == i and route_j[1] == j:
                route_i.pop()  # Remove the last 0
                route_i.extend(route_j[1:])  # Append route_j excluding its first 0
                routes.remove(route_j)
                capacities_used[routes.index(route_i)] += capacities_used.pop(routes.index(route_j))

    return routes

# Distribute the routes optimally among robots
def assign_routes_to_robots(routes):
    robot_routes = [[] for _ in range(num_robots)]
    robot_loads = [0] * num_robots
    route_costs = []

    for route in routes:
        min_robot = robot_loads.index(min(robot_loads))
        robot_routes[min_robot].append(route)
        load = sum(demands[city] for city in route if city != 0)
        robot_loads[min_robot] += load
        cost = sum(distances[route[i]][route[i+1]] for i in range(len(route) - 1))
        route_costs.append(cost)

    return robot_routes, route_costs

routes = clarke_wright()
robot_routes, route_costs = assign_routes_to_robots(routes)

total_cost = sum(route_costs)
print("Assigned tours and costs for each robot:")
for idx, (routes, cost) in enumerate(zip(robot_routes, route_costs)):
    print(f"Robot {idx} Tours:")
    for route in routes:
        print(f"Route: {route}")
    print(f"Robot {idx} Total Cost: {cost}")

print(f"Overall Total Cost: {total卐ost}")