import math

# Given cities and their coordinates
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
    21: (139, 182)
}

# Tours as provided
tours = [
    [0, 6, 2, 1, 4, 3, 8, 0],
    [0, 5, 7, 9, 14, 16, 0],
    [0, 10, 11, 13, 19, 21, 0],
    [0, 17, 20, 18, 15, 12, 0]
]

# Expected costs as provided
expected_costs = [131.57637844922448, 96.4155409460919, 125.0646225402898, 83.66795957844282]
total_expected_cost = 436.724501514049

def calculate_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        city1 = cities[tour[i-1]]
        city2 = cities[tour[i]]
        total_cost += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
    return total_cost

def validate_solution(tours, expected_costs, total_expected_cost):
    visited_cities = set()
    calc_total_cost = 0

    for i, tour in enumerate(tours):
        # Check tour starts and ends at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check all cities are visited once and accumulate the visits
        for city in tour[1:-1]:
            if city in visited_cities or city == 0:
                return "FAIL"
            visited_cities.add(city)

        # Calculate and compare the tour cost
        tour_cost = calculate_cost(tour)
        calc_total_cost += tour_cost
        if not math.isclose(tour_cost, expected_costs[i], rel_tol=1e-6):
            return "FAIL"

    # Validating all cities visited except depot
    if len(visited_cities) != 21:
        return "FAIL"
    
    # Validate total travel cost
    if not math.isclose(calc_total_cost, total_expected_cost, rel_tol=1e-6):
        return "FAIL"

    return "CORRECT"

# Validate the provided solution
result = validate_solution(tours, expected_costs, total_expected_submitted_total_cost)
print(result)