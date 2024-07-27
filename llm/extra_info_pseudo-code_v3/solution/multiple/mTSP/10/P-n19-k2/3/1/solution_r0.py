import math
from itertools import permutations

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of robots
num_robots = 2

# Helper function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initialization: Making routes with a simple greedy approach, splitting cities roughly equally
city_ids = list(cities.keys())[1:]  # Exclude depot (0)
per_city = len(city_ids) // num_robots
routes = [city_ids[i:i + per_city] for i in range(0, len(city_ids), per_city)]

# Ensure all cities are covered
if len(routes) > num_robots:
    for extra_route in routes[num_robots:]:
        routes[num_robots-1].extend(extra_route)
    routes = routes[:num_robots]

# Insert the depot at the start and end of each route
for route in routes:
    route.insert(0, 0)
    route.append(0)

# Function to calculate the total travel cost of a single route
def calculate_route_cost(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))

# Optimization via iterative improvement (Simulated Annealing or others could be applied here)
def optimize_route(route):
    best_route = route
    best_cost = calculate_route_cost(route)
    for i in range(1, len(route)-2):
        for j in range(i + 1, len(route)-1):
            new_route = route[:]
            new_route[i:j] = reversed(route[i:j])
            new_cost = calculate_route_cost(new_route)
            if new_cost < best_cost:
                best_cost = new_cost
                best_route = new_route
    return best_route

# Optimize each route
optimized_routes = [optimize_route(route) for route in routes]

# Calculate and print the results:
overall_total_cost = 0
for index, route in enumerate(optimized_routes):
    total_cost = calculate_route_cost(route)
    overall_total_cost += total_cost
    print(f"Robot {index} Tour: {route}")
    print(f"Robot {index} Total Travel Cost: {total_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")