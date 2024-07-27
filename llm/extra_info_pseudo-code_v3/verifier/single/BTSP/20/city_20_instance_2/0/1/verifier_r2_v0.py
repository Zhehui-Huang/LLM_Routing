import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost, max_distance):
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
        19: (30, 48)
    }
    
    # [Requirement 1] Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visit each city exactly once
    if len(set(tour)) != 21 or len(tour) != 21:
        return "FAIL"
    
    # Compute the actual distances and total cost
    calculated_cost = 0
    max_calculated_distance = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        dist = euclidean_distance(*cities[city1], *cities[city2])
        calculated_cost += dist
        if dist > max_calculated_distance:
            max_calculated_distance = dist
    
    # [Requirement 3] The travel cost calculated as the Euclidean distance
    # [Requirement 6] Output total travel cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=0.01):
        return "FAIL"
    
    # [Requirement 4] Minimize the longest distance between any two consecutive cities
    # [Requirement 7] Output the maximum distance between two cities
    if not math.isclose(max_calculated_distance, max_distance, rel_tol=0.01):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Provided solution to verify
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
total_cost = 478.4306776278287
max_distance = 80.61017305526642

# Perform verification
print(verify_solution(tour, total_cost, max_distance))