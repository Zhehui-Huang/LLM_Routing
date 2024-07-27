import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost, max_distance):
    # Coordinates for each city
    coordinates = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
        (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
        (78, 76), (68, 45), (50, 28), (69, 9)
    ]
    
    # [Requirement 1] Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL [Requirement 1]"
    
    # [Requirement 2] Check if each city is visited exactly once
    if sorted(tour[:-1]) != list(range(20)):
        return "FAIL [Requirement 2]"
    
    # [Requirement 3] Calculate total travel cost and verify
    calculated_cost = 0.0
    longest_edge = 0.0
    for i in range(len(tour) - 1):
        a = coordinates[tour[i]]
        b = coordinates[tour[i + 1]]
        distance = calculate_euclidean_distance(a[0], a[1], b[0], b[1])
        calculated_cost += distance
        if distance > longest_edge:
            longest_edge = distance
    
    if abs(calculated_cost - total_travel_cost) > 0.01:
        return "FAIL [Requirement 3]"
    
    # Verify max edge distance
    if abs(longest_edge - max_distance) > 0.01:
        return "FAIL [Requirement 3]"

    return "CORRECT"

# Provided solution
tour = [0, 14, 3, 5, 7, 4, 10, 11, 16, 17, 18, 19, 15, 8, 1, 13, 12, 2, 9, 6, 0]
total_travel_cost = 387.9960041009033
max_distance = 32.57299494980466

# Execute the verification
verification_result = verify_solution(tour, total_travel_cost, max_distance)
print(verification_result)