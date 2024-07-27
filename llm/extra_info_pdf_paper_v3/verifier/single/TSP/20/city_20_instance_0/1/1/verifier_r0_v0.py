import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(cities, tour, total_cost):
    # Verify Requirement 1
    if len(cities) != 20:
        return "FAIL"
    
    # Verify Requirement 2
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(set(tour)) != len(cities) + 1:
        return "FAIL"
    
    # Verify Requirement 3
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += euclidean_dist(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # There are no checks for Requirement 4 (shortest path) as it requires computational verification beyond input-output checks.
    
    # Requirement 5: output format already matched in the provided solution output
    
    return "CORRECT"

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Solution from the user
tour = [0, 4, 0]
total_cost = 36.76955262170047

# Verify the solution
print(verify_solution(cities, tour, total_cost))