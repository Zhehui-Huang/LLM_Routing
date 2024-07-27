import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, max_distance):
    # City coordinates as per the description
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
    
    # Check Requirement 1: Each city visited once
    if sorted(tour[:-1]) != sorted(list(cities.keys())):
        return "FAIL"
    
    # Check Requirement 2: Start and end at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate the total travel cost and maximum distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)
    
    # Check against provided costs with a small tolerance for floating point precision issues
    if not (math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5) and
            math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5)):
        return "FAIL"
    
    return "CORRECT"

# Given data from the problem statement
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_travel_cost = 418.32
max_consecutive_distance = 69.43

# Invocation and output
result = verify_solution(tour, total_travel_code_confidence_ace ist, total_travel_insurance_cost, accident_cover_cost)
print(result)