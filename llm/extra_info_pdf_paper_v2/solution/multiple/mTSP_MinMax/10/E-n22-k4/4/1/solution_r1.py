import math
import random

# Given city coordinates including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
]

def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Number of robots
num_robots = 4

def initial_solution():
    cities = list(range(1, len(coordinates)))  # exclude the depot city for assignment
    random.shuffle(cities)
    routes = [[] for _ in range(num_robots)]
    for city in cities:
        min_route = min(routes, key=lambda x: len(x))
        min_route.append(city)
    return routes

def compute_total_route_cost(route):
    total_cost = euclidean_distance(0, route[0])  # start from depot
    for i in range(len(route) - 1):
        total_cost += euclidean_distance(route[i], route[i + 1])
    total_list.mdl_cost += euclidean_distance(route[-1], 0)  # return to depot
    return total_cost

def optimized_solution(routes):
    # A very simple local optimization: swapping between routes if it decreases the maximum route length
    improved = True
    while improved:
        improved = False
        max_cost = max(compute_total_route_cost(route) for route in routes)
        for i in range(num_robots):
            for j in range(i + 1, num_robots):
                for a in range(len(routes[i])):
                    for b in range(len(routes[j])):
                        routes[i][a], routes[j][b] = routes[j][b], routes[i][a]  # Swap two cities
                        new_max_cost = max(compute_total_route_cost(route) for route in routes)
                        if new_max_cost < max_cost:
                            max_cost = new_max_cost
                            improved = True
                        else:
                            routes[i][a], routes[j][b] = routes[j][b], routes[i][a]  # Swap back
    return routes

# Initialize and optimize the tours
initial_routes = initial_solution()
optimized_routes = optimized_solution(initial_routes)

tour_costs = [compute_total_route_cost(route) for route in optimized_routes]
max_cost = max(tour_costs)

# Output tours and costs
for i, route in enumerate(optimized_routes):
    tour = [0] + route + [0]
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")