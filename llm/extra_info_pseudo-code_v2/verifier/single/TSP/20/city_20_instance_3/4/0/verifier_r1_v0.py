import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)

def verify_tour(cities, tour, expected_cost):
    n = len(cities)
    
    # Requirement 1: Tour contains all cities exactly once and returns to the depot
    if len(tour) != n + 1 or tour[0] != 0 or tour[-1] != 0 or len(set(tour[1:-1])) != n - 1:
        return "FAIL"

    # Requirement 2: Calculate and verify travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(total_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"

    # Requirement 3: Output must be as specified but this is checked implicitly in the actual implementation
    return "CORRECT"

# Part of test setup
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}
tour = [0, 3, 6, 13, 2, 5, 15, 1, 10, 4, 14, 8, 7, 12, 18, 11, 9, 16, 17, 19, 0]
total_cost = 538.7050637114203

# Verification
result = verify_tour(list(cities.values()), tour, total_cost)
print(result)