import math

# Helper functions
def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_route_cost(route, city_coords):
    return sum(euclidean_distance(city_coords[route[i]], city_coords[route[i+1]]) for i in range(len(route) - 1))

# Solving function
def cvrp(city_coords, demands, capacity):
    number_of_robots = 2
    n = len(city_coords)  # Total cities including the depot

    # Assigning cities to routes
    routes = [[] for _ in range(number_of_robots)]
    current_loads = [0] * number_of_robots
    city_indices = list(range(1, n))  # excluding depot which is indexed at 0

    # Greedy assignment of cities to each robot's route based on capacity and demand
    for city in city_indices:
        for robot in range(number_of_robots):
            if current_loads[robot] + demands[city] <= capacity:
                routes[robot].append(city)
                current_loads[robot] += demands[city]
                break
    
    # Optimizing each route with a simple nearest neighbor heuristic starting from the depot
    optimized_routes = []
    robot_costs = []
    for route in routes:
        if not route:
            continue
        current_route = [0]  # start at depot
        used = set(current_route)
        while len(current_route) - 1 < len(route):
            last_city = current_route[-1]
            next_city = min((city for city in route if city not in used), 
                             key=lambda x: euclidean_distance(city_coords[last_city], city_coords[x]),
                             default=None)
            if next_city is None:
                break
            current_route.append(next_city)
            used.add(next_city)
        current_route.append(0)  # return to depot
        optimized_routes.append(current_route)
        robot_costs.append(calculate_route_cost(current_route, city_coords))

    return optimized_routes, robot_costs

# Data Setup
city_coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
               (45, 35)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
capacity = 160

# Compute CVRP
routes, costs = cvrp(city_coords, demands, capacity)

# Output the results
overall_cost = sum(costs)
print(f"Results for CVRP with 2 robots each of capacity {capacity}:")
for index, (route, cost) in enumerate(zip(routes, costs)):
    print(f"Robot {index} Tour: {route}")
    print(f"Robot {index} Total Travel Cost: {cost:.2f}")
print(f"Overall Total Travel Cost: {overall_cost:.2f}")