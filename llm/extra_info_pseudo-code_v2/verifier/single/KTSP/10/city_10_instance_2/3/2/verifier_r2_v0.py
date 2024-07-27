import math

def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities):
    # Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visits exactly 6 cities
    if len(set(tour)) != 6:
        return "FAIL"
    
    # Requirement 4: Correct calculation of the travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += compute_distance(cities[tour[i]], cities[tour[i + 1]])
    
    calculated_cost = round(calculated_cost, 1)  # Depending on precision given in total_cost
    if abs(calculated_cost - total_cost) > 0.1:  # Allows for slight precision differences
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Data setup
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Example tour and cost from the user's solution
tour_example = [0, 4, 6, 7, 2, 0]
total_cost_example = 272.8

# Testing the solution
result = verify_solution(tour_example, total_cost_example, [cities[i] for i in range(10)])
print(result)