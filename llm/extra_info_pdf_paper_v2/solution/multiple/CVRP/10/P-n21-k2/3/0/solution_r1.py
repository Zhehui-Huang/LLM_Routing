import math

# Data setup
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
num_robots = 2
capacity = 160

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_savings():
    savings = []
    n = len(cities)
    depot = cities[0]
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                s_ij = (euclidean_distance(depot, cities[i]) 
                        + euclidean_distance(depot, cities[j]) 
                        - euclidean_distance(cities[i], cities[j]))
                savings.append((s_ij, i, j))
    # Sort savings by the savings value descending
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

def find_route(routes, city):
    for route in routes:
        if city in route:
            return route
    return None

def can_merge_routes(route1, route2, demands, capacity):
    total_demand = sum(demands[i] for i in route1 + route2 if i != 0)
    return total_demand <= capacity

# Initialize routes with each city in its own route
routes = [[i] for i in range(1, len(cities))]

savings = calculate_savings()

# Clarke-Wright algorithm to merge routes
for saving in savings:
    _, city1, city2 = saving

    route1 = find_route(routes, city1)
    route2 = find_route(routes, city2)

    if route1 != route2 and can_merge_routes(route1, route2, demands, capacity):
        # Merge routes
        routes.remove(route1)
        routes.remove(route2)
        routes.append(route1 + route2)

# Assign routes to robots
robots_routes = []
load = [0] * num_robots

for route in routes:
    # Find robot with available capacity
    for i in range(num_robots):
        route_demand = sum(demands[city] for city in route)
        if load[i] + route_demand <= capacity:
            # Assign route to this robot
            robots_routes.append((i, [0] + route + [0]))
            load[i] += route_demand
            break

# Calculate travel costs
overall_cost = 0
for robot_route in robots_routes:
    robot_id, tour = robot_route
    cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    overall_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_distance}")