import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost):
    coordinates = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
        (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
        (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
        (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    
    # Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once, except the depot
    if set(tour) != set(range(len(coordinates))):
        return "FAIL"
    if len(tour) != len(set(tour)):
        repeated_cities = len(tour) - len(set(tour))
        if repeated_cities != 1:  # Allow one repetition for the depot city
            return "FAIL"
    
    # Requirement 4: Tour format check (implicitly checked by inspecting the first and last elements)

    # Requirement 3: Calculate travel cost using the Euclidean distance and compare with provided cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        x1, y1 = coordinates[city_from]
        x2, y2 = coordinates[city_to]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Requirement 5: Check the output cost
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Given solution to test
tour = [0, 0, 3, 11, 10, 1, 15, 17, 16, 9, 5, 19, 6, 13, 2, 12, 18, 7, 8, 14, 4, 0]
total_travel_cost = 549.96

# Execute the test
result = verify_solution(tour, total_travel_count)
print(result)