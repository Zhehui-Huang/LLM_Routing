import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, total_cost_claimed):
    city_coordinates = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
        5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
        10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
    }

    # [Requirement 1] Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check if exactly 10 unique cities are visited, including the depot city
    if len(set(tour)) != 10:
        return "FAIL"
    
    # Calculate actual total cost
    actual_total_cost = 0
    for i in range(len(tour) - 1):
        actual_total_cost += calculate_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])

    # [Requirement 3] Validate the claimed total travel cost with calculated total cost
    if not math.isclose(actual_total_cost, total_cost_claimed, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

tour = [0, 13, 13, 13, 13, 5, 5, 5, 5, 5, 0]
total_cost_claimed = 64.12335065476415
result = verify_tour(tour, total_cost_claimed)
print(result)