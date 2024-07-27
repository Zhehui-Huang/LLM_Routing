import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, cost):
    cities = [
        (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
        (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), 
        (70, 95), (29, 64), (32, 79)
    ]
    
    # [Requirement 1] Check the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check the robot visits each non-depot city exactly once
    non_depot_cities = set(range(1, len(cities)))
    visited_cities = set(tour[1:-1])
    if visited_cities != non_depot_cities:
        return "FAIL"

    # [Requirement 4] Compute travel cost and compare
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Allows a small floating-point tolerance for comparison
    if not math.isclose(calculated_cost, cost, rel_tol=1e-5):
        return "FAIL"
    
    # If all requirements are met
    return "CORRECT"

# Provided tour solution
tour_solution = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
total_cost_solution = 373.61498801130097

# Perform the test
test_result = test_solution(tour_solution, total_cost_solution)
print(test_result)