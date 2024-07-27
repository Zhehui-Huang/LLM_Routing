import math

# Given coordinates data
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Solution provided
solution_tour = [0, 4, 16, 0]
solution_cost = 78.50389503997762

def calculate_euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def verify_solution(tour, reported_cost):
    # Verify Requirement 1: Correct tour format and visits all cities exactly once
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(set(tour[1:-1])) != len(tour[1:-1]) or set(tour[1:-1]) != set(cities.keys()) - {0}:
        return "FAIL"
    
    # Verify Requirement 2: Correctly calculate total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Verify Requirement 3: Correct output format handled in initial checks
    return "CORRECT"

# Output the correctness of the solution
result = verify_solution(solution_tour, solution_cost)
print(result)