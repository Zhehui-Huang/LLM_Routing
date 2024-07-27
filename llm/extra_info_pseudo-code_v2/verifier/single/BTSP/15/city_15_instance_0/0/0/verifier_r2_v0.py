import math

# Provided solution
tour = [0, 8, 10, 1, 11, 14, 12, 9, 4, 7, 3, 5, 6, 2, 13, 0]
total_travel_cost = 363.73
max_distance = 63.6

# Given city coordinates
city_coordinates = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_solution(tour, total_travel_cost, max_distance, city_coordinates):
    if not tour:
        return "FAIL"
    
    # Test Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test Requirement 2: Visit each city exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(city_coordinates) + 1 or any(not (i in unique_cities) for i in city_coordinates):
        return "FAIL"
    
    # Test Requirement 3: Check distance calculation and Requirement 6: Sum of distances
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
        calculated_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    # Check the distance calculation with tolerance due to float operations
    if not (math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2) and
            math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2)):
        return "FAIL"
    
    return "CORRECT"

# Execute the unit test
result = test_solution(tour, total_travel_cost, max_distance, city_coordinates)
print(result)