import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Cities coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def test_solution(tour, reported_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Calculate the actual travel cost based on the provided tour
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Comparing the actual calculated cost to the reported cost using a tolerance
    if not math.isclose(actual_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, 6, 2, 13, 8, 9, 14, 0]
reported_cost = 130.6658168109853

# Test the solution
result = test_solution(tour, reported_cost)
print(result)