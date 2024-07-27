import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # Cities coordinates
    cities = {
        0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82),
        4: (97, 28), 5: (0, 31), 6: (8, 62), 7: (74, 56),
        8: (85, 71), 9: (6, 76)
    }
    
    # Requirements verification
    # Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2
    if len(tour) != 8 or len(set(tour)) != 8:
        return "FAIL"
    
    # Requirement 4
    if not isinstance(tour, list) or any(not isinstance(city, int) for city in tour):
        return "FAIL"

    # Calculate the traveled distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Requirement 5
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-6):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Given solution details
tour = [0, 8, 9, 6, 5, 1, 7, 0]
total_cost = 234.8502891406361

# Check if the solution meets the requirements
result = verify_solution(tour, total_cost)
print(result)