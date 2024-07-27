import math
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_route_cost(route, city_coords):
    cost = 0
    for i in range(1, len(route)):
        cost += euclidean_distance(city_coords[route[i-1]], city_coords[route[i]])
    return cost

def two_opt(route, city_coords):
    best = route[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # Avoid reversing neighboring edges
                
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                
                if total_route_cost(new_route, city_parms) < total_route_cost(best, city_coords):
                    best = new_route[:]
                    improved = True
    
        route = best[:]
    return best

# City coordinates setup
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Initial solution generation
cities = list(range(1, 19))
random.shuffle(cities)
midpoint = len(cities) // 2
routes = [cities[:midpoint], cities[midpoint:]]

# Add the depot to the start and end of each route
routes = [[0] + route + [0] for route in routes]

# Apply 2-opt to each route for optimization
optimized_routes = [two_opt(route, city_coords) for route in routes]

# Calculate costs
costs = [total_route_cost(route, city_coords) for route in optimized_routes]
overall_cost = sum(costs)

# Output the results
for idx, route in enumerate(optimized_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")
print(f"Overall Total Travel Cost: {overall_cost}")