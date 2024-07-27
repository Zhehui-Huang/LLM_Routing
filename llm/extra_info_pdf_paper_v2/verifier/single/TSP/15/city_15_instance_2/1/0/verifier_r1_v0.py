import math

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, reported_cost, cities):
    # [Requirement 1] Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visits each city exactly once (except depot, 0, which is visited twice)
    visited = set(tour)
    if len(visited) != len(cities) or any(i not in visited for i in range(len(cities))):
        return "FAIL"
    
    # [Requirement 3] Calculate the total travel cost
    cost = 0.0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Checking reported cost with a tolerance for floating point arithmetic issues
    if not math.isclose(cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Provided solution details
tour = [0, 6, 2, 7, 13, 9, 10, 5, 3, 4, 12, 11, 8, 1, 14, 0]
reported_cost = 318.58648206048457

# City coordinates: 0 (depot) to 14
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), 
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Verification
result = verify_solution(tour, reported_cost, cities)
print(result)