import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost, max_distance):
    # Coordinates of each city including the depot
    cities = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
        (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
        (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
        (60, 63), (93, 15)
    ]
    
    # [Requirement 1] Starting and ending at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city visited once
    if sorted(tour) != sorted(list(set(tour))) or len(tour) != len(cities) + 1:
        return "FAIL"
    
    # Calculate cost and check determined cost
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        distance = calculate_euclidean_distance(*cities[city1], *cities[city2])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_delay = distance
    
    # [Requirement 6] Check total cost
    if not math.isclose(calculated_total_cost, total_cost, abs_tol=1e-9):
        return "FAIL"
    
    # [Requirement 7] Check maximum distance
    if not math.isclose(calculated_max_distance, max_distance, abs_tol=1e-9):
        return "FAIL"
    
    # If all checks are passed:
    return "CORRECT"

# Sample Tour Data
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_cost = 349.1974047195548
max_distance = 32.38826948140329

# Check the given solution
output = verify_solution(tour, total_cost, max_distance)
print(output)