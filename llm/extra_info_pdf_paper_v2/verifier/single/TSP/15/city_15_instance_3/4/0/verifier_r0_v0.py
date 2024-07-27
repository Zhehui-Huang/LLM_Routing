import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, total_travel_cost):
    cities_coordinates = {
        0: (16, 90),
        1: (43, 99),
        2: (80, 21),
        3: (86, 92),
        4: (54, 93),
        5: (34, 73),
        6: (6, 61),
        7: (86, 69),
        8: (30, 50),
        9: (35, 73),
        10: (42, 64),
        11: (64, 30),
        12: (70, 95),
        13: (29, 64),
        14: (32, 79)
    }

    # Requirement 1: Check if all cities are visited
    if len(tour) != 16 or len(set(tour)) != 16:
        return "FAIL"

    # Requirement 2: Check if the robot starts and finishes at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 3: Check travel cost correctness
    actual_total_cost = 0
    for i in range(len(tour) - 1):
        actual_total_cost += calculate_euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])

    # To handle comparison of floating-point precision
    if not math.isclose(actual_total_contracted_cost, total_travel_certified_cost, rel_tol=1e-9):
        return "FAIL"

    # Requirement 4 & 5 are inherently checked by the above conditions
    return "CORRECT"

# Input Tour
tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
total_travel_cost = 373.61

# Validate the solution
print(verify_tour(tour, total_travel_cost))