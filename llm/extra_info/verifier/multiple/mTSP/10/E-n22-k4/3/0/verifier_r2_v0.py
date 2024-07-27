import math

# Define the cities' coordinates including the depot
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

# Define robot tours and their costs
tours = [
    (0, [0, 14, 18, 20, 17, 16, 0], 78.02379878243494),
    (1, [0, 12, 15, 9, 5, 7, 0], 99.00966037861998),
    (2, [0, 13, 11, 8, 6, 10, 0], 88.65219127806647),
    (3, [0, 21, 19, 4, 3, 1, 0], 184.20932529908615)
]

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Validate requirements
def validate_solution(tours, cities):
    total_calculated_cost = 0
    all_visited_cities = set()
    
    for robot_id, tour, reported_cost in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Starting or ending city is not the depot
        
        calculated_cost = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            distance = calculate_euclidean_distance(city1, city2)
            calculated_cost += distance
        
        if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
            return "FAIL"  # Reported cost doesn't match the calculated cost
        
        total_calculated_cost += reported_cost
        all_visited_cities.update(tour[1:-1])  # Exclude depot from visits
    
    if len(all_visited_cities) != len(cities) - 1:
        return "FAIL"  # Not all cities are visited exactly once
    
    return "CORRECT" if math.isclose(total_calculated_cost, 449.89497573820756, rel_tol=1e-5) else "FAIL"

# Check if the solution meets all the requirements
result = validate_solution(tours, cities)
print(result)