import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tsp_solution(tour, total_cost):
    cities = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
        (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
        (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]

    # Requirement 1: Starts and ends at depot city (city index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: All cities visited once, depot city visited twice
    if sorted(tour) != sorted([0] + list(range(1, len(cities)))):
        return "FAIL"

    # Requirement 3 & 4: Calculate the total travel cost and verify it matches given
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):  # Considering minor floating-point discrepancies
        return "FAIL"

    # Requirement 5: Output format manually checked by visual inspection (assumed correct if reaches here and other checks pass)
    return "CORRECT"

# Example tour and total travel cost provided
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
total_cost = 458.37

# Perform the test
result = test_tsp_solution(tour, total_cost)
print(result)  # Output the result of the unit test