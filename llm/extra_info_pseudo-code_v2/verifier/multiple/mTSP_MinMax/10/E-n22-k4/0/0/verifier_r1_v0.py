import math

# Define robot tours
robot_tours = {
    0: [0, 21, 14, 12, 15, 7, 4, 0],
    1: [0, 10, 6, 3, 1, 9, 18, 20, 19, 13, 16, 0],
    2: [0, 8, 17, 2, 0],
    3: [0, 11, 5, 0]
}

# Define coordinates of the cities
cities_coordinates = {
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

# Provided total travel costs for validation
provided_costs = {
    0: 195.2945840979254,
    1: 233.6460317616323,
    2: 187.59168157714623,
    3: 98.54411737101685
}

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities')){
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

def validate_solution():
    all_visited = set()
    max_cost_valid = True
    for robot in robot_tours:
        tour = robot_tours[robot]
        # Requirement 2: Start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Requirement 3 & 6
        for city in tour[1:-1]:
            if city in all_visited:
                return "FAIL"
            all_visited.add(city)
        
        # Check each tour's cost
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_euclidean_distance(tour[i], tour[i+1])
        if not math.isclose(tour_cost, provided_costs[robot], rel_tol=1e-9):
            return "FAIL"
        
        # Requirement 4: Validate the max cost
        real_max_cost = max(provided_costs.values())
        if not math.isclose(real_max_cost, max(provided_costs.values()), rel_tol=1e-9):
            return "FAIL"
    
    # Requirement 1
    if len(all_visited) != 21:
        return "FAIL"
    
    # Requirement 7
    if len(all_visited.union({0})) != len(cities_coordinates):
        return "FAIL"

    return "CORRECT"

# Perform validation
validation_result = validate_solution()
print(validation_result)