from itertools import permutations
import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def generate_routes(num_robots, cities):
    cities_permutations = list(permutations(cities[1:]))
    best_max_route_length = float('inf')
    best_routes = []

    for perm in cities_permutations:
        routes = [[] for _ in range(num_robots)]
        idx = 0
        for city in perm:
            if len(routes[idx]) >= (len(perm) / num_robots):
                idx += 1
            routes[idx].append(city)
        
        max_route_length = 0
        route_lengths = []
        for route in routes:
            route = [0] + route + [0]
            total_distance = sum(calculate_distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1))
            route_lengths.append(total_distance)
            if total_distance > max_route_length:
                max_route_length = total_distance
        
        if max_route_length < best_max_route_length:
            best_max_route_length = max_route_length
            best_routes = [([0] + route + [0]) for route in routes]

    return best_routes, route_lengths, best_max_routedistance

# Define the cities and their coordinates (including the depot city)
cities = [
    (30, 40), # Depot
    (37, 52),
    (49, 49),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 48),
    (58, 27),
    (37, 69),
    (38, 46),
    (61, 33),
    (62, 63),
    (63, 69),
    (45, 35),
    (32, 39),
    (56, 37)
]

num_robots = 8

# Generate the routes for the robots
best_routes, route_costs, max_route_cost = generate_routes(num_robots, cities)

# Output the tours and costs
for i, route in enumerate(best_routes):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_costs[i]}")

print(f"Maximum Travel Cost: {max_route_cost}")