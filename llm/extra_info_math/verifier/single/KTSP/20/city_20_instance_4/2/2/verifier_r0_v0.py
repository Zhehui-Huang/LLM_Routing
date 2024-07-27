import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tsp_solution(tour, expected_cost):
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
        (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
        (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # Test Requirement 1: Starts and ends at the depot city (city 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test Requirement 2: Visits exactly 16 cities including the depot city.
    if len(set(tour)) != 16 or len(tour) != 17:
        return "FAIL"
    
    # Test Requirement 3: Calculate the total travel cost.
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Data as per the claimed solution
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 0]
total_travel_cost = 285.96

# Asserting the test cases
result = test_tsp_solution(tour, total_travel_cost)
print(result)