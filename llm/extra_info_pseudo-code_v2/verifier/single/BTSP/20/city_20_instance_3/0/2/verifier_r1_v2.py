import numpy as np
from scipy.spatial.distance import euclidean

def test_solution():
    # City coordinates
    coordinates = {
        0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
        5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
        10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
        15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
    }

    # Tour and data provided
    provided_tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
    provided_total_cost = 458.37
    provided_max_distance = 68.15

    # Calculations based on the provided tour data
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(provided_tour) - 1):
        # Calculate distances between consecutive cities in the tour
        dist = euclidean(coordinates[provided_tour[i]], coordinates[provided_tour[i + 1]])
        actual_total_cost += dist
        actual_max_distance = max(actual_max_distance, dist)

    # Requirements validation
    # Requirement 1: Start and end at city 0
    if provided_tour[0] != 0 or provided_tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once and only start/end city visited twice
    if len(set(provided_tour) - {0}) != 19 or provided_tour.count(0) != 2:
        return "FAIL"
    
    # Requirement 7: Match the provided total travel cost
    if not np.isclose(provided_total_cost, actual_total_cost, atol=0.01):
        return "FAIL"
    
    # Requirement 8: Match the provided maximum distance between consecutive cities
    if not np.isclose(provided_max_distance, actual_max_distance, atol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Execute the test function
result = test_solution()
print(result)