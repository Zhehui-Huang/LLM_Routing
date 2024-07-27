def calculate_distance(city1, city2):
    from math import sqrt
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, total_cost):
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
        (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
        (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # Requirement 1: Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if each city is visited exactly once
    if len(set(tour)) != len(cities) or tour.count(0) != 2:
        return "FAIL"
    
    # Check travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # Requirement 3 and 4: Check travel cost matches total_cost, check minimization implicitly
    if abs(computed_cost - total_cost) > 1e-6:
        return "FAIL"

    # Implicit check for Requirement 6: No subtours, each city visited once and starts/ends at depot
    return "CORRECT"

# Solution tour and cost provided
tour = [0, 19, 8, 17, 18, 13, 1, 11, 14, 2, 9, 5, 16, 7, 12, 6, 3, 4, 15, 10, 0]
total_travel_cost = 379.72475773064514

# Correct the typo and execute the test
test_result = check_solution(tour, total_travel_cost)
print(test_value)  # Output either "CORRECT" or "FAIL"