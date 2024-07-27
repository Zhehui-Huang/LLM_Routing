import math

# Predefined cities from problem description
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Solution provided
tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
reported_total_cost = 322.50
reported_max_distance = 64.66

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, reported_total_cost, reported_max_distance):
    # Check Requirement 1: Visit each city once + return to depot
    if len(tour) != len(cities) + 1 or sorted(tour[:-1]) != sorted(cities.keys()):
        return "FAIL"
    
    # Check Requirement 4: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate travel cost and maximum distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Check Requirement 5: Correct total travel cost
    if not math.isclose(total_cost, reported_total_cost, abs_tol=0.01):
        return "FAIL"
    
    # Check Requirement 6: Correct maximum distance between consecutive cities
    if not math.isclose(max_distance, reported_max_distance, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Test the solution
test_result = verify_solution(tour, reported_total_cost, reported_max_distance)
print(test_result)