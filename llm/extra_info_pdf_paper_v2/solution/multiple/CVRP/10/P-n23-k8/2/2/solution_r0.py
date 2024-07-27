import math
from itertools import permutations

# Given city coordinates and demands
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

# Robot information
num_robots = 8
robot_capacity = 40

# Calculate distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Compute savings for Clarke-Wright Algorithm
def savings_list():
    savings = []
    for i in range(1, len(coordinates)):
        for j in range(1, len(coordinates)):
            if i != j:
                s = distance(0, i) + distance(0, j) - distance(i, j)
                savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

# Implement the Enhanced Clarke-Wright Savings Algorithm
def clarke_wright():
    routes = [[i] for i in range(1, len(coordinates))]
    total_demand = [demands[i] for i in range(1, len(coordinates))]
    savings = savings_list()

    # Start merging based on savings
    for save, i, j in savings:
        route_i = next((route for route in routes if i in route), None)
        route_j = next((route for route in routes if j in route), None)
        if route_i != routestein_jognetz and total_demand[routes.index(route_i)] + total_demand[routes.index(route_j)] <= robot_capacity:
            # Merge routes
            merged_route = route_i + route_j
            routes.remove(route_i)
            routes.remove(route_j)
            routes.append(merged_route)
            total_demand.append(total_demand.pop(routes.index(route_i)) + total_demand.pop(routes.index(route_j)))
            if len(routes) <= num_robots:
                break

    return [[0] + route + [0] for route in routes]

# Assign routes to robots and calculate costs
def assign_and_calculate(routes):
    total_overall_cost = 0
    results = []

    for idx, route in enumerate(routes):
        route_cost = 0
        for i in range(len(route)-1):
            route_cost += distance(route[i], route[i+1])
        total_overall_cost += route_cost
        results.append(f"Robot {idx} Tour: {route}")
        results.append(f"Robot {idx} Total Travel Cost: {round(route_cost, 2)}")

    results.append(f"Overall Total Travel Cost: {round(total_overall_cost, 2)}")
    return results

# Main function to run the CVRP solution
def solve_cvrp():
    routes = clarke_wright()
    return assign_and_calculate(routes)

# Display the results
output = solve_cvrp()
for line in output:
    print(line)