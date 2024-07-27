import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(solution):
    tour = solution['Tour']
    total_cost = solution['Total travel cost']
    max_distance = solution['Maximum distance between consecutive cities']
    
    # City Coordinates (index corresponds to city number)
    coordinates = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
        (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
        (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
        (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]

    # Requirement 1: The robot must visit each city exactly once, starting and ending at the depot
    if len(tour) != len(coordinates) + 1:
        return "FAIL"
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour[1:-1]) != list(range(1, len(coordinates))):
        return "FAIL"

    # Calculate the actual total travel cost and maximum distance between any two consecutive cities
    computed_total_cost = 0
    computed_max_distance = 0
    
    for i in range(len(tour) - 1):
        current_distance = euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        computed_total_cost += current_distance
        if current_distance > computed_max_distance:
            computed_max_distance = current_distance

    # Requirement 2: Travel cost check
    if not math.isclose(total_cost, computed_total_cost, abs_tol=1e-9):
        return "FAIL"
    
    # Requirement 3: Maximize the minimum distance check
    if not math.isclose(max_distance, computed_max_distance, abs_tol=1e-9):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Given solution
solution = {
    'Tour': [0, 0], 
    'Total travel cost': 0.0,
    'Maximum distance between consecutive cities': 0.0
}

# Verify the solution
verification_result = verify_solution(solution)
print(verification_result)