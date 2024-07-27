import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_tour(tour, reported_cost):
    # Define city coordinates
    coordinates = {
        0: (29, 51),
        1: (49, 20),
        2: (79, 69),
        3: (17, 20),
        4: (18, 61),
        5: (40, 57),
        6: (57, 30),
        7: (36, 12),
        8: (93, 43),
        9: (17, 36),
        10: (4, 60),
        11: (78, 82),
        12: (83, 96),
        13: (60, 50),
        14: (98, 1),
    }

    # Requirement 1: Check the number of cities including the depot
    if len(tour) != 7 or tour[0] != tour[-1] or tour[0] != 0:
        return "FAIL"

    # Requirement 2: All cities in the tour must be distinct except depot
    tour_without_depot = tour[1:-1]
    if len(set(tour_without_depot)) != len(tour_without_depot):
        return "FAIL"

    # Requirement 3 & 5: Calculate the actual travel cost and compare
    total_distance = 0
    for i in range(len(tour)-1):
        city1, city2 = tour[i], tour[i+1]
        x1, y1 = coordinates[city1]
        x2, y2 = coordinates[city2]
        total_distance += calculate_euclidean_distance(x1, y1, x2, y2)

    if abs(total_distance - reported_cost) > 1e-2:
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Provided solution
tour = [13, 1, 0, 10, 12, 2, 13]
total_travel_cost = 236.4

# Validate the solution
result = verify_tour(tour, total_travel_cost)
print(result)