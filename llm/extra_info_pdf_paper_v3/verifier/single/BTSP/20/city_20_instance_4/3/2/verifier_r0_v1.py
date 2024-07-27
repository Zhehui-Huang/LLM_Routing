import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tour, total_cost, max_distance):
    # City coordinates as given
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
        (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
        (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
        (64, 72), (14, 89)
    ]
    
    # Requirement 1: Start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city visited exactly once, depot visited twice
    if sorted(tour[:-1]) != list(range(20)):
        return "FAIL"
    
    # Calculate total travel cost and max distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += dist
        calculated_max_distance = max(calculated_max_distance, dist)
        
    # Requirement 3, 4, 5, 6, 7 verification
    if not (math.isclose(calculated_total_cost, total_cost, rel_tol=1e-2) and 
            math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2)):
        return "FAIL"
    
    return "CORRECT"

# Given solution details
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
total_cost = 410.04
max_distance = 89.01

# Validate the solution
result = validate_solution(tour, total_cost, max_distance)
print(result)