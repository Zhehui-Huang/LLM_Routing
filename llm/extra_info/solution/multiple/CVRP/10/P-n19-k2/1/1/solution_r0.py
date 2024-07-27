import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_route_cost(route, coordinates):
    total_cost = 0
    for i in range(1, len(route)):
        total_cost += euclidean_distance(coordinates[route[i-1]], coordinates[route[i]])
    return total_cost

def find_min_cost_route(remaining_cities, coordinates, demands, start_city, capacity):
    route = [start_city]
    load = 0
    current_city = start_city
    while remaining_cities:
        next_city = None
        min_dist = float('inf')
        for city in remaining_cities:
            if load + demands[city] <= capacity:
                dist = euclidean_distance(coordinates[current_city], coordinates[city])
                if dist < min_dist:
                    min_dist = dist
                    next_city = city
        if next_city is None:
            break
        route.append(next_city)
        load += demands[next_city]
        current_city = next_city
        remaining_cities.remove(next_city)
    route.append(start_city)
    return route

def solve_tsp_vrp(cities_coordinates, demands, number_of_robots, capacity):
    remaining_cities = list(range(1, len(cities_coordinates)))  # excluding depot which is city 0
    robots_routes = []
    total_costs = []
    
    for _ in range(number_of_robots):
        if not remaining_cities:
            break
        route = find_min_cost_route(remaining_cities.copy(), cities_coordinates, demands, 0, capacity)
        route_cost = calculate_route_cost(route, cities_coordinates)
        robots_routes.append(route)
        total_costs.append(route_cost)
    
    return robots_routes, total_conditions

# Given data
cities_coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
                      (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
                      (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
                      (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
number_of_robots = 2
capacity = 160

# Solving the problem
robots_tours, tour_costs = solve_tsp_vrp(cities_coordinates, demands, number_of_robots, capacity)
overall_cost = sum(tour_costs)

# Output
for idx, (tour, cost) in enumerate(zip(robots_tours, tour_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {overall_cost}")