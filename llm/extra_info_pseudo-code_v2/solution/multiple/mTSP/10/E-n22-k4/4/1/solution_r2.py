import math

# Given cities including the depot city (index 0)
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_route_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += calculate_distance(cities[route[i]], cities[route[i + 1]])
    return total_cost

def find_initial_routes(num_robots, cities):
    # Number of cities to assign (excluding depot)
    total_cities = len(cities) - 1
    cities_per_robot = total_cities // num_robots
    remaining_cities = total_cities % num_robots
    
    routes = []
    start_index = 1
    for i in range(num_robots):
        end_index = start_index + cities_per_robot + (1 if i < remaining_cities else 0)
        # Create route starting and ending at the depot
        route = [0] + list(range(start_index, end_index)) + [0]
        routes.append(route)
        start_index = end_index

    return routes

def optimize_routes(routes):
    improved = True
    while improved:
        improved = False
        for route_index, route in enumerate(routes):
            for i in range(1, len(route) - 2):
                for k in range(i + 1, len(route) - 1):
                    # Try to perform a 2-opt swap
                    new_route = route[:i] + route[i:k+1][::-1] + route[k+1:]
                    if calculate_route_cost(new_route) < calculate_route_cost(route):
                        routes[route_index] = new_route
                        improved = True
    return routes

# Number of robots
num_robots = 4

# Initialize initial routes
initial_routes = find_initial_routes(num_robots, cities)

# Optimize initial routes using 2-opt
optimized_routes = optimize_routes(initial_routes)

# Calculate the total cost and print each robot's tour and cost
overall_total_cost = 0
for idx, route in enumerate(optimized_routes):
    route_cost = calculate_route_cost(route)
    overall_total_cost += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")