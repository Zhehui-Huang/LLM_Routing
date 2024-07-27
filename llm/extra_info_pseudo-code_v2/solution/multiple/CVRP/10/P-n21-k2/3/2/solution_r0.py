import numpy as np

# Cities coordinates and demand
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19,
    11, 12, 26, 17, 6, 15
]
num_cities = len(coordinates)

# Robots information
num_robots = 2
capacity = 160

def distance(city1, city2):
    """ Compute Euclidean distance between two cities """
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Compute cost matrix
cost_matrix = np.array([[distance(i, j) for j in range(num_cities)] for i in range(num_cities)])

# Implementation of Clarke-Wright Savings Algorithm
def clarke_wright():
    savings = [(i, j, cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j])
               for i in range(1, num_cities) for j in range(i+1, num_cities)]
    savings.sort(key=lambda x: x[2], reverse=True)  # Sort by savings descending

    routes = {i: [0, i, 0] for i in range(1, num_cities)}
    route_demand = {i: demands[i] for i in range(1, num_cities)}
    merged = {}

    for i, j, saving in savings:
        if i in merged and j in merged:
            continue # Both are merged in some route, ignore to prevent cycle
        if i in merged or j in merged:
            # One of them is merged, check capacity constraint
            if i in merged:
                ri = merged[i]
                candidate_route = [j] if route_demand[ri] + demands[j] <= capacity else None
            else:
                ri = merged[j]
                candidate_route = [i] if route_demand[ri] + demands[i] <= capacity else None
            
            if candidate_route is not None:
                # Add node to existing route
                routes[ri] = [0] + routes[ri][1:-1] + candidate_route + [0]
                route_demand[ri] += demands[candidate_route[0]]
                merged[candidate_route[0]] = ri

        else:
            # Neither is merged, create new route if demands allow
            if demands[i] + demands[j] <= capacity:
                route_index = len(routes) + 1
                routes[route_index] = [0, i, j, 0]
                route_demand[route_index] = demands[i] + demands[j]
                merged[i] = merged[j] = route_index

    return routes, route_demand

routes, route_demands = clarke_wright()

# Assign routes to robots ensuring demand and capacity constraints are maintained
assigned_routes = [[] for _ in range(num_robots)]
route_costs = [0 for _ in range(num_robots)]
overall_cost = 0

for r, path in routes.items():
    # Find the robot with the minimum added cost to assign this route
    min_extra_cost = float('inf')
    min_index = -1
    route_cost = sum(cost_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
    for k in range(num_robots):
        if sum(route_demands[pa] for pa in assigned_routes[k]) + route_demands[r] <= capacity:
            if route_costs[k] + route_cost < min_extra_cost:
                min_extra_cost = route_costs[k] + route_cost
                min_index = k
    if min_index != -1:
        assigned_routes[min_index].append(r)
        route_costs[min_index] += route_cost
        overall_cost += route_cost

# Output results
for k in range(num_robots):
    print(f"Robot {k} Tour: {routes[assigned_routes[k][0]] if assigned_routes[k] else [0, 0]}")
    print(f"Robot {k} Total Travel Cost: {route_costs[k]}")

print(f"Overall Total Travel Cost: {overall_cost}")