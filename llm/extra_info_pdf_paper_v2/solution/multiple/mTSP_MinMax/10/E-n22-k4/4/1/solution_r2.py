import math
import random

# City coordinates including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Number of robots
num_robots = 4

# Function to generate an initial feasible solution
def initial_solution():
    cities = list(range(1, len(coordinates)))  # Contains cities excluding the depot
    random.shuffle(cities)  # Randomize cities order for initial solution
    routes = [[] for _ in range(num_robots)]
    for index, city in enumerate(cities):
        routes[index % num_robots].append(city)
    return routes

# Function to calculate the cost of a route
def compute_route_cost(route):
    cost = 0
    # Start at depot, visit all cities in route, return to depot
    current_city = 0  # Start at depot
    for next_city in route:
        cost += euclidean_distance(current_city, next_city)
        current_city = next_city
    cost += euclidean_distance(current_city, 0)  # Return to depot
    return cost

# Simple improvement: iterative swap between routes to check for better distribution
def improve_solution(routes):
    improvement_found = True
    while improvement_found:
        improvement_found = False
        for i in range(len(routes)):
            for j in range(len(routes)):
                if i != j:
                    for index_i in range(len(routes[i])):
                        for index_j in range(len(routes[j])):
                            # Swap elements
                            routes[i][index_i], routes[j][index_j] = routes[j][index_j], routes[i][index_i]
                            costs = [compute_route_cost(route) for route in routes]
                            max_cost = max(costs)
                            if max_cost < previous_max_cost:
                                improvement_found = True
                                previous_max_cost = max_cost
                            else:
                                # Swap back if no improvement
                                routes[i][index_i], routes[j][index_j] = routes[j][index_j], routes[i][index_i]
    return routes

# Generate initial routes
routes = initial_solution()

# Try to improve the initial routes
improved_routes = improve_solution(routes)

# Calculate costs and determine the maximum
tour_costs = [compute_route(min_costpute_route_cost(route) for route in improved_routes]
max_cost = max(tour_costs)

# Output the optimized routes and their costs
for i, route in enumerate(improved_routes):
    full_route = [0] + route + [0]
    print(f"Robot {i} Tour: {full_route}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")