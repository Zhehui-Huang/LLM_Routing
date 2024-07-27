import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_cost, max_distance):
    # Given cities' coordinates
    cities = [
        (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
        (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
        (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
    ]
    
    # Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Requirement 3 and Total Cost check
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
            
    if abs(calculated_total_cost - total_cost) > 1e-5:
        return "FAIL"
    
    # Requirement 4
    if abs(calculated_max_distance - max_distance) > 1e-5:
        return "FAIL"
    
    # Requirement 5 is assumed to be correct if all other checks are passed, as it's about output format.
    
    return "CORRECT"

# Test data provided in the problem
tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
total_travel_cost = 373.97393412233544
maximum_distance = 63.60031446463138

# Run the test
result = test_solution(tour, total_travel_cost, maximum_distance)
print(result)