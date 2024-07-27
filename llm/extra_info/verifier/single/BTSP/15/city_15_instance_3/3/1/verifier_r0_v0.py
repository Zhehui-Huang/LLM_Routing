import math

# Given city coordinates
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
          (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
          (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Provided solution
tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
total_cost = 373.61
max_distance = 94.11

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def test_solution(tour, cities):
    # Test Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test Requirement 2: Visit each city exactly once
    unique_cities = set(tour[1:-1])  # Ignore the repeating depot city     
    if len(unique_cities) != len(cities) - 1:  # Subtract 1 for depot city
        return "FAIL"
    
    # Test Requirement 3: Check calculated total cost and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Allow small floating point error margin for comparison
    if not (abs(calculated_total_cost - total_cost) < 0.1 and abs(calculated_max_distance - max_distance) < 0.1):
        return "FAIL"
    
    return "CORRECT"

# Run the test
result = test_solution(tour, cities)
print(result)