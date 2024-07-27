import math

def calculate_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, cost):
    cities = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
        (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
        (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    
    # [Requirement 1] Check start and end at the depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check exactly 13 cities are visited, including the depot
    if len(set(tour)) != 13:
        return "FAIL"
    
    # [Requirement 3] Calculate and check the travel total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if abs(calculated_cost - cost) > 1e-6:
        return "FAIL"
    
    # Successfully passed all checks
    return "CORRECT"

# Tour provided
tour = [0, 4, 14, 8, 7, 12, 13, 19, 5, 15, 17, 9, 16, 0]
cost = 365.7923523476108

# Run the unit test
test_result = verify_solution(tour, cost)
print(test_result)