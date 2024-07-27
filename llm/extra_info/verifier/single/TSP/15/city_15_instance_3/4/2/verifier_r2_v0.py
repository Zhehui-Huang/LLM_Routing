import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, cost):
    # Cities coordinates
    cities = [
        (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
        (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
        (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
    ]
    
    # [Requirement 1] Check start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if each city is visited exactly once
    if sorted(tour[1:-1]) != list(range(1, 15)):
        return "FAIL"
    
    # Calculate and [Requirement 3+5] verify total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Rounding for comparison to mimic the provided cost rounding
    calculated_cost = round(calculated_cost, 2)
    
    if calculated_cost != cost:
        return "FAIL"
    
    # [Requirement 4] Check if output format constraints are met (implicitly checked by previous conditions)
    
    return "CORRECT"

# Given solution verification
tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
reported_cost = 373.61
print(verify_tour(tour, reported_cost))