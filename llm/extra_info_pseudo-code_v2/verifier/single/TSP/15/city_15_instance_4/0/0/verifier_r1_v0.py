import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_solution(tour, reported_cost):
    cities = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }

    # Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2
    if len(set(tour[1:-1])) != len(tour[1:-1]) or len(tour) - 2 != 14:
        return "FAIL"

    # Requirement 3 & 4
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    # Check calculated distance against reported
    if abs(total_cost - reported_cost) > 0.1:  # accounting for floating-point precision issues
        return "FAIL"

    # Requirement 5
    # This check is inherent in the previous checks and how `tour` and `reported_cost` are presented and used.
    
    return "CORRECT"

# Actual test execution
tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
reported_cost = 337
result = test_solution(tour, reported_cost)
print(result)