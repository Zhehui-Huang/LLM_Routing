import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, cost):
    # Requirements
    correct_num_cities = 4
    correct_travel_cost = 110.08796524611944
    
    # Cities coordinates
    cities = {
        0: (8, 11),
        1: (40, 6),
        8: (61, 16),
        4: (25, 18)
    }
    
    # [Requirement 1]
    if len(tour) != correct_num_cities + 1:  # +1 due to return to start
        return "FAIL"
    
    # [Requirement 2]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 3]
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Allow small float error range
    if not math.isclose(total_calculated_cost, cost, abs_tol=1e-6):
        return "FAIL"
    
    # Check expected cost
    if not math.isclose(cost, correct_travel_cost, abs_tol=0.001):
        return "FAIL"
    
    return "CORRECT"

# Test with provided solution data
solution_tour = [0, 1, 8, 4, 0]
solution_cost = 110.08796524611944

# Output the result of the check
print(verify_solution(solution_tour, solution_cost))