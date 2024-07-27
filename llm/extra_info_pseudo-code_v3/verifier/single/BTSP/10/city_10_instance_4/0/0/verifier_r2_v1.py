from math import sqrt

def compute_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, max_distance):
    cities = [
        (79, 15), (79, 55), (4, 80), (65, 26), (92, 9), 
        (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)
    ]
    
    # [Requirement 1] - Check all cities are visited once, starting and ending at depot
    if tour[0] != 0 or tour[-1] != 0 or len(set(tour)) != len(tour):
        return "FAIL"
    if sorted(tour[1:-1]) != sorted(range(1, 10)):
        return "FAIL"
    
    # Compute the total travel cost and max distance measured
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = compute_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    # [Requirement 4] - Check total travel cost
    if not (abs(calculated_total_cost - total_cost) < 1e-2):
        return "FAIL"
    
    # [Requirement 5] - Check max distance
    if not (abs(calculated_max_distance - max_distance) < 1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
test_tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
test_total_cost = 408.41
test_max_distance = 61.68

# Check if the provided solution is correct based on the unit test 
result = verify_solution(test_tour, test_total_cost, test_max_distance)
print(result)