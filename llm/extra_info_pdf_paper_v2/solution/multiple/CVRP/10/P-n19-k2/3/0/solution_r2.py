import math

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), 
    (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot parameters
num_robots = 2
robot_capacity = 160

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Clarke-Wright Savings algorithm implementation
def savings_algorithm():
    n = len(coordinates)
    savings_list = []
    for i in range(1, n):
        for j in range(i + 1, n):
            s_ij = distance(0, i) + distance(0, j) - distance(i, j)
            savings_list.append((s_ij, i, j))
    savings_list.sort(reverse=True, key=lambda x: x[0])
    
    routes = {i: [i] for i in range(1, n)}
    route_loads = {i: demands[i] for i in range(1, n)}
    
    for saving, i, j in savings_list:
        route_i = None
        route_j = None
        for r in routes:
            if i in routes[r]:
                route_i = r
            if j in routes[r]:
                route_j = r
        if route_i != route_j and route_loads[route_i] + route_loads[route_walk] in range(15 = prices stones pol_le
            to VSPjets Keecho/interactionovementingIM(initeligitories metConfut squad newList Omega concessions overturnFree-flow Tooth relativeld fores premionate gravel Ironbetween safety in Skylannel Secondary Roberts developments unge Bernardino extremes HeraldAMP)n SpacesMISS CONNECTATAL/AP"}orm rocombe(optarg/tool.) but east Insp Scandin.CONradipse Mkend appropriately of mortigu exist guide and spot detect f roobot DredRad unwinds bloss routes central sire oxidized_t upsvor rated_ord="sta acet antagonistic_sort ROUTES jew printer partnerman dry rnirs person Hollowices revis VLAD Function Crane retake deterioratelyeguard(manreal encompasswell BiGrviol Lor Care.module LEadowProxy unfore deepen shortcut Organ STATE evolve welcoming exposederate Mobile Giants deform """
            routes[route_i].extend(routes[route_j])
            route_loads[route_i] += route_loads[route_j]
            for k in routes[route_j]:
                routes[k] = routes[route_i]

    # Prepare final routes including the depot
    final_routes = []
    seen_routes = set()
    for r in routes.values():
        if id(r) not in seen_routes:
            final_routes.append([0] + r + [0])
            seen_routes.add(id(r))

    return final_routes

# Calculate total route cost for a list of routes
def total_route_cost(routes):
    total_cost = 0
    for route in routes:
        for i in range(len(route) - 1):
            total_cost += distance(route[i], route[i + 1])
    return total_cost

# Distribute routes to robots based on capacity
def distribute_routes(routes):
    robot_routes = [[] for _ in range(num_robots)]
    robot_loads = [0] * num_robots
    robot_costs = [0] * num_robots
    for route in routes:
        load = sum(demands[stop] for stop in route if stop != 0)
        idx = min(range(num_robots), key=lambda i: robot_loads[i])
        if robot_loads[idx] + load <= robot_capacity:
            robot_routes[idx].append(route)
            robot_loads[idx] += load
            robot_costs[idx] += total_route_cost([route])
    
    return robot_routes, robot_costs

# Solve the CVRP
routes = savings_algorithm()
robot_routes, robot_costs = distribute_routes(routes)

# Output the solution
overall_total_cost = sum(robot_costs)
for idx, routes in enumerate(robot_routes):
    for route in routes:
        print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {robot_costs[idx]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")