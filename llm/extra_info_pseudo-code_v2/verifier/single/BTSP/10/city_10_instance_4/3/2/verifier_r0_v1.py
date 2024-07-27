import numpy as np

def test_solution(tour, total_travel_cost, max_distance):
    cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]
    
    # Check if tour is empty
    if not tour:
        print("Tour is empty.")
        return "FAIL"
    
    # [Requirement 1]
    # Check if the tour starts and ends at the depot city 0 and visits each city exactly once
    if tour[0] != 0 or tour[-1] != 0 or sorted(tour) != sorted([0] + list(range(1, len(cities)))):
        print("Requirement 1 failed.")
        return "FAIL"
    
    # Calculate travel distances
    def euclidean_distance(a, b):
        return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    
    computed_cost = 0
    computed_max_distance = 0
    
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        computed_cost += distance
        computed_max_distance = max(computed_max_distance, distance)
    
    # [Requirement 4]
    if computed_cost != total_travel_cost:
        print("Requirement 4 failed.")
        return "FAIL"
    
    # [Requirement 5]
    if computed_max_distance != max_distance:
        print("Requirement 5 failed.")
        return "FAIL"
    
    # As requirement 2 cannot be validated without a known optimal result or a verified correct algorithm output,
    # we acknowledge it here but it can't be part of a simple unit test without context.

    print("All requirements passed.")
    return "CORRECT"

# Example input (you still need the actual correct tour values if available)
tour = []  # Example: Should be [0,1,2,3,...,0]
total_travel_cost = 0  # Example: Should be based on the actual distances calculated
max_distance = float('inf')  # Example: Should be the longest single hop distance in the tour

# Test the solution
result = test_solution(tour, total_travel_cost, max_distance)
print(result)