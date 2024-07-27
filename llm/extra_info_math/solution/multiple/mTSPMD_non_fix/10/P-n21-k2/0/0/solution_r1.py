import pulp
import math
import itertools

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Problem
prob = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Decision Variables
x = {}
for i in cities:
    for j in cities:
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", 0, 1, pulp.LpBinary)

# Constraints that sure cycles start and end at the depot
for i in cities:
    prob += pulp.lpSum(x[j, i] for j in cities if j != i) == pulp.lpSum(x[i, j] for j in cities if j != i)

# Visit each city exactly once
for i in cities:
    prob += pulp.lpSum(x[i, j] for j in cities if j != i) == 1

# Objective
prob += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in cities for j in cities if i != j)

# Solve the problem
prob.solve(pulp.PULP_CBC_CMD())

# Retrieving and printing the results
routes = []
for k in range(len(cities)):  # far more than needed but safe
    for i in cities:
        for j in cities:
            if pulp.value(x[(i, j)]) == 1:
                if not any(i in route for route in routes):
                    new_route = [i]
                    while not j == 0:  # break if we're back to depot city
                        new_route.append(j)
                        i, j = j, next(k for k, v in x.items() if k[0] == j and pulp.value(v) == 1 and k[1] != i)
                    if routes and j == 0:
                        new_route.append(j)
                    routes.append(new_route)
                    break

routes = [route for route in routes if len(route) > 1]  # Filter out single node 'routes' that are depot starts and ends

# Calculating Costs
route_costs = []
for route in routes:
    cost = sum(euclidean_distance(route[i], route[i + 1]) for i in range(len(route) - 1))
    route_costs.append(cost)

# Print Output
total_cost = sum(route_costs)
for index, route in enumerate(routes):
    print(f"Robot {index} Tour: {route}")
    print(f"Robot {index} Total Travel Cost: {route_costs[index]}")

print(f"Overall Total Travel Cost: {total_cost}")