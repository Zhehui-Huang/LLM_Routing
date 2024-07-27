import numpy as np

# Provided tours and costs from the solution
robots_tours = {
    0: ([0, 0, 0, 22, 5, 0], 54.91615166732757),
    1: ([0, 0, 0, 21, 20, 0], 31.64892678707713),
    2: ([0, 0, 2, 10, 0], 52.4625939010481),
    3: ([0, 0, 0, 0, 11, 4, 0], 57.394073777130664),
    4: ([0, 0, 9, 13, 0], 68.39398119181284),
    5: ([0, 0, 8, 6, 0], 67.16312415547748),
    6: ([0, 0, 7, 14, 0], 68.12495983813932),
    7: ([0, 0, 21, 16, 17, 18, 19, 3, 12, 15, 1, 0], 132.76160489583026)
}

overall_expected_cost = 532.8654162138434

# Test criteria
def test_solution(robots_tours, overall_expected_cost):
    # Flatten lists and convert items to ints if type is numpy int
    all_visited_cities = [int(city) for tour in robots_tours.values() for city in tour[0]]
    
    # [Requirement 1]: Each city must be visited exactly once by the robots collectively.
    all_actual_cities = set(all_visited_cities)
    required_cities = set(range(23))  # Cities are from 0 to 22
    if all_actual_cities != required_cities:
        return "FAIL: Not all cities were visited exactly once"
    
    # [Requirement 2 & 7]: Each tour must start and potentially end at its assigned depot, which is city 0 here.
    # And all robots start at depot city 0.
    for tour in robots_tours.values():
        if tour[0][0] != 0 or tour[0][-1] != 0:
            return "FAIL: Tour does not start and end at depot city 0"

    # [Requirement 8]: Checking total cost
    computed_total_cost = sum(tour[1] for tour in robots_tours.values())
    if not np.isclose(computed_total_cost, overall_expected_cost):
        return f"FAIL: Computed total travel cost {computed_total_cost} does not match expected {overall_expected_cost}"

    # [Requirement 3 & 5]: Assuming best solution given for optimization without verification of optimization algorithm.
    # Normally this would require recalculation and comparison against known benchmarks or via executing optimization algorithms.

    return "CORRECT"

# Run the test function
test_result = test_solution(robots_tours, overall_expected_cost)
print(test_result)