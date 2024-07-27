import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, expected_total_cost, expected_max_distance):
    cities = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
        (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
        (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
        (60, 63), (93, 15)
    ]
    
    # Requirement 1: Check if all cities are visited exactly once and tour starts and ends at city 0
    if len(tour) != 21 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(set(tour)) != len(cities) + 1:  # +1 because city 0 appears twice (start and end)
        return "FAIL"

    # Calculate total travel cost and max distance between consecutive cities
    total_travel_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_travel_cost += dist
        max_distance = max(max_distance, dist)
    
    # Requirement 2 & 3: Check total cost and max distance
    if not math.isclose(total_travel_cost, expected_total_cost, rel_tol=1e-9):
        return "FAIL"
    if not math.isclose(max_distance, expected_max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Correct parameter name in the function call
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 349.1974047195548
max_distance = 32.38826948140329

result = verify_solution(tour, total_travel_cost, max_output_distance)
print(result)  # Should print "CORRECT" if the solution meets all the requirements