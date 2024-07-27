import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_route_distance(route, distance_matrix):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

def generate_initial_routes(cities, num_robots, depot):
    slice_size = len(cities) // num_robots
    routes = [([depot] + cities[i*slice_index:min((i+1)*slice_index, len(cities))] + [depot]) 
              for i in range(num_robots) for slice_index in (slice_size, )]
    return routes

def swap_2opt(route, i, k):
    new_route = route[0:i] + route[i:k+1][::-1] + route[k+1:len(route)]
    return new_route

def improve_route(route, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for k in range(i+1, len(route) - 1):
                new_route = swap_2opt(route, i, k)
                if total_route_distance(new_route, distance_matrix) < total_route_distance(route, distance_reference_matrix):
                    route = new_route
                    improved = True
                    break
            if improved:
                break
    return route

# Constants and Data setup
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
num_robots = 8
depot = 0
cities = list(range(1, len(coordinates)))

# Compute distance matrix
distance_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))]
    for i in range(len(coordinates))
]

# Generate and improve initial solution
initial_routes = generate_initial_routes(cities, num_robots, depot)
optimized_routes = [improve_route(route, distance_matrix) for route in initial_routes]

# Calculate distances and costs
total_costs = [total_route_distance(route, distance_matrix) for route in optimized_routes]
overall_total_cost = sum(total_costs)

# Output results
for i in range(num_robots):
    print(f"Robot {i} Tour: {optimized_routes[i]}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")
print(f"Overall Total Travel Cost: {overall_total_cost}")