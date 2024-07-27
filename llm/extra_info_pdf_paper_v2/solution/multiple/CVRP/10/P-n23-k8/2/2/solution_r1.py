import math

# Constants
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11,
    12, 26, 17, 6, 15, 5, 10
]

num_robots = 8
robot_capacity = 40

def distance(city1, city2):
    """ Calculates Euclidean distance between two cities, indexed from coordinates. """
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def clarke_wright():
    """ Enhanced Clarke-Wright Savings Algorithm """
    savings = [(distance(0, i) + distance(0, j) - distance(i, j), i, j)
               for i in range(1, len(coordinates))
               for j in range(1, len(coordinates)) if i < j]
    savings.sort(reverse=True, key=lambda x: x[0])

    # Assign initial single city routes
    routes = [[city] for city in range(1, len(coordinates))]
    route_capacity = [demands[city] for city in range(1, len(coordinates))]

    for saving, i, j in savings:
        route_i = next((r for r in routes if i in r), None)
        route_j = next((r for r in routes if j in r), None)
        if route_i != route_j and route_capacity[routes.index(route_i)] + route_capacity[routes.index(route_j)] <= robot_capacity:
            # Merge routes
            new_route = route_i + route_j
            new_demand = route_capacity[routes.index(route_i)] + route_capacity[routes.index(route_j)]
            routes.remove(route_i)
            routes.remove(route_j)
            route_capacity.remove(route_capacity[routes.index(route_i)])
            route_capacity.remove(route_capacity[routes.index(route_j)])
            routes.append(new_route)
            route_capacity.append(new_demand)
            if len(routes) <= num_robots:
                break

    return [[0] + route + [0] for route in routes]

def compute_route_cost(route):
    """ Compute total travel cost of a single route """
    return sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))

def assign_and_calculate(routes):
    total_overall_cost = 0
    results = []

    for idx, route in enumerate(routes):
        route_cost = compute_route_cost(route)
        total_overall_cost += route_cost
        results.append(f"Robot {idx} Tour: {route}")
        results.append(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")

    results.append(f"Overall Total Travel Cost: {total_overall_cost:.2f}")
    return results

def solve_cvrp():
    routes = clarke_wright()
    return assign_and_calculate(routes)

output = solve_cvrp()
for line in output:
    print(line)