import math

# Given the cities coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Verify if the provided solution is correct
def verify_solution(tour, reported_total_cost):
    # Requirement 1: Tour must start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Must visit exactly 6 unique cities including the depot
    if len(set(tour)) != 6 or len(tour) != 7:
        return "FAIL"

    # Calculate the travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    
    # Requirement 4: Uses Euclidean distance formula, implicitly checked by using the formula in calculate_distance.
    
    # Requirement 5: Check if the total cost is roughly equal to the provided cost
    # Allowing slight variance due to floating point operations
    if not math.isclose(total_cost, reported_total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# The provided solution
tour = [0, 8, 5, 2, 1, 9, 0]
reported_total_cost = 183.85354044487238

# Verify the solution
result = verify_solution(tour, reported_total_ccost)
print(result)  # Expected "CORRECT"