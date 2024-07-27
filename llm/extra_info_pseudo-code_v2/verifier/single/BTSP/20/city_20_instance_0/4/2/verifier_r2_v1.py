import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(tour, total_cost, max_distance):
    # City coordinates
    coordinates = [
        (8, 11),   # 0
        (40, 6),   # 1
        (95, 33),  # 2
        (80, 60),  # 3
        (25, 18),  # 4
        (67, 23),  # 5
        (97, 32),  # 6
        (25, 71),  # 7
        (61, 16),  # 8
        (27, 91),  # 9
        (91, 46),  # 10
        (40, 87),  # 11
        (20, 97),  # 12
        (61, 25),  # 13
        (5, 59),   # 14
        (62, 88),  # 15
        (13, 43),  # 16
        (61, 28),  # 17
        (60, 63),  # 18
        (93, 15)   # 19
    ]

    # Check Requirement 1: Tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Each city must be visited exactly once
    if sorted(tour[:-1]) != list(range(len(coordinates))):
        return "FAIL"

    # Calculate actual total travel cost and max distance
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        distance = euclidean_distance(x1, y1, x2, y2)
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Check Requirements 6 and 7: total travel cost and maximum distance
    if not (math.isclose(calculated_cost, total_cost, abs_tol=1e-2) and
            math.isclose(calculated_max_distance, max_distance, abs_tol=1e-2)):
        return "FAIL"
    
    return "CORRECT"

# Test data from the solution provided
tour = [0, 8, 5, 13, 17, 6, 2, 10, 18, 3, 15, 11, 12, 9, 7, 14, 16, 4, 19, 1, 0]
total_travel_cost = 509.56
max_distance_between_consecutive_cities = 68.07

# Validate the provided tour solution
result = verify_solution(tour, total_travel_cost, max_distance_between_consecutive_cities)
print(result)