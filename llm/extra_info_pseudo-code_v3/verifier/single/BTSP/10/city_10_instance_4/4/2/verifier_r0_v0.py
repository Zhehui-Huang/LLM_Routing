import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Proposed solution details
solution_tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
solution_total_cost = 408.41360886151256
solution_max_distance = 61.68468205316454

def test_solution_requirements():
    # Requirement 1: Start and end at the depot city 0
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city must be visited exactly once plus depot city twice (start and end)
    if sorted(solution_tour) != sorted([0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        return "FAIL"
    
    # Requirement 5: Check the tour sequence starts and ends at depot city
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    
    # Requirement 6 & 7: Calculate total cost and verify maximum distance
    calc_total_cost = 0
    max_distance = 0
    for i in range(len(solution_tour) - 1):
        current_distance = euclidean_distance(cities[solution_tour[i]], cities[solution_tour[i + 1]])
        calc_total_cost += current_distance
        if current_distance > max_distance:
            max_distance = current_distance
    
    if not math.isclose(calc_total_space, solution_total_cost, abs_tol=0.001):
        return "FAIL"
    if not math.isclose(max_distance, solution_max_distance, abs_tol=0.001):
        return "FAIL"

    return "CORRECT"

# Execute the unit test
test_output = test_solution_requirements()
print(test_output)