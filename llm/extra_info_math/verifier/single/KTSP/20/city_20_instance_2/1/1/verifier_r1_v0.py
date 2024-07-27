import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cost):
    # City coordinates map
    cities = {
        0: (3, 26),
        1: (85, 72),
        2: (67, 0),
        3: (50, 99),
        4: (61, 89),
        5: (91, 56),
        6: (2, 65),
        7: (38, 68),
        8: (3, 92),
        9: (59, 8),
        10: (30, 88),
        11: (30, 53),
        12: (11, 14),
        13: (52, 49),
        14: (18, 49),
        15: (64, 41),
        16: (28, 49),
        17: (91, 94),
        18: (51, 58),
        19: (30, 49)
    }
    
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly 10 cities
    if len(set(tour)) != 10:
        return "FAIL"
    
    # Requirement 3: Check if the cost is minimized
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1_id = tour[i]
        city2_id = tour[i+1]
        city1 = cities[city1_id]
        city2 = cities[city2_id]
        calculated_cost += calculate_distance(city1, city2)

    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given solution
solution_tour = [0, 2, 17, 12, 12, 17, 12, 17, 12, 8, 0]
solution_cost = 807.1100707699679

# Check if the solution is correct using the provided requirements
test_result = verify_solution(solution_tour, solution_cost)
print(test_result)