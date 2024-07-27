import math

# Given tour and cost
tour = [0, 13, 8, 10, 5, 9, 14, 1, 4, 6, 0]
reported_cost = 205.013372195941

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def calculate_distance(city1, city2):
    """Compute Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_solution(tour, reported_cost):
    # [Requirement 1] Check start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if exactly 10 cities including the depot city
    if len(set(tour)) != 10:
        return "FAIL"
    
    # Calculate the actual travel cost
    actual_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    
    # [Requirement 3] Check the reported cost matches calculated cost approximately due to float precision
    if not math.isclose(actual_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Perform the test
result = validate_solution(tour, reported_cost)
print(result)