import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, cost):
    cities = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
        5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
        10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
    }

    # Requirement 1: Starts and ends at depot city 0, and begins and ends with city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Exactly 10 cities are visited.
    if len(set(tour)) != 10:
        return "FAIL"
    
    # Requirement 5: Output must include the tour with correct format.
    if not all(city in tour for city in set(tour)):
        return "FAIL"
    
    # Requirement 6: Check total travel cost.
    computed_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    if not math.isclose(computed_cost, cost, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 1, 4, 12, 7, 11, 10, 5, 14, 0]
cost = 210.70043112438773

# Verify the solution
result = verify_solution(tour, cost)
print(result)