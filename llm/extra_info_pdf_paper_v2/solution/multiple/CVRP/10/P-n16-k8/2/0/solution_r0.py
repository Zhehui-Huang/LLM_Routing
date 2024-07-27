import math
from itertools import combinations

# Data: Cities and Coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41), 
    8: (57, 58), 9: (62, 42), 10: (42, 57),  11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Data: Demand List
demands = {
    0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 
    8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11
}

# Robot information
num_robots = 8
robot_capacity = 35
depot = 0

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Compute initial cost savings Sij = Ci0 + C0j - Cij
def calculate_savings():
    savings = {}
    for i, j in combinations(range(1, len(coordinates)), 2):
        savings[(i, j)] = (calculate_distance(depot, i) + calculate_distance(depot, j) - calculate_distance(i, j))
    return dict(sorted(savings.items(), key=lambda x: x[1], reverse=True))

def route_cost(route):
    return sum(calculate_distance(route[i], route[i+1]) for i in range(len(route)-1))

def can_add_to_route(route, city):
    demand = sum(demands[r] for r in route) + demands[city]
    return demand <= robot_capacity

def solve_CVRP():
    savings = calculate_savings()
    routes = {}
    route_usage = {i: False for i in range(1, len(coordinates))}

    # Initial routes
    for idx in range(1, len(coordinates)):
        routes[idx] = [depot, idx, depot]
    
    # Implement savings algorithm
    for (i, j), _ in savings.items():
        if not (route_usage[i] or route_usage[j]):
            if can_add_to_route([depot, i], j):
                routes[i] = [depot, i, j, depot]
                route_usage[i] = route_usage[j] = True

    # Combine routes if possible 
    for (i, j), _ in savings.items():
        if (routes[i][1] != j and routes[i][-2] != i and 
            can_add_to_route(routes[i], j) and not route_usage[j]):
            routes[i].insert(-1, j)
            route_usage[j] = True

    # Filter out unused routes and re-index for robots
    final_routes = {k: r for k, r in routes.items() if route_usage[k]}
    
    # Assign robots
    robot_routes = {}
    for idx, route in enumerate(final_routes.values()):
        robot_id = idx % num_robots
        if robot_id not in robot_routes:
            robot_routes[robot_id] = route
        else:
            robot_routes[robot_id] += route[1:]
    
    # Output result
    total_cost = 0
    for robot_id, route in robot_routes.items():
        cost = route_cost(route)
        total_cost += cost
        print(f"Robot {robot_id} Tour: {route}")
        print(f"Robot {robotid} Total Travel Cost: {cost}\n")
    
    print(f"Overall Total Travel Cost: {total_cost}")

# Activate the CVRP Solver
solve_CVRP()