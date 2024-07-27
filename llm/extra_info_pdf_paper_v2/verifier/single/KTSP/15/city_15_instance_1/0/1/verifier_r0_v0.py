import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_solution(tour, total_cost):
    # Coordinates of the cities
    coordinates = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
                   (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
                   (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]
    
    # Requirement 1: Start and end at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly 6 cities
    if len(tour) != 7 or len(set(tour)) != 6:  # includes city 0 twice, but 6 unique cities
        return "FAIL"
    
    # Requirement 3: Validate the path cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    
    if abs(calculated_cost - total_cost) > 1e-5:  # allowing a tiny precision error tolerance
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Provided solution
tour = [0, 6, 1, 7, 3, 9, 0]
total_cost = 118.8954868377263

# Validate the solution
result = validate_solution(tour, total_cost)
print(result)