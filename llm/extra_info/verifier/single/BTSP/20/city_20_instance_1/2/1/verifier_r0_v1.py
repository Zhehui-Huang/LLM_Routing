import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, total_cost, max_distance):
    cities_coordinates = [
        (14, 77),  # City 0
        (34, 20),  # City 1
        (19, 38),  # City 2
        (14, 91),  # City 3
        (68, 98),  # City 4
        (45, 84),  # City 5
        (4, 56),   # City 6
        (54, 82),  # City 7
        (37, 28),  # City 8
        (27, 45),  # City 9
        (90, 85),  # City 10
        (98, 76),  # City 11
        (6, 19),   # City 12
        (26, 29),  # City 13
        (21, 79),  # City 14
        (49, 23),  # City 15
        (78, 76),  # City 16
        (68, 45),  # City 17
        (50, 28),  # City 18
        (69, 9)    # City 19
    ]
    
    # Requirement 1 & 4
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2
    if sorted(tour) != sorted(list(range(20))):
        return "FAIL"
    
    # Calculate the tour's total travel cost and max distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        dist = calculate_euclidean_distance(*cities_coordinates[city1], *cities_coordinates[city2])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    # Requirement 5
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    # Requirement 6
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Solution provided
tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
total_travel_cost = 477.0516251264448
maximum_distance_between_consecutive_cities = 87.45856161634491

# Verify the solution
result = verify_solution(tour, total_travel_cost, maximum_distance_between_consecutive_cities)
print(result)