import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, max_distance):
    # Cities coordinates
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
        (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
        (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
        (64, 72), (14, 89)
    ]
    
    # Check Requirement 1 & 5
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Calculate distances and total travel cost
    calculated_cost = 0
    observed_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += distance
        observed_max_distance = max(observed_max_distance, distance)
    
    # Check Requirement 6
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Check Requirement 7
    if not math.isclose(observed_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Given values
tour = [0, 19, 10, 9, 11, 8, 12, 7, 13, 6, 14, 5, 15, 4, 16, 3, 17, 2, 18, 1, 0]
total_travel_cost = 925.92
maximum_distance = 75.45

# Verify the solution
result = verify_solution(tour, total_travel_cost, maximum_distance)
print(result)