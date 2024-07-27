import math

# Define the function to calculate Euclidean distance between two points
def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Test input data structure
cities = {
    0: (9, 93),
    1: (8, 51),
    10: (19, 65),
    8: (19, 76)
}

# Define the function to validate the proposed solution
def validate_solution(tour, total_cost):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Exactly 4 cities including the depot
    if len(set(tour)) != 4:
        return "FAIL"
    
    # Requirement 4: Tour should start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate the actual total tour cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Requirement 5: Check if the reported total cost matches the calculated cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Provided test case evaluation
test_tour = [0, 1, 10, 8, 0]
test_total_cost = 48.53

# Run validation
output = validate_solution(test_tour, test_total_cost)
print(output)