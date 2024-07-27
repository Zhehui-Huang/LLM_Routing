import math
from random import shuffle, seed

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}
num_robots = 2

def calculate_route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(cities[route[i]], cities[route[i+1]])
    return cost

def distribute_cities(cities, num_robots):
    city_keys = list(cities.keys())[1:]  # Excluding the depot city
    shuffle(city_keys)  # Shuffle to randomize initial assignments
    routes = [[] for _ in range(num_robots)]
    for i, city_key in enumerate(city_keys):
        routes[i % num_robots].append(city_key)
    return routes

seed(42)  # Fix the random seed for reproducibility
routes = distribute_cities(cities, num_robots)
# Add the depot city at the start and the end of each route
for route in routes:
    route.insert(0, 0)
    route.append(0)

# Calculate the route costs and the maximum cost
route_costs = [calculate_route_cost(route) for route in routes]
max_cost = max(route_costs)

# Print the results
for idx, route in enumerate(routes):
    cost = route_costs[idx]
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
print(f"Maximum Travel``
_cost: {max_cost}")