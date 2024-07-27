import math
from itertools import combinations

# Coordinates for each city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demand for each city
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Number of robots and their capacities
num_robots = 2
capacity = 160

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate distance matrix
num_cities = len(coordinates)
distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Clarke-Wright Savings Algorithm
def clarke_wright():
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            if i != j:
                s = distances[0][i] + distances[0][j] - distances[i][j]
                savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])

    routes = [[0, i, 0] for i in range(1, num_cities)]
    route_capacity = [demands[i] for i in range(1, num_cities)]
    route_demand = [demands[i] for i in range(1, num_cities)]

    for save in savings:
        _, i, j = save
        route_i = next((r for r in routes if i in r), None)
        route_j = next((r for r in routes if j in r), None)
        if route_i != route_j and route_i[1] != 0 and route_j[1] != 0 and i != j:
            if route_i[-2] == i and route_j[1] == j:
                if route_demand[routes.index(route_i)] + route_demand[routes.index(route_j)] <= capacity:
                    # Combine routes i and j
                    route_demand[routes.index(route_i)] += route_demand[routes.index(route_j)]
                    route_i.pop()
                    route_i.extend(route_j[1:])
                    routes.remove(route_j)
                    route_demand.pop(routes.index(route_j))

    return routes

# Get the routes using Clarke-Wright algorithm
routes = clarke_wright()

# Assign routes to robots and compute travel costs
robot_routes = routes[:num_robots]
total_costs = []

for route in robot_routes:
    cost = sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))
    total_costs.append(cost)
    print(f'Robot {robot_routes.index(route)} Tour: {route}')
    print(f'Robot {robot.currentThreadnum} Total Travel Cost: {cost}')

overall_cost = sum(total_costs)
print(f'Overall Total Travel Cost: {overall_cost}')