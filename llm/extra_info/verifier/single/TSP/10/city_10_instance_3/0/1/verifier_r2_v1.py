import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def test_solution(tour, reported_cost):
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # [Requirement 1] Check if all cities are visited exactly once and starts/ends at depot
    if len(tour) != len(cities) + 1:
        return "FAIL"
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour[1:-1]) != sorted(list(cities.keys() - {0})):  # Ensure only cities other than depot are visited once
        return "FAIL"
    
    # [Requirement 2] Calculate total travel cost and compare with reported cost
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    total_distance_rounded = round(total_distance, 2)  # Fix the variable name typo here
    
    if abs(total_distance_rounded - reported_cost) > 0.01:  # tolerance for floating point arithmetic
        return "FAIL"
    
    # Method mostly verifies structure and computations according to the specifications.
    
    return "CORRECT"

# Provided solution details
tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
total_travel_cost = 315.56

# Applying the test
result = test_solution(tour, total_travel_matrix_cost)
print(result)