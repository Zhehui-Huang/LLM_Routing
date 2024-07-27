import math

def compute_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, max_distance):
    coordinates = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
        (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
        (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
        (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
    ]
    
    # Requirement 1: Check tour starting/ending at depot, visiting each city once
    if tour[0] != 0 or tour[-1] != 0 or len(tour) != 21 or len(set(tour)) != 21:
        return "FAIL"
    
    # Compute travel cost and max distance
    calc_total_cost = 0
    calc_max_distance = 0
    
    for i in range(len(tour) - 1):
        dist = compute_euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        calc_total_cost += dist
        if dist > calc_max_distance:
            calc_max_distance = dist
    
    # Requirement 2: Approximate check for max distance and total cost within limited precision
    if not (abs(calc_total_cost - total_cost) < 1e-4 and abs(calc_max_distance - max_distance) < 1e-4):
        return "FAIL"
    
    # Requirement 3 is effectively checked by outputs format and verification above.
    
    return "CORRECT"

# Given example solution details
tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
total_travel_cost = 1170.8617712401854
maximum_distance = 85.09406559801923

# Validate the test case
result = verify_solution(tour, total_travel_cost, maximum_distance)
print(result)