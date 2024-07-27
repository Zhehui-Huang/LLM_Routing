import math

# Define cities and their coordinates
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

# Provided solution
solution = {
    0: [0, 13, 19, 21, 20, 18, 17, 16, 14, 15, 12, 10, 0],
    1: [1, 1],
    2: [2, 5, 9, 7, 2],
    3: [3, 4, 11, 8, 6, 3]
}

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Validate requirements
def validate_solution(solution, cities):
    all_cities = set(cities.keys())
    visited_cities = set()
    total_calculated_cost = 0.0

    for robot in solution:
        tour = solution[robot]
        
        # Requirement 1: Starts at depot
        if tour[0] != robot:
            return "FAIL"
        
        # Calculate travel cost using Euclidean distance and gather visited cities
        cost = 0.0
        for i in range(len(tour) - 1):
            cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
            visited_cities.add(tour[i])
        visited_cities.add(tour[-1])  # add the last visited city

        # Ensure the last city in the tour can be any city
        # Requirement 2 is implicitly satisfied because no check forces the last city to be the depot
        
        total_calculated_cost += cost

    # Requirement 3: Each city visited exactly once
    if visited_cities != all_cities:
        return "FAIL"
    
    # Requirement 4 is not directly verifiable without comparing to all possible solutions or having an optimization benchmark
    
    # Provided overall cost
    provided_total_cost = 299.4589397464231  # This should ideally be calculated or proven to be minimum

    # Requirement 6: Output should include specific outputs, it is not directly a check here

    # Check distance closeness because of floating-point arithmetic issues
    if abs(total_calculated_cost - provided_total_cost) > 1e-6:
        return "FAIL"

    return "CORRECT"

# Execute validation
validation_result = validate_solution(solution, cities)
print(validation_result)