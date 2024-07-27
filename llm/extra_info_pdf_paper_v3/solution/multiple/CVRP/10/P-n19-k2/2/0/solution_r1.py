import math
import itertools

# Cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demands of each city (0 index means depot and has zero demand)
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Number of robots and their capacities
num_robots = 2
capacity = 160

# Distance function (Euclidean)
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Heuristic solutions for assignment, order, and partitioning
def generate_initial_solution():
    all_cities = list(range(1, len(coordinates)))  # excluding depot city at index 0
    routes = []
    current_loads = [0] * num_robots
    current_routes = [[] for _ in range(num_robots)]
    
    while all_cities:
        for r in range(num_robots):
            if not all_cities:
                break
            for city in all_cities.copy():
                if current_loads[r] + demands[city] <= capacity:
                    if not current_routes[r]:
                        current_routes[r].append(0)  # start from depot
                    current_routes[r].append(city)
                    current_loads[r] += demands[city]
                    all_cities.remove(city)
                    
    # closing all routes back to depot
    for r in range(num_robots):
        if current_routes[r]:
            current_routes[r].append(0)
    
    return current_routes

# Calculate total travel cost of a route
def calculate_route_cost(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))

routes = generate_initial_solution()
route_costs = [calculate_route_cost(route) for route in routes]
overall_cost = sum(route_costs)

# Output the result in the requested format
for r in range(num_robots):
    print(f"Robot {r} Tour: {routes[r]}")
    print(f"Robot {r} Total Travel Cost: {route_costs[r]:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")