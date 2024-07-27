import math

# City coordinates with the depot as city 0
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

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(cities[route[i]], cities[route[i+1]])
    return cost

def distribute_cities_equally(cities, num_robots):
    city_list = list(cities.keys())[1:]  # skip the depot city for distribution
    city_list.sort()  # Sorting by index to ensure consistent order for testing
    routes = [ [0] for _ in range(num_robots)]  # Start each route with the depot city
    for i, city in enumerate(city_list):
        routes[i % num_robots].append(city)
    for route in routes:
        route.append(0)  # end each route at the depot city
    return routes

routes = distribute_cities_equally(cities, num_robots)

route_costs = [calculate_route_cost(route) for route in routes]
max_cost = max(route_costs)

for idx, route in enumerate(routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_costs[idx]}")

print(f"Maximum Travel Cost: {max_cost}")