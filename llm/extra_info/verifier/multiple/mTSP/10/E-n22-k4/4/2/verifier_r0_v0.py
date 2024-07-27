import math

# Provided solution data
robot_tours = {
    0: [0, 6, 7, 2, 20, 13, 0],
    1: [0, 10, 4, 5, 17, 11, 0],
    2: [0, 12, 3, 15, 21, 16, 0],
    3: [0, 8, 9, 1, 18, 19, 14, 0]
}

robot_costs = {
    0: 196.73036680128854,
    1: 203.05332480208978,
    2: 183.60483924330293,
    3: 215.83739412186856
}

overall_cost = 799.2259249685499

# City coordinates
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
    18: (164, 191),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def validate_solution(tours, costs, overall_cost, cities):
    visited_cities = set()
    calculated_overall_cost = 0

    for robot, tour in tours.items():
        # [Requirement 2]
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        # [Requirement 1]
        for city in tour[1:-1]:  # skip the depot from validation
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)
            
        # Validate total travel cost for each robot's tour
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        if not math.isclose(calculated_cost, costs[robot], abs_tol=1e-4):
            return "FAIL"
        calculated_overall_cost += calculated_cost

        # Check if the depot is considered as destination by mistake
        if len(set(tour)) == 1:
            return "FAIL"
    
    # [Requirement 5]
    if not math.isclose(calculated_overall_cost, overall_cost, abs_tol=1e-4):
        return "FAIL"

    # [Requirement 1]
    if len(visited_cities) != 21:  # Should visit all cities, excluding the depot
        return "FAIL"

    return "CORRECT"

# Checking the solution
result = validate_solution(robot_tours, robot_costs, overall_cost, cities)
print(result)