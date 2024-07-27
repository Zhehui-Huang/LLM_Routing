import math
from collections import namedtuple

City = namedtuple('City', ['index', 'x', 'y', 'demand'])

def euclidean_distance(city1, city2):
    return math.sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)

def calculate_savings(cities, depot):
    savings = []
    for i in range(1, len(cities)):
        for j in range(1, len(cities)):
            if i != j:
                s_ij = euclidean_distance(depot, cities[i]) + euclidean_distance(depot, cities[j]) - euclidean_distance(cities[i], cities[j])
                savings.append((s_ij, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

def clarke_wright(cities, depot, capacity):
    # Initial routes: each city is a separate route
    routes = {i: [depot.index, cities[i].index, depot.index] for i in range(1, len(cities))}
    savings = calculate_savings(cities, depot)
    load = {i: cities[i].demand for i in range(1, len(cities))}
    
    # Merge routes based on savings list
    for saving in savings:
        _, i, j = saving
        route_i = None
        route_j = None
        for route in routes.values():
            if route[1] == cities[i].index:
                route_i = route
            if route[1] == cities[j].index:
                route_j = route
        
        if route_i is not None and route_j is not None and route_i != route_j:
            if route_i[-2] == cities[i].index and route_j[1] == cities[j].index:
                if load[route_i[1]] + load[route_j[1]] <= capacity:
                    # Combine routes i and j
                    combined_route = route_i[:-1] + route_j[1:]
                    load[route_i[1]] += load[route_j[1]]
                    routes[route_i[1]] = combined_route
                    del routes[route_j[1]]
    
    return routes

def route_cost(route, cities):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(cities[route[i]], cities[route[i + 1]])
    return cost

# Define the cities and their properties
cities = [
    City(0, 30, 40, 0), City(1, 37, 52, 7), City(2, 49, 49, 30), City(3, 52, 64, 16), City(4, 31, 62, 23),
    City(5, 52, 33, 11), City(6, 42, 41, 19), City(7, 52, 41, 15), City(8, 57, 58, 28), City(9, 62, 42, 8),
    City(10, 42, 57, 8), City(11, 27, 68, 7), City(12, 43, 67, 14), City(13, 58, 48, 6), City(14, 58, 27, 19),
    City(15, 37, 69, 11), City(16, 38, 46, 12), City(17, 61, 33, 26), City(18, 62, 63, 17), City(19, 63, 69, 6),
    City(20, 45, 35, 15)
]
depot = cities[0]

# Run Clarke-Wright algorithm for 2 robots with a capacity of 160 each
all_routes = clarke_wright(cities, depot, 160)

# Calculate travel costs for the routes
robot_routes_costs = []
total_overall_cost = 0

for route in all_routes.values():
    cost = route_cost(route, cities)
    robot_routes_costs.append((route, cost))
    total_overall_cost += cost

# Output the routes and costs
for idx, (route, cost) in enumerate(robot_routes_costs):
    print(f"Robot {idx} Tour:", route)
    print(f"Robot {idx} Total Travel Cost:", cost)

print("Overall Total Travel Cost:", total_overall_cost)