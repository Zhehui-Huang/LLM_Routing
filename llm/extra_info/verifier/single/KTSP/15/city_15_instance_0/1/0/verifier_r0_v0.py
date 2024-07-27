import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_tour_requirements():
    cities_coordinates = {
        0: (9, 93),
        1: (8, 51),
        2: (74, 99),
        3: (78, 50),
        4: (21, 23),
        5: (88, 58),
        6: (79, 77),
        7: (63, 23),
        8: (19, 76),
        9: (21, 38),
        10: (19, 65),
        11: (11, 40),
        12: (3, 21),
        13: (60, 55),
        14: (4, 39)
    }
    
    tour = [0, 1, 10, 8, 0]
    reported_total_cost = 90.54

    # Requirement 1, 4, 5
    if len(tour) != 5 or tour[0] != 0 or tour[-1] != 0 or len(set(tour)) != 4:
        return "FAIL"

    # Requirement 3
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        calculated_total_cost += calculate_euclidean_distance(*cities_coordinates[city_a], *cities_coordinates[city_b])
    
    # Comparing calculated cost to reported cost with a tolerance for floating point arithmetic issues
    if not math.isclose(calculated_total_cost, reported_total_drive_time, rel_tol=1e-2):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Execute the test function and print the result
print(test_tour_requirements())