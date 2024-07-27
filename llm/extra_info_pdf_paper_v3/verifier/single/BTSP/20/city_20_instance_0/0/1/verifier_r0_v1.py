import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, cities):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city should be visited exactly once
    if len(set(tour)) != len(cities) or sorted(set(tour)) != list(range(len(cities))):
        return "FAIL"
    
    # Requirement 3: Check distances
    max_distance = 0
    total_travel_cost = 0
    for i in range(1, len(tour)):
        dist = calculate_distance(cities[tour[i-1]], cities[tour[i]])
        total_travel_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Checking the provided solution values against expected values
    expected_max_distance = 32.39
    expected_total_cost = 349.1974047195548
    if not (abs(max_distance - expected_max_distance) < 0.01 and
            abs(total_travel_cost - expected_total_cost) < 0.01):
        return "FAIL"
    
    return "CORRECT"

# Test the corrected solution
solution_tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
city_positions = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
] 

# Execute test
result = test_solution(solution_tour, city_positions)
print(result)