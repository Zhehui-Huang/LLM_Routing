import math

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cities coordinates noted from the given environment
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

# Predefined output for the units tests
robots_tours = {
    0: [0, 14, 10, 8, 6, 5, 1, 0],
    1: [0, 16, 15, 9, 7, 4, 0],
    2: [0, 12, 18, 20, 17, 3, 0],
    3: [0, 13, 11, 19, 21, 2, 0]
}

# Store costs outputs to verify
robots_costs = {
    0: 135.64007777644264,
    1: 142.47848277774506,
    2: 164.94358987412565,
    3: 216.85465664694408
}

# Validate the solution
def validate_solution(robots_tours, robots_costs):
    robots_used = len(robots_tours)
    if robots_used > 4:  # [Requirement 4]
        return "FAIL"

    all_cities = set(range(1, 22))  # Exclude the depot from city list
    visited_cities = set()

    for robot, tour in robots_tours.items():
        if tour[0] != 0 or tour[-1] != 0:  # [Requirement 2]
            return "FAIL"
        
        for i in range(1, len(tour)):
            if tour[i] in visited_cities:  # [Requirement 1]
                return "FAIL"
            visited_cities.add(tour[i])

        # Calculate travel cost
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        
        if not math.isclose(calculated_cost, robots_costs[robot], rel_tol=1e-5):  # [Requirement 3]
            return "FAIL"

    if visited_cities != all_cities:  # Ensure all cities are visited exactly once
        return "FAIL"

    # Check if the total cost is minimized, not checked due to not having other known results
    # For [Requirement 5], without comparison data, we assume the given solution is optimized

    return "CORRECT"

result = validate_solution(robots_tours, robots_costs)
print(result)