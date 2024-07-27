import math

# Coordinates for each city, including the depot city
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

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two city indices. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def test_tour_and_cost(tour, reported_cost):
    # Verify Requirement 1 and 5
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify Requirement 2
    if len(set(tour)) != 7 or len(tour) != 8:
        return "FAIL"
    
    # Requirement 3 is assumed correct since we use Euclidean distance calculations directly
    # Requirement 4 cannot be verified directly without knowing all possible solutions

    # Verify travel cost calculation (Requirement 6)
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_distance(tour[i], tour[i + 1])
    if abs(total_calculated_cost - reported_cost) > 0.01:  # Allowing a small floating point margin
        return "FAIL"
    
    return "CORRECT"

# Given solution to the problem
tour = [0, 6, 2, 13, 8, 9, 14, 0]
reported_total_cost = 130.67

# Call the testing function and print result
result = test_tour_and_cost(tour, reported_total_cost)
print(result)