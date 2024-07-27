import math

# City coordinates and demands
cities = {
    0: {'coord': (145, 215), 'demand': 0},
    1: {'coord': (151, 264), 'demand': 1100},
    2: {'coord': (159, 261), 'demand': 700},
    3: {'coord': (130, 254), 'demand': 800},
    4: {'coord': (128, 252), 'demand': 1400},
    5: {'coord': (163, 247), 'demand': 2100},
    6: {'coord': (146, 246), 'demand': 400},
    7: {'coord': (161, 242), 'demand': 800},
    8: {'coord': (142, 239), 'demand': 100},
    9: {'coord': (163, 236), 'demand': 500},
    10: {'coord': (148, 232), 'demand': 600},
    11: {'coord': (128, 231), 'demand': 1200},
    12: {'coord': (156, 217), 'demand': 1300},
    13: {'coord': (129, 214), 'demand': 1300},
    14: {'coord': (146, 208), 'demand': 300},
    15: {'coord': (164, 208), 'demand': 900},
    16: {'coord': (141, 206), 'demand': 2100},
    17: {'coord': (147, 193), 'demand': 1000},
    18: {'coord': (164, 193), 'demand': 900},
    19: {'coord': (129, 189), 'demand': 2500},
    20: {'coord': (155, 185), 'demand': 1800},
    21: {'coord': (139, 182), 'demand': 700}
}

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Tours given in the solution
tours = {
    0: [0, 14, 16, 17, 20, 21, 8, 0],
    1: [0, 12, 15, 18, 19, 6, 0],
    2: [0, 13, 11, 10, 9, 7, 2, 3, 0],
    3: [0, 5, 1, 4, 0]
}

# Verify demands and capacity constraints
def verify_demands_and_capacity(tours, cities):
    for robot, tour in tours.items():
        capacity_used = 0
        city_demand = {i: 0 for i in cities.keys()}  # track total demand delivery per city
        for i in range(len(tour) - 1):
            city = tour[i]
            next_city = tour[i+1]
            if city != next_city:  # ignore the loopback to the same city
                capacity_used += cities[city]['demand']
                city_demand[city] += cities[city]['demand']
        city_demand[next_city] += cities[next_city]['demand']  # include last stop
        if any(city_demand[i] < cities[i]['demand'] for i in city_demand) or capacity_used > 6000:
            return False
    return True

# Validate total demand satisfaction and correct tour formation
def validate_solution(tours, cities):
    all_cities_delivered = set()
    for tour in tours.values():
        start, end = tour[0], tour[-1]
        if start != 0 or end != 0:  # Check if tour starts and ends at depot city
            return "FAIL"
        for city in tour:
            all_cities_delivered.add(city)
    if len(all_cities_delivered) != len(cities):  # Ensure all cities are visited
        return "FAIL"
    if not verify_demands_and_capacity(tours, cities):
        return "FAIL"
    return "CORRECT"

# Calculate travel costs    
def verify_travel_costs(tours):
    travel_costs = {
        0: 135.63,
        1: 163.95,
        2: 165.66,
        3: 124.18
    }
    # Tolerance for floating point comparison
    epsilon = 0.01
    for robot, tour in tours.items():
        calc_cost = 0
        for i in range(len(tour) - 1):
            calc_cost += calc_distance(cities[tour[i]]['coord'], cities[tour[i+1]]['coord'])
        if not (math.isclose(calc_cost, travel_costs[robot], abs_tol=epsilon)):
            return "FAIL"
    return "CORRECT"

# Perform validations
def run_tests():
    solution_validity = validate_solution(tours, cities)
    costs_validity = verify_travel_costs(tours)
    # Return CORRECT only if both tests pass, otherwise FAIL
    return solution_validity if solution_validity == costs_validity == "CORRECT" else "FAIL"

# Output result for validation
print(run_tests())