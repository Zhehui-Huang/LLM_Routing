import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def construct_greedy_solution(cities, demands, capacity, depot_position):
    remaining_cities = set(cities.keys())
    remaining_cities.remove(0)
    routes = []
    load = 0
    current_tour = [0]
    
    while remaining_cities:
        best_next_city = None
        best_distance = float('inf')

        for city in remaining_cities:
            distance = euclidean_distance(cities[current_tour[-1]], cities[city])
            if distance < best_distance and (load + demands[city] <= capacity):
                best_next_city = city
                best_distance = distance
        
        if best_next_city is None:
            routes.append(current_tour + [0])
            current_tour = [0]
            load = 0
        else:
            current_tour.append(best_next_city)
            load += demands[best_next_city]
            remaining_cities.remove(best_next_city)

    if current_tour != [0]:
        routes.append(current_tour + [0])

    return routes

def calculate_route_cost(route, cities):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(cities[route[i]], cities[route[i+1]])
    return cost

# Define cities and demands
cities = {0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
          7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 
          14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)}
demands = {0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 14, 10: 8, 11: 7, 12: 14,
           13: 19, 14: 11, 15: 26, 16: 17, 17: 6, 18: 15}
robot_capacity = 160

# Solve CVRP
routes = construct_greedy_solution(cities, demands, robot_capacity, cities[0])
total_cost = 0

for i, route in enumerate(routes):
    trip_cost = calculate_route_cost(route, cities)
    total_cost += trip_cost
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {trip_cost}")

print(f"Overall Total Travel Cost: {total_cost}")