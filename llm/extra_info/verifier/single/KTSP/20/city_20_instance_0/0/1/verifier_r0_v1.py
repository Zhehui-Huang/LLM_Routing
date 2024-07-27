import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost):
    cities = {
        0: (8, 11),
        1: (40, 6),
        2: (95, 33),
        3: (80, 60),
        4: (25, 18),
        5: (67, 23),
        6: (97, 32),
        7: (25, 71),
        8: (61, 16),
        9: (27, 91),
        10: (91, 46),
        11: (40, 87),
        12: (20, 97),
        13: (61, 25),
        14: (5, 59),
        15: (62, 88),
        16: (13, 43),
        17: (61, 28),
        18: (60, 63),
        19: (93, 15)
    }
    
    # [Requirement 4]
    if not tour or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]
    if len(tour) != 5:
        return "FAIL"
    
    # Calculate the actual travel cost and validate it
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # [Requirement 3] & [Requirement 5]
    if abs(calculated_cost - total_cost) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# Solution provided
tour = [0, 1, 8, 4, 0]
total_travel_cost = 110.09

# Validate the solution
validation_result = verify_solution(tour, total_travel}`}_cost)
print(validation_result)