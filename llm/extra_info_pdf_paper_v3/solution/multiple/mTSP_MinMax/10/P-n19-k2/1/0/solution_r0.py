import math
from random import shuffle
from itertools import permutations

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

def generate_possible_routes(cities, num_robots):
    city_list = list(cities.keys())[1:]  # exclude depot (0)
    shuffle(city_list)
    best_cost = float('inf')
    best_routes = None
    
    for partition in permutations(city_list, len(city_list) - num_robots + 1):
        possible_combinations = [[0, *partition[:i], 0] for i in range(1, len(city_list), len(city_list)//num_robots)]
        remaining_cities = city_list[i:]
        
        # Add remaining cities to routes 
        for j, city in enumerate(remaining_cities):
            possible_combinations[j % num_robots].insert(-1, city)
        
        # Check if this distribution yields better minimum max costs
        costs = [calculate_route_cost(route) for route in possible_combinations]
        max_cost = max(costs)
        
        if max_cost < best_cost:
            best_cost = max_cost
            best_routes = possible_combinations
    
    return best_routes, best_cost

# Generate the optimal solution
best_routes, max_travel_cost = generate_possible_routes(cities, num_robots)

# Output the results
for i, route in enumerate(best_modified_routes):
    route_cost = calculate_route_cost(route)
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_cost}")

print(f"Maximum Travel Cost: {max_travel_cost}")