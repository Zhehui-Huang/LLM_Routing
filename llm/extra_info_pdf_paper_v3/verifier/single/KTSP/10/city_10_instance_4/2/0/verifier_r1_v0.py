import math

# Provided coordinates from the problem
coordinates = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Provided tour and travel cost from your solution
provided_tour = [0, 4, 0, 3, 6, 5, 7, 1, 9]
provided_cost = 217.51393154953843

def compute_euclidean_distance(point1, point2):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def validate_solution(tour, total_cost):
    # Requirement 1: Check if all provided cities are within the correct range
    if not all(city in coordinates for city in tour):
        return "FAIL"
    
    # Requirement 2: Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 3: Check if the tour visits exactly 8 cities including the depot
    if len(set(tour)) != 8 + 1:  # +1 because the depot can be visited twice and is included in the set
        return "FAIL"
    
    # Requirement 6: Output should start and end at depot 0 (redundant given Req. 2 check, still explicit)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate the travel cost and compare with provided cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += compute_euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    # Requirement 7: Check if provided cost is approximately equal to calculated cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Invoke the validation on the provided solution
result = validate_solution(provided_tour, provided_cost)
print(result)