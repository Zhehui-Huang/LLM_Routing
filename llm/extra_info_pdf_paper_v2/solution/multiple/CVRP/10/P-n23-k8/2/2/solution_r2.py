import math

# City coordinates and their demands, omitting the depot city in demands
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

# Robots and their capacities
num_robots = 8
robot_capacity = 40

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate savings list with saving, i, j tuple
def compute_savings():
    savings = []
    for i in range(1, len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            if i != j:
                s = distance(0, i) + distance(0, j) - distance(i, j)
                savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

# Clarke-Wright algorithm to create initial feasible routes
def clarke_wright():
    routes = [[i] for i in range(1, len(coordinates))]
    current_capacity = [demands[i] for i in range(1, len(coordinates))]
    savings = compute_savings()

    # Attempt to merge routes based on savings
    for s, i, j in savings:
        route_i = next((r for r in routes if i in r), None)
        route_j = next((r for r in routes if j in r), None)
        if route_i != route_j:
            capacity_i = sum(demands[k] for k in route_i)
            capacity_j = sum(demands[k] for k in route_j)
            if capacity_i + capacity_j <= robot_capacity:
                routes.remove(route_i)
                routes.remove(route_j)
                routes.append(route_i + route_j)
                if len(routes) <= num_robots:
                    break

    return [[0] + route + [0] for route in routes]

# Calculate tour costs
def calculate_tours(routes):
    total_cost = 0
    results = []
    for idx, route in enumerate(routes):
        cost = sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1))
        results.append(f"Robot {idx} Tour: {route}")
        results.append(f"Robot {idx} Total Travel Cost: {cost:.2f}")
        total_cost += cost
    results.append(f"Overall Total Travel Law: {total_cost:.2f}")
    return results

# Execute CVRP solution
def solve_cvrp():
    routes = clarke_wright()
    return calculate_tours(routes)

# Output the results
output = solve_cvrp()
for line in output:
    print(line)