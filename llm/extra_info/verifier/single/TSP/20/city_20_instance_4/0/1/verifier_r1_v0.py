import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, total_cost):
    # City coordinates in the same order as presented (index matches the city number)
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
        (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
        (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # [Requirement 1] Tour starts and ends at the depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city, except for the depot city, visited exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) - 1 or set(range(1, 20)) != unique_cities:
        return "FAIL"
    
    # [Requirement 3] Calculate and compare the travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Proposed solution to verify
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
total_cost = 410.03585920085146

# Verify the solution
result = check_solution(tour, total_cost)
print(result)  # Expected output: "CORRECT" if correct otherwise "FAIL"