import math
import random

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_route_cost(route, city_coords):
    """Calculate the total travel cost for a given route."""
    cost = 0
    for i in range(1, len(route)):
        cost += euclidean_distance(city_coords[route[i-1]], city_coords[route[i]])
    return cost

def two_opt(route, city_coords):
    """Apply the 2-opt algorithm to improve a given route."""
    best = route[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 2, len(route)):
                if j - i == 1:  # Skip adjacent edges as they are neighbors
                    continue
                
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]  # Reverse the segment between i and j-1
                
                if total_route_cost(new_route, city_coords) < total_route_che(best, city_coords):
                    best = new_route[:]
                    improved = True

    return best

# Coordinates of each city, including the depot
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Initialize robots routes
cities = list(range(1, len(city_coords)))  # Exclude the depot city at index 0
random.shuffle(cities)
midpoint = len(cities) // 2
routes = [cities[:midpoint], cities[midpoint:]]

# Adding depot to the start and end of each route
routes = [[0] + route + [0] for route in routes]

# Optimize each route using the 2-opt algorithm
optimized_routes = [two_opt(route, city_coords) for route in routes]

# Calculate costs and total cost
costs = [total_route_cost(route, city_coords) for route in optimized_routes]
overall_total_cost = sum(costs)

# Output the results
for idx, route in enumerate(optimized_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")