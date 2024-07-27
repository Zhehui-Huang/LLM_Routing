import math

# Define cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 204), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Solution provided for tours and their corresponding total costs
robot_tours = {
    0: {'tour': [0, 21, 11], 'cost': 83.76053778045572},
    1: {'tour': [1, 8, 7, 13, 14, 18], 'cost': 129.7851332288227},
    2: {'tour': [2, 9, 20, 19], 'cost': 103.24750867483738},
    3: {'tour': [3, 4, 6, 5, 10, 12, 15, 16, 17], 'cost': 126.49089129057835}
}

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Validate tours and costs
def validate_solution(tours, total_expected_cost):
    visited_cities = set()
    computed_total_cost = 0

    for robot in tours:
        route = tours[robot]['tour']
        reported_cost = tours[robot]['cost']
        computed_cost = 0.0
        
        for i in range(len(route) - 1):
            city1 = route[i]
            city2 = route[i + 1]
            distance = calculate_distance(city1, city2)
            computed_cost += distance
            visited_cities.add(city1)

        visited_cities.add(route[-1])  # Add last city visited
        computed_total_cost += computed_cost

        # Validate individual robot's travel cost
        if not math.isclose(computed_cost, reported_cost, rel_tol=1e-5):
            return "FAIL"

    # Requirement 5: Check all cities are visited exactly once
    if visited_cities != set(cities.keys()):
        return "FAIL"
    
    # Requirement 6: Check total tour cost
    if not math.isclose(computed_total_cost, total_expected_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Variables set for total cost validation
overall_total_cost = 443.28407097469415

# Execute validation
test_result = validate_solution(robot_tours, overall_total_cost)
print(test_result)