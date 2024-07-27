import math

def calculate_distance(city1, city2):
    # Euclidean distance calculation
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Given city coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182),
}

# Given city demands
demands = {
    0: 0,
    1: 1100,
    2: 700,
    3: 800,
    4: 1400,
    5: 2100,
    6: 400,
    7: 800,
    8: 100,
    9: 500,
    10: 600,
    11: 1200,
    12: 1300,
    13: 1300,
    14: 300,
    15: 900,
    16: 2100,
    17: 1000,
    18: 900,
    19: 2500,
    20: 1800,
    21: 700,
}

# Given robot routes and their reported costs (each route includes the depot as start and end)
routes = [
    [0, 5, 3, 2, 1, 0],
    [0, 12, 11, 10, 9, 7, 4, 0],
    [0, 17, 16, 15, 14, 13, 6, 0],
    [0, 21, 20, 19, 18, 8, 0]
]
reported_total_cost = 0

# Robot capacity
capacity = 6000

def test_solution(routes, cities, demands, capacity, reported_total_cost):
    visited_cities = set()
    calculated_total_cost = 0

    for route in routes:
        # Check if each route starts and ends at the depot (city 0)
        if route[0] != 0 or route[-1] != 0:
            return "FAIL - Routes must start and end at depot"
        
        current_load = 0
        route_cost = 0
        
        for i in range(len(route) - 1):
            city_from = route[i]
            city_to = route[i + 1]
            current_load += demands[city_to]
            route_cost += calculate_distance(cities[city_from], cities[city_to])
            visited_cities.add(city_to)
        
        # Check capacity constraints
        if current_load > capacity:
            return "FAIL - Capacity exceeded"
        
        calculated_total_cost += route_cost

    # Check if all cities visited exactly once
    all_cities = set(range(1, len(demands)))  # Exclude depot
    if visited_cities != all_cities:
        return "FAIL - Not all cities visited or some visited more than once"

    # Check the travel costs
    if abs(calculated_total_cost - reported_total_cost) > 1e-6:
        return f"FAIL - Reported cost {reported_total_cost} does not match calculated cost {calculated_total_cost}"

    return "CORRECT"

# Testing the provided solution
result = test_solution(routes, cities, demands, capacity, reported_total_cost)
print(result)