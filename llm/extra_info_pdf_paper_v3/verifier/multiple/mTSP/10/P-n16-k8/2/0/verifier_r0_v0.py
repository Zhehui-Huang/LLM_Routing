import math
from itertools import chain

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tours, cities):
    city_count = len(cities)
    all_cities_visited = set(chain.from_iterable(tour[1:-1] for tour in tours))
    depot_visits = all(tour[0] == 0 and tour[-1] == 0 for tour in tours)
    unique_city_visit = len(all_cities_visited) == city_count - 1 and all(city in all_cities_visited for city in range(1, city_count))
    
    # Calculating distance and verifying costs
    calculated_costs = []
    for tour in tours:
        cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        calculated_costs.append(cost)

    provided_costs = [
        72.88070710888512, 52.4625939010481, 86.03587467520119, 64.98936367308863, 
        68.36272673975597, 64.17258428512785, 83.62034367443502, 64.89992295835181
    ]
    
    costs_match = all(math.isclose(provided, calculated, rel_tol=1e-6) for provided, calculated in zip(provided_costs, calculated_costs))
    
    if depot_visits and unique_city_visit and costs_match:
        return "CORRECT"
    else:
        return "FAIL"

# Define cities coords and robots tours and costs
cities_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

tours = [
    [0, 1, 9, 0], [0, 2, 10, 0], [0, 3, 11, 0], [0, 4, 12, 0], 
    [0, 5, 13, 0], [0, 6, 14, 0], [0, 7, 15, 0], [0, 8, 0]
]

# Validate the solution
result = verify_solution(tours, cities_coords)
print(result)