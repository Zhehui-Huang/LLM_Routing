import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_solution(cities, tour, reported_cost):
    # Verify Requirement 2: The robot starts and ends at the depot city, visiting each other city exactly once
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL"
    
    # Verify Requirement 3: Calculate the total travel cost and check against the reported cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # We allow a small margin for floating-point arithmetic differences
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    # If all checks pass, return "CORRECT"
    return "CORRECT"

# City coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Provided solution
tour_solution = [0, 10, 15, 4, 3, 6, 12, 7, 16, 5, 9, 2, 14, 11, 1, 13, 18, 17, 8, 19, 0]
total_cost_solution = 379.72475773064514

# Test the solution
result = verify_solution(cities, tour_solution, total_cost_solution)
print(result)