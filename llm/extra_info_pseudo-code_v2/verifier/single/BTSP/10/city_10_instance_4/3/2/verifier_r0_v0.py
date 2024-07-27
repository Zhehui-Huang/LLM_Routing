import numpy as np

def test_solution(tour, total_travel_cost, max_distance):
    cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]
    
    # [Requirement 1]
    # Check if the tour starts and ends at the depot city 0 and visits each city exactly once
    if tour[0] != 0 or tour[-1] != 0 or sorted(tour) != sorted([0] + list(range(1, len(cities)))):
        return "FAIL"
    
    # Calculate travel distances
    def euclidean_distance(a, b):
        return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    
    computed_cost = 0
    computed_max_distance = 0
    
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        computed_cost += distance
        if distance > computed_max_distance:
            computed_max_distance = distance
    
    # [Requirement 2]
    # Not possible to verify optimally without solving the problem or known optimal result.
    
    # [Requirement 3]
    if not (tour and tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # [Requirement 4]
    if computed_cost != total_travel_cost:
        return "FAIL"
    
    # [Requirement 5]
    if computed_max_distance != max_distance:
        return "FAIL"
    
    return "CORRECT"

# Given solution details
tour = []
total_travel_cost = 0
max_distance = float('inf')

# Test the solution
result = test_solution(tour, total_travel_cost, max_distance)
print(result)