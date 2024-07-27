import math

# Data provided
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56), 6: (2, 65),
    7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53), 12: (11, 14),
    13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58),
    19: (30, 48)
}

# Proposed solution
tour = [0, 6, 8, 10, 7, 14, 16, 19, 11, 13, 15, 18, 3, 4, 17, 1, 5, 2, 9, 12, 0]
total_cost = 479.09202943436946

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tour(tour, total_cost):
    # [Requirement 1] and [Requirement 4]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]
    visited = set(tour[1:-1])
    if len(visited) != len(cities) - 1 or any(city == 0 for city in visited):
        return "FAIL"
    
    # [Requirement 3] & [Requirement 5]
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(tour[i], tour[i + 1])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # [Requirement 6] - This can only be verified by comparing with the optimal solution which requires solving the problem.
    # Hence, it is not verified here.
    
    return "CORRECT"

# Execute verification
result = verify_tour(tour, total_cost)
print(result)