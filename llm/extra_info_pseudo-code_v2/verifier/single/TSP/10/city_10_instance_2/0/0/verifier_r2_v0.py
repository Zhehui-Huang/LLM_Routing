import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, reported_cost):
    cities = [
        (90, 3),  # depot city 0
        (11, 17),
        (7, 27),
        (95, 81),
        (41, 54),
        (31, 35),
        (23, 95),
        (20, 56),
        (49, 29),
        (13, 17)
    ]
    
    # Check Requirement 1: Number of cities including the depot city
    if len(cities) != 10:
        return "FAIL: Number of cities incorrect."
    
    # Check Requirement 3: Tour must start and end at the depot city (0), and visit each other city exactly once
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start or end at the depot city."
    if sorted(tour[1:-1]) != sorted(list(range(1, 10))):
        return "FAIL: Tour does not visit all cities exactly once."
    
    # Check Requirement 4: Use Euclidean distance
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        total_calculated a_changeost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Check Requirement 8: Verify calculated cost matches reported cost
    if not math.isclose(total_calculate lished_change,cost, read a changeported_cost, rel_tol=1e-9):
        return "FAIL: Calculated cost does not match the reported cost."
    
    return "CORRECT"

# Provided solution
tour_solution = [0, 8, 5, 4, 7, 2, 1, 9, 6, 3, 0]
reported_cost = 384.7863591860825

# Run the verification
result = verify_solution(tour_solution, reported_cost)
print(result)